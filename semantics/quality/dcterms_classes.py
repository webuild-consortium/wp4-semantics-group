"""Reproduce the approved class-only OWL projection of the pinned DCMI schema."""

from pathlib import Path

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS

ONTOLOGY = URIRef("https://w3id.org/ebwv/semantic-model/imports/dcterms-classes")
VERSION = URIRef(f"{ONTOLOGY}/2026-11-23")
SOURCE = URIRef("https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl")
COMMENT = (
    "WEBUILD class-only OWL projection of the pinned DCMI Terms RDF schema. "
    "This is a locally derived module, not an official DCMI OWL distribution or "
    "a complete vocabulary import. It preserves the 22 class IRIs, their source "
    "labels, definition comments, descriptive notes and isDefinedBy links, and "
    "all eight subclass edges between those classes. RDFS class declarations "
    "are represented as OWL class declarations. RDF metamodel statements "
    "dcterms:Agent rdf:type dcterms:AgentClass and dcterms:AgentClass "
    "rdfs:subClassOf rdfs:Class are deliberately excluded; they are not "
    "domain-class hierarchy edges. Property definitions, datatypes, encoding "
    "schemes and issuance metadata are outside this module. No additional "
    "class mappings, disjointness or restrictions are introduced."
)


def class_module(source):
    """Return exactly the approved projection, including its provenance header."""
    graph = Graph()
    for name, namespace in (("dcterms", DCTERMS), ("owl", OWL), ("rdf", RDF), ("rdfs", RDFS)):
        graph.bind(name, namespace)
    graph.add((ONTOLOGY, RDF.type, OWL.Ontology))
    graph.add((ONTOLOGY, OWL.versionIRI, VERSION))
    graph.add((ONTOLOGY, RDFS.label, Literal("Dublin Core Terms class hierarchy — WEBUILD projection", lang="en-GB")))
    graph.add((ONTOLOGY, RDFS.comment, Literal(COMMENT, lang="en-GB")))
    graph.add((ONTOLOGY, DCTERMS.source, SOURCE))
    graph.add((DCTERMS.source, RDF.type, OWL.AnnotationProperty))
    graph.add((DCTERMS.description, RDF.type, OWL.AnnotationProperty))
    classes = {term for term in source.subjects(RDF.type, RDFS.Class)
               if isinstance(term, URIRef) and str(term).startswith(str(DCTERMS))}
    annotations = (RDFS.label, RDFS.comment, RDFS.isDefinedBy, DCTERMS.description)
    for term in classes:
        graph.add((term, RDF.type, OWL.Class))
        for predicate in annotations:
            for value in source.objects(term, predicate):
                graph.add((term, predicate, value))
        for parent in source.objects(term, RDFS.subClassOf):
            if parent in classes:
                graph.add((term, RDFS.subClassOf, parent))
            elif (term, parent) != (DCTERMS.AgentClass, RDFS.Class):
                raise ValueError(f"Unreviewed external superclass in DCMI projection: {term} -> {parent}")
    return graph


if __name__ == "__main__":
    directory = Path(__file__).resolve().parents[1] / "imports/dcterms"
    source = Graph().parse(directory / "dublin_core_terms.original.ttl", format="turtle")
    target = directory / "dcterms-classes-2026-11-23.ttl"
    class_module(source).serialize(target, format="turtle")
    print(f"Wrote {target}; update its manifest checksum and rerun the quality suite.")
