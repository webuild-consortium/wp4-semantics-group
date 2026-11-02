#!/usr/bin/env python3
"""Verify every JSON-LD example in vocabulary.yml against the current sources.

The script rebuilds the JSON-LD context from the current `vocabulary.yml`
(via the bundled `yml2vocab`) and then checks every ``json: |`` example block,
node by node, applying the ebwv resolution rules:

* the context is **type-scoped and @protected** - a property is only defined
  when the enclosing node carries a `@type` whose scoped `@context` defines it
  (scoped contexts of all of a node's types are unioned), in addition to the
  globally defined top-level terms, the Verifiable-Credentials v2 base terms
  and the JSON-LD keywords;
* `@type: @id`   -> a string value must be an absolute IRI or a defined term
  (a bare string such as "CEO" would expand to a relative IRI -> flagged);
* `@type: @vocab` -> a string value must be one of the mapped tokens
  (otherwise it falls through to the `ebwv:INVALID_VALUE:` sentinel);
* value objects (`{"@type": "<Datatype>", "@value": ...}`) -> the datatype
  must be a defined term.

Exit code is non-zero if any example has findings.

Usage:
    python3 vocab/scripts/verify-examples.py [--no-build] [path/to/vocabulary.yml]

By default the context is regenerated from the source. With --no-build the
already-built context at docs/ebwv/v0.1/vocabulary.context.jsonld is used.
"""
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC_YML = os.path.join(ROOT, "vocab", "src", "vocabulary.yml")
TEMPLATE = os.path.join(ROOT, "vocab", "src", "template.html")
YML2VOCAB = os.path.join(ROOT, "vocab", "scripts", "yml2vocab")
BUILT_CTX = os.path.join(ROOT, "docs", "ebwv", "v0.1", "vocabulary.context.jsonld")
EBWV_CTX_URL = "https://w3id.org/ebwv/v0.1"

KEYWORDS = {
    "@context", "@id", "@type", "@value", "@graph", "@list", "@set",
    "@language", "@direction", "@index", "@reverse", "@json", "@none", "@container",
}

# Verifiable Credentials v2 base-context terms (not part of the ebwv file).
VC_BASE = {
    "VerifiableCredential", "VerifiablePresentation",
    "EnvelopedVerifiableCredential", "EnvelopedVerifiablePresentation",
    "credentialSubject", "issuer", "validFrom", "validUntil",
    "issuanceDate", "expirationDate", "credentialStatus", "credentialSchema",
    "termsOfUse", "evidence", "refreshService", "renderMethod", "proof",
    "id", "type", "name", "description",
    "BitstringStatusListEntry", "BitstringStatusList",
    "DataIntegrityProof", "JsonSchema",
}

IRI_SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")


