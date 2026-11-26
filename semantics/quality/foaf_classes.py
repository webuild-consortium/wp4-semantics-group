"""Build the four-class FOAF module approved for the WEBUILD Agent review."""

from pathlib import Path

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import DCTERMS, FOAF, OWL, RDF, RDFS

from dcterms_classes import VERSION as DCTERMS_VERSION

ONTOLOGY = URIRef("https://w3id.org/ebwv/semantic-model/imports/foaf-classes")
VERSION = URIRef(f"{ONTOLOGY}/2026-11-26")
SOURCE = URIRef("https://xmlns.com/foaf/spec/20140114.rdf")


def class_module(source):
    graph = Graph()
    graph.bind("foaf", FOAF)
    graph.add((ONTOLOGY, RDF.type, OWL.Ontology))
    graph.add((ONTOLOGY, OWL.versionIRI, VERSION))
    graph.add((ONTOLOGY, RDFS.label, Literal("FOAF Agent classes — WEBUILD projection", lang="en-GB")))
    graph.add((ONTOLOGY, DCTERMS.source, SOURCE))
    graph.add((ONTOLOGY, OWL.imports, DCTERMS_VERSION))
    for term in (FOAF.Agent, FOAF.Person, FOAF.Group, FOAF.Organization):
        if (term, RDF.type, RDFS.Class) not in source:
            raise ValueError(f"Missing FOAF class declaration: {term}")
        graph.add((term, RDF.type, OWL.Class))
        for predicate in (RDFS.label, RDFS.comment, RDFS.isDefinedBy):
            for value in source.objects(term, predicate):
                graph.add((term, predicate, value))

    for axiom in (
        (FOAF.Person, RDFS.subClassOf, FOAF.Agent),
        (FOAF.Group, RDFS.subClassOf, FOAF.Agent),
        (FOAF.Organization, RDFS.subClassOf, FOAF.Agent),
        (FOAF.Agent, OWL.equivalentClass, DCTERMS.Agent),
    ):
        if axiom not in source:
            raise ValueError(f"Missing approved FOAF axiom: {axiom}")
        graph.add(axiom)
    return graph


if __name__ == "__main__":
    directory = Path(__file__).resolve().parents[1] / "imports/foaf"
    source = Graph().parse(directory / "foaf-20140114.original.rdf", format="xml")
    class_module(source).serialize(directory / "foaf-classes-2026-11-26.ttl", format="turtle")
