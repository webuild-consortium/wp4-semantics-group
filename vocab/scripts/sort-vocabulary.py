#!/usr/bin/env python3
"""Sort entries within each section of vocabulary.yml alphabetically by id.

The prefix of an id (everything up to and including the first ':') is ignored
for sorting, so e.g. `cred:CredentialSubject` sorts as `CredentialSubject` and
`schema:name` sorts as `name`. Sorting is case-insensitive.

Only sections whose entries all carry an `id:` are sorted; any other section
(e.g. `ontology`, whose entries use `property:`) is left untouched. Entry
formatting, comments and multi-line block scalars are preserved verbatim.

Usage:
    python3 sort-vocabulary.py [path/to/vocabulary.yml]
"""
import re
import sys

DEFAULT_PATH = "vocab/src/vocabulary.yml"

SECTION_RE = re.compile(r"^(\w+):\s*(?:#.*)?$")
ENTRY_RE = re.compile(r"^  - ")
ID_RE = re.compile(r"^  - id:\s*(\S+)")


def sort_key(entry_lines):
    """Return the case-insensitive sort key for an entry, or None if no id."""
    for line in entry_lines:
        m = ID_RE.match(line)
        if m:
            raw = m.group(1)
            # Ignore the prefix: keep the part after the first ':' if present.
            local = raw.split(":", 1)[1] if ":" in raw else raw
            return local.casefold()
    return None


def split_entries(body):
    """Split a section body (list of lines) into entry blocks.

    Each block keeps its own lines; trailing blank lines are dropped so they
    can be re-inserted uniformly when re-joining.
    """
    entries = []
    current = []
    for line in body:
        if ENTRY_RE.match(line):
            if current:
                entries.append(current)
            current = [line]
        else:
            if current:
                current.append(line)
            # lines before the first entry (rare) are ignored/preserved below
    if current:
        entries.append(current)

    # Strip trailing blank lines from each entry.
    for entry in entries:
        while entry and entry[-1].strip() == "":
            entry.pop()
    return entries


def sort_section(body):
    """Return sorted body lines for a section, or None if it can't be sorted."""
    entries = split_entries(body)
    if not entries:
        return None

    keyed = []
    for entry in entries:
        key = sort_key(entry)
        if key is None:
            return None  # section has non-id entries -> leave untouched
        keyed.append((key, entry))

    keyed.sort(key=lambda pair: pair[0])

    out = []
    for _, entry in keyed:
        out.extend(entry)
        out.append("\n")  # one blank line between entries
    return out


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PATH
    with open(path) as f:
        lines = f.readlines()

    out = []
    i = 0
    n = len(lines)
    changed_sections = []

    while i < n:
        line = lines[i]
        m = SECTION_RE.match(line.rstrip())
        if not m or m.group(1) in ("true", "false", "null"):
            out.append(line)
            i += 1
            continue

        section_name = m.group(1)
        out.append(line)  # keep section header verbatim (incl. inline comment)
        i += 1

        # Collect body until next section header or EOF.
        body = []
        while i < n:
            nxt = SECTION_RE.match(lines[i].rstrip())
            if nxt and nxt.group(1) not in ("true", "false", "null"):
                break
            body.append(lines[i])
            i += 1

        sorted_body = sort_section(body)
        if sorted_body is None:
            out.extend(body)
        else:
            out.extend(sorted_body)
            changed_sections.append(section_name)

    with open(path, "w") as f:
        f.writelines(out)

    print(f"Sorted sections: {', '.join(changed_sections)}")


if __name__ == "__main__":
    main()
