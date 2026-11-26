"""Check that reasoning cannot silently omit or replace imported axioms."""

from hashlib import sha256
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS

from dependencies import load_dependencies
from dcterms_classes import VERSION, class_module

ROOT = URIRef("urn:test:root")
ONE = URIRef("urn:test:one")
TWO = URIRef("urn:test:two")


class DependencyChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.model = self.root / "model"
        self.imports = self.root / "imports"
        self.model.mkdir()
        self.imports.mkdir()
        self.graph = Graph()
        self.graph.add((ROOT, RDF.type, OWL.Ontology))
        self.graph.add((ROOT, OWL.imports, ONE))
        self.records = []
        self.mappings = []

    def document(self, iri, name, imports=(), declared=None, version=None):
        graph = Graph()
        graph.add((declared or iri, RDF.type, OWL.Ontology))
        if version:
            graph.add((declared or iri, OWL.versionIRI, version))
        for target in imports:
            graph.add((declared or iri, OWL.imports, target))
        path = self.imports / name
        graph.serialize(path, format="turtle")
        record = {"iri": str(iri), "file": name,
                  "sha256": sha256(path.read_bytes()).hexdigest()}
        self.records.append(record)
        self.mappings.append((str(iri), "../imports/" + name))
        return path, record

    def save(self):
        (self.imports / "manifest.json").write_text(json.dumps({
            "format_version": 1, "imports": self.records}))
        entries = "".join(f'<uri name="{iri}" uri="{path}"/>'
                          for iri, path in self.mappings)
        (self.model / "catalog-v001.xml").write_text(
            '<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">'
            + entries + '</catalog>')

    def test_no_imports_need_no_catalogue(self):
        self.graph.remove((None, OWL.imports, None))
        self.assertEqual([], load_dependencies(self.graph, self.model))

    def test_complete_transitive_closure_and_cycles(self):
        self.document(ONE, "one.ttl", imports=[TWO])
        self.document(TWO, "two.ttl", imports=[ONE, ROOT])
        self.save()
        result = load_dependencies(self.graph, self.model)
        self.assertEqual({ONE, TWO}, {item.iri for item in result})

    def test_version_iri_can_identify_the_requested_import(self):
        self.document(ONE, "one.ttl", declared=TWO, version=ONE)
        self.save()
        self.assertEqual(1, len(load_dependencies(self.graph, self.model)))

    def test_missing_transitive_import_fails(self):
        self.document(ONE, "one.ttl", imports=[TWO])
        self.save()
        with self.assertRaisesRegex(ValueError, "Unmapped or unpinned"):
            load_dependencies(self.graph, self.model)

    def test_changed_dependency_checksum_fails(self):
        path, _ = self.document(ONE, "one.ttl")
        self.save()
        path.write_text(path.read_text() + '\n# changed\n')
        with self.assertRaisesRegex(ValueError, "checksum mismatch"):
            load_dependencies(self.graph, self.model)

    def test_matching_file_with_wrong_ontology_identity_fails(self):
        self.document(ONE, "one.ttl", declared=TWO)
        self.save()
        with self.assertRaisesRegex(ValueError, "does not declare requested"):
            load_dependencies(self.graph, self.model)

    def test_non_ontology_version_statement_cannot_hide_missing_import(self):
        self.document(ONE, "one.ttl", imports=[TWO])
        self.graph.add((URIRef("urn:test:ordinary-resource"), OWL.versionIRI, TWO))
        self.save()
        with self.assertRaisesRegex(ValueError, "Unmapped or unpinned"):
            load_dependencies(self.graph, self.model)

    def test_literal_import_target_is_rejected(self):
        self.document(ONE, "one.ttl")
        self.graph.add((ROOT, OWL.imports, Literal("not-an-IRI")))
        self.save()
        with self.assertRaisesRegex(ValueError, "must be IRIs"):
            load_dependencies(self.graph, self.model)

    def test_catalogue_cannot_override_the_pinned_document(self):
        self.document(ONE, "one.ttl")
        self.mappings = [(str(ONE), "../imports/other.ttl")]
        self.save()
        with self.assertRaisesRegex(ValueError, "Catalogue and manifest disagree"):
            load_dependencies(self.graph, self.model)

    def test_catalogue_cannot_escape_the_import_directory(self):
        self.document(ONE, "one.ttl")
        self.mappings = [(str(ONE), "../../elsewhere.ttl")]
        self.save()
        with self.assertRaisesRegex(ValueError, "leaves the imports directory"):
            load_dependencies(self.graph, self.model)

    def test_correction_does_not_authorise_other_changes(self):
        path, record = self.document(ONE, "one.ttl")
        prop = URIRef("urn:test:property")
        original = Graph().parse(path, format="turtle")
        original.add((prop, RDF.type, OWL.ObjectProperty))
        original.add((prop, RDF.type, OWL.AnnotationProperty))
        upstream = self.imports / "original.ttl"
        original.serialize(upstream, format="turtle")
        original.remove((prop, RDF.type, OWL.AnnotationProperty))
        original.add((prop, RDFS.comment, Literal("Unapproved change")))
        original.serialize(path, format="turtle")
        record.update({
            "sha256": sha256(path.read_bytes()).hexdigest(),
            "upstream_file": "original.ttl",
            "upstream_sha256": sha256(upstream.read_bytes()).hexdigest(),
            "remove_annotation_property_declarations": [str(prop)],
        })
        self.save()
        with self.assertRaisesRegex(ValueError, "beyond its approved correction"):
            load_dependencies(self.graph, self.model)

    def test_approved_provo_copy_preserves_both_object_properties(self):
        model = Path(__file__).resolve().parents[1] / "model"
        graph = Graph().parse(model / "webuild.ttl", format="turtle")
        imports = load_dependencies(graph, model)
        self.assertEqual(3, len(imports))
        prov = next(item.graph for item in imports
                    if str(item.iri) == "http://www.w3.org/ns/prov#")
        effective = graph + prov
        for name in ["wasRevisionOf", "specializationOf"]:
            prop = URIRef("http://www.w3.org/ns/prov#" + name)
            self.assertIn((prop, RDF.type, OWL.ObjectProperty), effective)
            self.assertIn((prop, RDF.type, OWL.ObjectProperty), prov)
            self.assertNotIn((prop, RDF.type, OWL.AnnotationProperty), graph)
            self.assertNotIn((prop, RDF.type, OWL.AnnotationProperty), prov)

    def test_provo_import_matches_the_ontology_identity_loaded_by_protege(self):
        model = Path(__file__).resolve().parents[1] / "model"
        graph = Graph().parse(model / "webuild.ttl", format="turtle")
        imported = set(graph.objects(None, OWL.imports))
        self.assertIn(URIRef("http://www.w3.org/ns/prov#"), imported)
        self.assertNotIn(URIRef("http://www.w3.org/ns/prov-o-20130430"), imported)
        prov = next(item.graph for item in load_dependencies(graph, model)
                    if str(item.iri) == "http://www.w3.org/ns/prov#")
        self.assertIn((URIRef("http://www.w3.org/ns/prov#Agent"), RDF.type, OWL.Class), prov)
        self.assertIn((URIRef("http://www.w3.org/ns/prov#Activity"), OWL.disjointWith,
                       URIRef("http://www.w3.org/ns/prov#Entity")), prov)

    def test_wrong_published_version_pin_fails(self):
        _, record = self.document(ONE, "one.ttl", version=TWO)
        record["published_version_iri"] = "urn:test:other-version"
        self.save()
        with self.assertRaisesRegex(ValueError, "published version is absent"):
            load_dependencies(self.graph, self.model)

    def test_dcterms_module_preserves_classes_source_text_and_domain_hierarchy(self):
        directory = Path(__file__).resolve().parents[1] / "imports/dcterms"
        source = Graph().parse(directory / "dublin_core_terms.original.ttl", format="turtle")
        module = Graph().parse(directory / "dcterms-classes-2026-11-23.ttl", format="turtle")
        classes = set(source.subjects(RDF.type, RDFS.Class))
        self.assertEqual(22, len(classes))
        self.assertEqual(classes, set(module.subjects(RDF.type, OWL.Class)))
        expected = {(s, p, o) for s, p, o in source.triples((None, RDFS.subClassOf, None))
                    if s in classes and o in classes}
        self.assertEqual(8, len(expected))
        self.assertEqual(expected, set(module.triples((None, RDFS.subClassOf, None))))
        self.assertIn((DCTERMS.PeriodOfTime, RDFS.subClassOf,
                       DCTERMS.LocationPeriodOrJurisdiction), module)
        for term in classes:
            for predicate in (RDFS.label, RDFS.comment, RDFS.isDefinedBy, DCTERMS.description):
                self.assertEqual(set(source.objects(term, predicate)),
                                 set(module.objects(term, predicate)))

    def test_dcterms_module_does_not_import_properties_or_rdf_metamodel(self):
        directory = Path(__file__).resolve().parents[1] / "imports/dcterms"
        graph = Graph().parse(directory / "dcterms-classes-2026-11-23.ttl", format="turtle")
        for kind in (OWL.ObjectProperty, OWL.DatatypeProperty, RDF.Property, RDFS.Datatype):
            self.assertFalse(list(graph.subjects(RDF.type, kind)))
        for predicate in (RDFS.domain, RDFS.range, RDFS.subPropertyOf, OWL.imports):
            self.assertFalse(list(graph.triples((None, predicate, None))))
        self.assertNotIn((DCTERMS.Agent, RDF.type, DCTERMS.AgentClass), graph)
        self.assertNotIn((DCTERMS.AgentClass, RDFS.subClassOf, RDFS.Class), graph)

    def test_dcterms_projection_cannot_add_an_unapproved_superclass_even_with_updated_hash(self):
        path, record = self.document(VERSION, "classes.ttl")
        self.graph.remove((ROOT, OWL.imports, ONE))
        self.graph.add((ROOT, OWL.imports, VERSION))
        directory = Path(__file__).resolve().parents[1] / "imports/dcterms"
        original = self.imports / "original.ttl"
        original.write_bytes((directory / "dublin_core_terms.original.ttl").read_bytes())
        source = Graph().parse(original, format="turtle")
        graph = class_module(source)
        graph.add((DCTERMS.Agent, RDFS.subClassOf, DCTERMS.PeriodOfTime))
        graph.serialize(path, format="turtle")
        record.update({
            "sha256": sha256(path.read_bytes()).hexdigest(),
            "upstream_file": "original.ttl",
            "upstream_sha256": sha256(original.read_bytes()).hexdigest(),
            "projection": "dcterms-classes-v1",
        })
        self.save()
        with self.assertRaisesRegex(ValueError, "beyond its approved class projection"):
            load_dependencies(self.graph, self.model)


if __name__ == "__main__":
    unittest.main()
