"""Behaviour checks for accepted models and common authoring mistakes."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from rdflib import BNode, Graph, Literal, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS, XSD

from check import ONTOLOGY, W, check_graph, load_model


class QualityChecks(unittest.TestCase):
    def setUp(self):
        self.g = Graph()
        self.g.add((ONTOLOGY, RDF.type, OWL.Ontology))
        for prop in (SKOS.prefLabel, SKOS.altLabel, DCTERMS.source,
                     W.taxonomicDefinition, W.legalDefinition, W.businessDefinition):
            self.g.add((prop, RDF.type, OWL.AnnotationProperty))
        for term, kind in ((W.taxonomicDefinition, OWL.AnnotationProperty),
                           (W.legalDefinition, OWL.AnnotationProperty),
                           (W.businessDefinition, OWL.AnnotationProperty),
                           (W.Organization, OWL.Class),
                           (W.hasAddress, OWL.ObjectProperty),
                           (W.birthDate, OWL.DatatypeProperty)):
            self.g.add((term, RDF.type, kind))
            self.g.add((term, SKOS.prefLabel, Literal(str(term).split('#')[-1], lang='en-GB')))
            self.g.add((term, W.taxonomicDefinition, Literal('A base definition.', lang='en-GB')))

    def errors(self):
        return '\n'.join(check_graph(self.g)[0])

    def legal(self, text='Quoted definition.', lang='en-GB'):
        definition = Literal(text, lang=lang)
        self.g.add((W.Organization, W.legalDefinition, definition))
        ax = BNode()
        for p, v in ((RDF.type, OWL.Axiom), (OWL.annotatedSource, W.Organization),
                     (OWL.annotatedProperty, W.legalDefinition),
                     (OWL.annotatedTarget, definition),
                     (DCTERMS.source, URIRef('https://example.org/law/article/1'))):
            self.g.add((ax, p, v))
        return ax, definition

    def test_base_definitions_need_no_artificial_parent(self):
        self.assertEqual('', self.errors())

    def test_datatype_range_is_allowed_and_optional(self):
        self.g.add((W.birthDate, RDFS.range, XSD.date))
        self.assertEqual('', self.errors())

    def test_object_range_and_both_domains_are_rejected(self):
        self.g.add((W.hasAddress, RDFS.range, W.Organization))
        self.g.add((W.hasAddress, RDFS.domain, W.Organization))
        self.g.add((W.birthDate, RDFS.domain, W.Organization))
        self.assertEqual(3, len(check_graph(self.g)[0]))

    def test_missing_preferred_label_is_rejected(self):
        self.g.remove((W.Organization, SKOS.prefLabel, None))
        self.assertIn('exactly one en-GB', self.errors())

    def test_duplicate_preferred_label_in_same_language_is_rejected(self):
        self.g.add((W.Organization, SKOS.prefLabel, Literal('Organisation', lang='en-gb')))
        self.assertIn('at most one preferred label', self.errors())

    def test_same_literal_cannot_be_preferred_and_alternative(self):
        label = self.g.value(W.Organization, SKOS.prefLabel)
        self.g.add((W.Organization, SKOS.altLabel, label))
        self.assertIn('both preferred and alternative', self.errors())

    def test_alternative_label_needs_language(self):
        self.g.add((W.Organization, SKOS.altLabel, Literal('Organisation')))
        self.assertIn('language-tagged', self.errors())

    def test_multiple_languages_and_synonyms_are_allowed(self):
        self.g.add((W.Organization, SKOS.prefLabel, Literal('Organisatie', lang='nl')))
        self.g.add((W.Organization, SKOS.altLabel, Literal('Organisation', lang='en-GB')))
        self.assertEqual('', self.errors())

    def test_missing_or_blank_required_definition_is_rejected(self):
        self.g.remove((W.Organization, W.taxonomicDefinition, None))
        self.assertIn('definition is required', self.errors())
        self.g.add((W.Organization, W.taxonomicDefinition, Literal('  ')))
        self.assertIn('non-empty definition text', self.errors())

    def test_optional_definitions_are_not_required_but_cannot_be_empty(self):
        self.g.add((W.Organization, W.businessDefinition, Literal('')))
        self.assertIn('non-empty definition text', self.errors())

    def test_legal_source_on_exact_assertion_passes(self):
        self.legal()
        self.assertEqual('', self.errors())

    def test_source_on_entity_does_not_satisfy_definition_requirement(self):
        ax, _ = self.legal()
        self.g.remove((ax, DCTERMS.source, None))
        self.g.add((W.Organization, DCTERMS.source, URIRef('https://example.org/law')))
        self.assertIn('lacks a source', self.errors())

    def test_one_source_does_not_cover_a_second_definition(self):
        self.legal()
        self.g.add((W.Organization, W.legalDefinition, Literal('Another definition.', lang='en-GB')))
        self.assertIn('lacks a source', self.errors())

    def test_language_mismatch_and_stale_source_are_rejected(self):
        ax, definition = self.legal()
        self.g.set((ax, OWL.annotatedTarget, Literal(str(definition), lang='nl')))
        self.assertIn('missing or changed legal definition', self.errors())
        self.assertIn('lacks a source', self.errors())

    def test_textual_citation_is_allowed_with_review_warning(self):
        ax, _ = self.legal()
        self.g.set((ax, DCTERMS.source, Literal('Example Regulation, Article 1')))
        errors, warnings = check_graph(self.g)
        self.assertFalse(errors)
        self.assertTrue(any('prefer an official article URI' in w for w in warnings))

    def test_empty_or_anonymous_source_is_rejected(self):
        ax, _ = self.legal()
        for source in (Literal(''), BNode()):
            with self.subTest(source=source):
                self.g.set((ax, DCTERMS.source, source))
                self.assertIn('lacks a source', self.errors())

    def test_iri_case_conventions(self):
        self.g.add((W.organization, RDF.type, OWL.Class))
        self.g.add((W.HasAddress, RDF.type, OWL.ObjectProperty))
        self.assertIn('UpperCamelCase', self.errors())
        self.assertIn('lowerCamelCase', self.errors())

    def test_reused_terms_do_not_require_our_editorial_annotations(self):
        self.g.add((URIRef('https://example.net/ExternalClass'), RDF.type, OWL.Class))
        self.assertEqual('', self.errors())

    def test_missing_ontology_or_annotation_declaration_fails(self):
        self.g.remove((ONTOLOGY, RDF.type, OWL.Ontology))
        self.g.remove((DCTERMS.source, RDF.type, OWL.AnnotationProperty))
        self.assertIn('ontology declaration', self.errors())
        self.assertIn('annotation property declaration', self.errors())

    def test_active_files_only_and_blank_nodes_are_separate(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'Archive').mkdir()
            (root / 'modelling_considerations').mkdir()
            (root / 'Archive/old.ttl').write_text('not Turtle')
            (root / 'modelling_considerations/old.ttl').write_text('not Turtle')
            fragment = '_:same <https://example.org/p> "value" .'
            (root / 'webuild.ttl').write_text(fragment)
            (root / 'module.ttl').write_text(fragment)
            graph, files = load_model(root)
            self.assertEqual(2, len(files))
            self.assertEqual(2, len(graph))

    def test_missing_or_invalid_active_file_fails(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(ValueError):
                load_model(root)
            (root / 'webuild.ttl').write_text('not Turtle')
            with self.assertRaises(Exception):
                load_model(root)


if __name__ == '__main__':
    unittest.main()
