"""Check the agreed, machine-checkable WEBUILD authoring conventions."""

from collections import Counter
from pathlib import Path
import re
import sys

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS

ROOT = Path(__file__).resolve().parents[2]
MODEL = ROOT / "semantics/model"
W = Namespace("https://example.org/webuild/ontology#")
ONTOLOGY = URIRef("https://example.org/webuild/ontology")
KINDS = (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)


def nonempty_text(value):
    return isinstance(value, Literal) and bool(str(value).strip())


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

    entities = {s for kind in (*KINDS, RDFS.Class, RDF.Property)
                for s in graph.subjects(RDF.type, kind)
                if isinstance(s, URIRef) and str(s).startswith(str(W))}
    for term in sorted(entities):
        types = set(graph.objects(term, RDF.type))
        if not types.intersection(KINDS):
            error(term, "declare the OWL class or specific OWL property type")
        name = str(term)[len(str(W)):]
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
        warnings.append("Imports are present; imported ontologies were not fetched or validated")
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
        part = Graph().parse(path, format="turtle")
        for triple in part:
            combined.add(triple)
    return combined, files


def main():
    try:
        graph, files = load_model(MODEL)
        errors, warnings = check_graph(graph)
    except Exception as exc:
        print(f"FAIL: could not parse the active Turtle model: {exc}")
        return 1
    for message in sorted(set(errors)):
        print(f"ERROR: {message}")
    for message in sorted(set(warnings)):
        print(f"REVIEW: {message}")
    print(f"{'FAIL' if errors else 'PASS'}: {len(files)} active Turtle file(s), "
          f"{len(graph)} triples, {len(set(errors))} error(s)")
    print("Human review required: meaning and hierarchy, US/UK spelling, exact legal "
          "quotations and article/version relevance, use cases and joint approval.")
    print("No OWL reasoner, import closure, source availability or legal-text comparison was run.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