def build_context():
    """Regenerate the context from source; return (context_dict, note)."""
    if not os.path.exists(YML2VOCAB):
        return load_built(), "yml2vocab not found - used already-built context"
    generated = [
        os.path.join(ROOT, "vocab", "src", n)
        for n in ("vocabulary.html", "vocabulary.jsonld",
                  "vocabulary.ttl", "vocabulary.context.jsonld")
    ]
    pre_existing = {p for p in generated if os.path.exists(p)}
    try:
        subprocess.run(
            [YML2VOCAB, "-v", SRC_YML, "-t", TEMPLATE, "-c"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        )
    except (subprocess.CalledProcessError, OSError) as exc:
        return load_built(), f"build failed ({exc}); used already-built context"
    ctx_path = os.path.join(ROOT, "vocab", "src", "vocabulary.context.jsonld")
    with open(ctx_path) as handle:
        ctx = json.load(handle)["@context"]
    # Clean up freshly generated artifacts so the source tree stays tidy.
    for path in generated:
        if path not in pre_existing and os.path.exists(path):
            os.remove(path)
    return ctx, "context rebuilt from current source"


def load_built():
    with open(BUILT_CTX) as handle:
        return json.load(handle)["@context"]


def scoped_terms(ctx, types):
    """Union of the scoped-context keys for the given node types."""
    terms = set()
    for typ in types:
        definition = ctx.get(typ)
        if isinstance(definition, dict) and isinstance(definition.get("@context"), dict):
            terms.update(k for k in definition["@context"] if not k.startswith("@"))
    return terms


def term_def(ctx, types, key):
    """Resolve a term definition, preferring a type-scoped one."""
    for typ in types:
        definition = ctx.get(typ)
        if isinstance(definition, dict) and isinstance(definition.get("@context"), dict):
            if key in definition["@context"]:
                return definition["@context"][key]
    return ctx.get(key)


def as_list(value):
    return value if isinstance(value, list) else [value]


def node_types(node):
    return [t for t in as_list(node.get("@type", [])) if isinstance(t, str)]


def check_node(ctx, top_level, node, types, path, findings):
    available = KEYWORDS | VC_BASE | top_level | scoped_terms(ctx, types)
    tstr = "+".join(types) if types else "(no @type)"
    for key, value in node.items():
        if key in KEYWORDS:
            continue
        loc = f"{path}.{key}"
        if key not in available:
            findings.append(f"UNDEFINED  {loc}  (property not in scope of <{tstr}>)")
            # still recurse so nested problems surface
            recurse_values(ctx, top_level, value, loc, findings)
            continue
        definition = term_def(ctx, types, key)
        check_value(ctx, top_level, definition, value, loc, findings)


def check_value(ctx, top_level, definition, value, loc, findings):
    coerce = definition.get("@type") if isinstance(definition, dict) else None

    for item in as_list(value):
        if isinstance(item, dict) and "@value" in item:
            dt = item.get("@type")
            if isinstance(dt, str) and dt not in KEYWORDS and dt not in top_level \
                    and not IRI_SCHEME.match(dt):
                findings.append(f"BAD-DATATYPE  {loc}  (value @type '{dt}' is not a defined datatype)")
            continue
        if isinstance(item, dict):
            # a nested node - recurse using its own @type
            check_node(ctx, top_level, item, node_types(item), loc, findings)
            continue
        if isinstance(item, str):
            if coerce == "@vocab":
                inner = definition.get("@context", {}) if isinstance(definition, dict) else {}
                # A mapped token is fine; an absolute IRI is kept as-is by @vocab
                # expansion; only an unmapped bare token hits ebwv:INVALID_VALUE:.
                if item not in inner and not IRI_SCHEME.match(item):
                    findings.append(f"INVALID-VOCAB  {loc}  (token '{item}' not in {sorted(k for k in inner if not k.startswith('@'))})")
            elif coerce == "@id":
                if not IRI_SCHEME.match(item) and item not in top_level:
                    findings.append(f"RELATIVE-IRI  {loc}  (@id value '{item}' is neither an absolute IRI nor a defined term)")


def recurse_values(ctx, top_level, value, loc, findings):
    for item in as_list(value):
        if isinstance(item, dict) and "@value" not in item:
            check_node(ctx, top_level, item, node_types(item), loc, findings)


def extract_examples(yml_text):
    """Yield (label, json_text, line_no) for every `json: |` block."""
    lines = yml_text.splitlines()
    i = 0
    last_label = None
    while i < len(lines):
        line = lines[i]
        m_label = re.match(r"\s*-?\s*label:\s*(.+?)\s*$", line)
        if m_label:
            last_label = m_label.group(1)
        m_json = re.match(r"^(\s*)json:\s*\|\s*$", line)
        if m_json:
            key_indent = len(m_json.group(1))
            body = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if nxt.strip() == "":
                    body.append("")
                    j += 1
                    continue
                indent = len(nxt) - len(nxt.lstrip())
                if indent <= key_indent:
                    break
                body.append(nxt)
                j += 1
            # dedent by the minimum indent of non-empty body lines
            indents = [len(b) - len(b.lstrip()) for b in body if b.strip()]
            cut = min(indents) if indents else 0
            text = "\n".join(b[cut:] if b.strip() else "" for b in body).rstrip()
            yield (last_label or f"example@L{i + 1}", text, i + 1)
            i = j
            continue
        i += 1


def main():
    args = [a for a in sys.argv[1:] if a != "--no-build"]
    no_build = "--no-build" in sys.argv
    yml_path = args[0] if args else SRC_YML

    if no_build:
        ctx, note = load_built(), "used already-built context (--no-build)"
    else:
        ctx, note = build_context()
    top_level = {k for k in ctx if not k.startswith("@")}

    with open(yml_path) as handle:
        yml_text = handle.read()

    total = 0
    failed = 0
    print(f"Verifying examples in {os.path.relpath(yml_path, ROOT)}  [{note}]\n")
    for label, text, line_no in extract_examples(yml_text):
        total += 1
        findings = []
        try:
            doc = json.loads(text)
        except json.JSONDecodeError as exc:
            print(f"  [FAIL] {label} (L{line_no}) - invalid JSON: {exc}")
            failed += 1
            continue
        check_node(ctx, top_level, doc, node_types(doc), "$", findings)
        if findings:
            failed += 1
            print(f"  [FAIL] {label} (L{line_no})")
            for f in findings:
                print(f"           {f}")
        else:
            print(f"  [ OK ] {label} (L{line_no})")

    print(f"\n{total - failed}/{total} examples verified; {failed} with findings.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
