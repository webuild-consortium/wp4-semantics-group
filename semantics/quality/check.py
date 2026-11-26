"""Check the agreed, machine-checkable WEBUILD authoring conventions."""

from collections import Counter
from pathlib import Path
import re
import sys

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS, split_uri

from dependencies import load_dependencies

ROOT = Path(__file__).resolve().parents[2]
MODEL = ROOT / "semantics/model"
ONTOLOGY = URIRef("https://w3id.org/ebwv/semantic-model")
W = Namespace(f"{ONTOLOGY}#")
EBWV = Namespace("https://w3id.org/ebwv#")
# Extend only after reviewing reuse against the pinned vocabulary and recording
# that decision. This is a reuse boundary, not a copy of the upstream ontology.
REVIEWED_EBWV_DECLARATIONS = frozenset({EBWV.Agent})
KINDS = (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)


def nonempty_text(value):
    return isinstance(value, Literal) and bool(str(value).strip())


def prefixed_names(graph, term):
    namespace, local = split_uri(term)
    return {f'{prefix}:{local}' for prefix, iri in graph.namespaces()
            if prefix and str(iri) == namespace}


def class_name_pattern(graph, term, qualified_only=False):
    """Match prefixed IRIs exactly and English class names case-insensitively."""
    qualified_names = prefixed_names(graph, term)
    forms = [re.escape(name) for name in qualified_names]
    if not qualified_only:
        local = split_uri(term)[1]
        labels = {local, re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', local)}
        labels.update(name.replace(':', ' ') for name in qualified_names)
        for predicate in (SKOS.prefLabel, RDFS.label):
            labels.update(str(label) for label in graph.objects(term, predicate)
                          if isinstance(label, Literal) and
                          (not label.language or label.language.lower().split('-')[0] == 'en'))
        forms.extend(f'(?i:{re.escape(label)})' for label in labels)
    return '(?:' + '|'.join(forms) + ')' if forms else '(?!)'


def check_taxonomic_wording(graph, term, definitions, warnings):
    local_name = split_uri(term)[1]
    parents = {parent for parent in graph.objects(term, RDFS.subClassOf)
               if isinstance(parent, URIRef) and parent not in (term, OWL.Thing)}
    if parents:
        subject = class_name_pattern(graph, term)
        parent_names = '|'.join(class_name_pattern(graph, parent, split_uri(parent)[1] == local_name)
                                for parent in parents)
        opening = re.compile(rf'^An? {subject} is an? (?:{parent_names})(?:,?\s+)\w')
        reference = re.compile(rf'(?<![\w.:/#-])(?:{parent_names})(?![\w:-]|\.\w)')
        for definition in definitions:
            language = getattr(definition, 'language', None)
            if language and language.lower().split('-')[0] != 'en':
                continue
            text = ' '.join(str(definition).split())
            if not reference.search(text):
                yield (f"{term}: taxonomic definition must name its direct superclass "
                       f"({', '.join(sorted(parents))}); use a prefixed name for a same-named superclass")
            elif not opening.match(text):
                warnings.append(f"{term}: alternative wording names a superclass; "
                                "review the distinguishing characteristics in context")

    for parent in graph.objects(term, RDFS.subPropertyOf):
        if not isinstance(parent, URIRef) or parent == term or split_uri(parent)[1] != local_name:
            continue
        for definition in definitions:
            if not any(re.search(rf"(?<![\w.:/#-]){re.escape(name)}(?![\w:-]|\.\w)", str(definition))
                       for name in prefixed_names(graph, parent)):
                yield f"{term}: taxonomic definition must use a prefixed name for {parent}"


def check_graph(graph):
    """Return errors and review warnings; do not fetch imports or source URIs."""
    errors, warnings = [], []

    def error(term, message):
        errors.append(f"{term}: {message}")

    if (ONTOLOGY, RDF.type, OWL.Ontology) not in graph:
        error(ONTOLOGY, "missing agreed ontology declaration")
    for prop in (SKOS.prefLabel, SKOS.altLabel, DCTERMS.source,
                 W.taxonomicDefinition, W.legalDefinition, W.businessDefinition):
        if (prop, RDF.type, OWL.AnnotationProperty) not in graph:
            error(prop, "missing annotation property declaration")

    # Apply editorial rules to new extension terms and to reused EBWV terms
    # explicitly augmented with our definitions. A bare external declaration
    # does not require rewriting that vocabulary's original annotations.
    declared = {s for kind in (*KINDS, RDFS.Class, RDF.Property)
                for s in graph.subjects(RDF.type, kind) if isinstance(s, URIRef)}
    for term in declared:
        if (str(term).startswith(str(EBWV))
                and term not in REVIEWED_EBWV_DECLARATIONS):
            error(term, "EBWV declarations require reviewed reuse; new terms belong in ebwsm")
    definitions = (W.taxonomicDefinition, W.legalDefinition, W.businessDefinition)
    augmented = {s for prop in definitions for s in graph.subjects(prop, None)
                 if isinstance(s, URIRef) and str(s).startswith(str(EBWV))}
    entities = {s for s in declared if str(s).startswith(str(W))} | augmented
    for prop in (EBWV.taxonomicDefinition, EBWV.legalDefinition, EBWV.businessDefinition):
        if (any(graph.triples((prop, None, None)))
                or any(graph.triples((None, prop, None)))
                or any(graph.triples((None, OWL.annotatedProperty, prop)))):
            error(prop, "extension definition properties must use the ebwsm namespace")
    for term in sorted(entities):
        types = set(graph.objects(term, RDF.type))
        if not types.intersection(KINDS):
            error(term, "declare the OWL class or specific OWL property type")
        namespace = W if str(term).startswith(str(W)) else EBWV
        name = str(term)[len(str(namespace)):]
        if OWL.Class in types or RDFS.Class in types:
            if not re.fullmatch(r"[A-Z][A-Za-z0-9]*", name):
                error(term, "class name must use UpperCamelCase")
        if types.intersection({OWL.ObjectProperty, OWL.DatatypeProperty,
                               OWL.AnnotationProperty, RDF.Property}):
            if not re.fullmatch(r"[a-z][A-Za-z0-9]*", name):
                error(term, "property name must use lowerCamelCase")

        preferred = set(graph.objects(term, SKOS.prefLabel))
        alternatives = set(graph.objects(term, SKOS.altLabel))
        for label in preferred | alternatives:
            if not nonempty_text(label) or not label.language:
                error(term, "labels must be non-empty language-tagged literals")
        languages = Counter((v.language or "").lower() for v in preferred
                            if isinstance(v, Literal))
        if languages["en-gb"] != 1:
            error(term, "exactly one en-GB preferred label is required")
        if any(count > 1 for count in languages.values()):
            error(term, "at most one preferred label per language is allowed")
        if preferred & alternatives:
            error(term, "a literal cannot be both preferred and alternative label")

        definitions = list(graph.objects(term, W.taxonomicDefinition))
        if not definitions:
            error(term, "taxonomic or base definition is required")
        errors.extend(check_taxonomic_wording(graph, term, definitions, warnings))
        for prop in (W.taxonomicDefinition, W.legalDefinition, W.businessDefinition):
            if any(not nonempty_text(v) for v in graph.objects(term, prop)):
                error(term, f"{prop} must contain non-empty definition text")

    # Apply global-property rules to axioms present in the authored graph,
    # including any statements about reused properties. Imports are not loaded.
    for kind in (OWL.ObjectProperty, OWL.DatatypeProperty):
        for term in graph.subjects(RDF.type, kind):
            if any(graph.objects(term, RDFS.domain)):
                error(term, "global rdfs:domain is prohibited")
            if kind == OWL.ObjectProperty and any(graph.objects(term, RDFS.range)):
                error(term, "global rdfs:range is prohibited for object properties")

    # A source must annotate the exact legal-definition assertion, including
    # the literal's language/datatype. A source on the entity is insufficient.
    legal_axioms = {}
    for axiom in graph.subjects(OWL.annotatedProperty, W.legalDefinition):
        if (axiom, RDF.type, OWL.Axiom) not in graph:
            error(axiom, "legal-definition source must annotate an owl:Axiom")
            continue
        subjects = list(graph.objects(axiom, OWL.annotatedSource))
        targets = list(graph.objects(axiom, OWL.annotatedTarget))
        if len(subjects) != 1 or len(targets) != 1:
            error(axiom, "source annotation needs one subject and one definition target")
            continue
        subject, target = subjects[0], targets[0]
        if (subject, W.legalDefinition, target) not in graph:
            error(subject, "source annotation refers to a missing or changed legal definition")
        legal_axioms.setdefault((subject, target), []).append(axiom)

    for term, definition in graph.subject_objects(W.legalDefinition):
        if not nonempty_text(definition):
            error(term, "legal definition must contain non-empty text")
        sources = {source for ax in legal_axioms.get((term, definition), [])
                   for source in graph.objects(ax, DCTERMS.source)}
        valid = False
        for source in sources:
            if isinstance(source, URIRef) and re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", str(source)):
                valid = True
            elif nonempty_text(source):
                valid = True
                warnings.append(f"{term}: textual source reference; prefer an official article URI")
            else:
                error(term, "source must be an absolute IRI or a non-empty textual citation")
        if not valid:
            error(term, "legal definition lacks a source on its exact assertion")

    if any(graph.triples((None, OWL.imports, None))):
        warnings.append("Imported axioms retain their source conventions; the full suite checks the pinned import closure")
    return errors, warnings


def load_model(directory):
    """Parse modules separately so blank node identifiers cannot cross files."""
    files = sorted(path for path in directory.rglob("*.ttl")
                   if not {"Archive", "modelling_considerations"}.intersection(
                       path.relative_to(directory).parts))
    if directory / "webuild.ttl" not in files:
        raise ValueError("semantics/model/webuild.ttl is missing")
    combined = Graph()
    for path in files:
        combined.parse(path, format="turtle")
    return combined, files


def main():
    try:
        graph, files = load_model(MODEL)
        errors, warnings = check_graph(graph)
        dependencies = load_dependencies(graph, MODEL)
    except Exception as exc:
        print(f"FAIL: could not load the active model and pinned dependencies: {exc}")
        return 1
    for message in sorted(set(errors)):
        print(f"ERROR: {message}")
    for message in sorted(set(warnings)):
        print(f"REVIEW: {message}")
    print(f"{'FAIL' if errors else 'PASS'}: {len(files)} active Turtle file(s), "
          f"{len(graph)} triples, {len(set(errors))} error(s)")
    print("Human review required: meaning and hierarchy, US/UK spelling, exact legal "
          "quotations and article/version relevance, use cases and joint approval.")
    print("Structural checks only. The full suite runs HermiT separately.")
    print(f"Dependencies: {len({item.path for item in dependencies})} pinned local document(s), complete import closure verified.")
    print("Editorial scope: authored graph only. HermiT includes pinned imports; the full upstream EBWV vocabulary remains outside the import closure.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
