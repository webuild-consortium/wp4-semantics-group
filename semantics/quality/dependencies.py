"""Resolve complete import closures from pinned local files, without network IO."""

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

from rdflib import Graph, URIRef
from rdflib.compare import isomorphic
from rdflib.namespace import OWL, RDF

from dcterms_classes import class_module

CATALOG_NS = "{urn:oasis:names:tc:entity:xmlns:xml:catalog}"


@dataclass
class Dependency:
    iri: URIRef
    path: Path
    graph: Graph


def local_path(base, value, allowed):
    if urlparse(value).scheme or Path(value).is_absolute():
        raise ValueError(f"Dependency path must be relative: {value}")
    path = (base / value).resolve()
    if not path.is_relative_to(allowed.resolve()):
        raise ValueError(f"Dependency path leaves the imports directory: {value}")
    return path


def verify_hash(path, expected):
    if sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError(f"Dependency checksum mismatch: {path.name}")


def load_dependencies(authored, model_directory):
    """Validate every direct/transitive import and return its local document.

    Authored axioms stay separate so imported editorial conventions and global
    domains/ranges are not incorrectly treated as new WEBUILD authoring errors.
    Missing mappings, altered files, wrong identities and undeclared imports fail.
    """
    pending = list(authored.objects(None, OWL.imports))
    if not pending:
        return []
    directory = Path(model_directory).resolve()
    imports = directory.parent / "imports"
    manifest = json.loads((imports / "manifest.json").read_text())
    if manifest.get("format_version") != 1:
        raise ValueError("Unsupported dependency manifest format")
    records = {}
    for record in manifest["imports"]:
        iri = record["iri"]
        if iri in records:
            raise ValueError(f"Duplicate dependency manifest IRI: {iri}")
        records[iri] = record

    catalog = ET.parse(directory / "catalog-v001.xml")
    mappings = {}
    for entry in catalog.findall(f".//{CATALOG_NS}uri"):
        iri = entry.attrib["name"]
        if iri in mappings:
            raise ValueError(f"Duplicate catalogue mapping: {iri}")
        mappings[iri] = local_path(directory, entry.attrib["uri"], imports)

    seen = set(authored.subjects(RDF.type, OWL.Ontology))
    seen.update(v for s in tuple(seen) for v in authored.objects(s, OWL.versionIRI))
    result, cache = [], {}
    while pending:
        iri = pending.pop()
        if not isinstance(iri, URIRef):
            raise ValueError("Import targets must be IRIs")
        if iri in seen:
            continue
        key = str(iri)
        if key not in records or key not in mappings:
            raise ValueError(f"Unmapped or unpinned import: {iri}")
        record = records[key]
        path = local_path(imports, record["file"], imports)
        if mappings[key] != path:
            raise ValueError(f"Catalogue and manifest disagree: {iri}")
        verify_hash(path, record["sha256"])
        if path not in cache:
            cache[path] = Graph().parse(path, format="turtle")
        graph = cache[path]
        identities = set(graph.subjects(RDF.type, OWL.Ontology))
        versions = {v for s in identities for v in graph.objects(s, OWL.versionIRI)}
        if iri not in identities | versions:
            raise ValueError(f"Imported document does not declare requested ontology/version: {iri}")
        if ("published_version_iri" in record
                and URIRef(record["published_version_iri"]) not in versions):
            raise ValueError(f"Pinned published version is absent from the source: {iri}")

        # Verify the approved correction against the untouched original, not
        # merely against a checksum that might be updated with a broader edit.
        if "remove_annotation_property_declarations" in record:
            original = local_path(imports, record["upstream_file"], imports)
            verify_hash(original, record["upstream_sha256"])
            expected = Graph().parse(original, format="turtle")
            for name in record["remove_annotation_property_declarations"]:
                prop = URIRef(name)
                if ((prop, RDF.type, OWL.AnnotationProperty) not in expected
                        or (prop, RDF.type, OWL.ObjectProperty) not in expected):
                    raise ValueError(f"Expected duplicate property declaration missing: {prop}")
                expected.remove((prop, RDF.type, OWL.AnnotationProperty))
            if not isomorphic(expected, graph):
                raise ValueError(f"Dependency differs beyond its approved correction: {iri}")

        if "projection" in record:
            if record["projection"] != "dcterms-classes-v1":
                raise ValueError(f"Unknown dependency projection: {record['projection']}")
            original = local_path(imports, record["upstream_file"], imports)
            verify_hash(original, record["upstream_sha256"])
            source = Graph().parse(original, format="turtle")
            if not isomorphic(class_module(source), graph):
                raise ValueError(f"Dependency differs beyond its approved class projection: {iri}")

        seen.add(iri)
        result.append(Dependency(iri, path, graph))
        pending.extend(graph.objects(None, OWL.imports))
    return sorted(result, key=lambda item: str(item.iri))
