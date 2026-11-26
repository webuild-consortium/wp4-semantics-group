# Dublin Core Terms class module

Bart approved this class-only reuse strategy on 23 November 2026 so that WEBUILD, PROV-O and the Dublin Core class hierarchy can be inspected from the single working file `semantics/model/webuild.ttl`. The dependency files are resolved automatically through the adjacent model catalogue. They are not additional working ontologies for the modeller to switch between.

This is a locally derived OWL module, not an official DCMI OWL distribution, a complete Dublin Core import or a claim of semantic equivalence with the full RDF schema. Approval by the other modeller remains required before merging the resulting central-model revision into `main`.

## Source and identity

| Item | Value |
| --- | --- |
| Upstream publisher | Dublin Core Metadata Initiative (DCMI) |
| Distribution list | https://www.dublincore.org/schemas/rdfs/ |
| Downloaded source | https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl |
| Retrieval date | 23 November 2026 |
| Unmodified snapshot | `dublin_core_terms.original.ttl` |
| Source graph | 700 triples; no `owl:Ontology` header or `owl:imports` |
| Source SHA-256 | `13df401072dd7015bf9d75162f3e41c8138075304b7b9cc1aa1e9c16db976797` |
| Local module ontology IRI | `https://w3id.org/ebwv/semantic-model/imports/dcterms-classes` |
| Imported version IRI | `https://w3id.org/ebwv/semantic-model/imports/dcterms-classes/2026-11-23` |
| Derived file | `dcterms-classes-2026-11-23.ttl` |
| Derived graph | 106 triples, including 22 class declarations and eight subclass axioms |

The URL was listed as the latest Turtle distribution when retrieved. The actual served file's namespace metadata records a 2012 modification date; do not identify this snapshot as the dated 2020 distribution solely from its download location. The source is attributed to DCMI; see the [DCMI document notice](https://www.dublincore.org/about/documents/) and the source distribution page for reuse terms. The exact source and module file checksums are pinned in `../manifest.json`.

## Exact projection

The extraction recipe is `semantics/quality/dcterms_classes.py`:

1. Select the 22 resources in the `http://purl.org/dc/terms/` namespace explicitly typed as `rdfs:Class` in the snapshot.
2. Declare each unchanged term IRI as `owl:Class` in the module.
3. Copy each class's `rdfs:label`, `rdfs:comment` (source definition), `rdfs:isDefinedBy`, and `dcterms:description` values exactly, including their language tags. No definition text is rewritten. The existing WEBUILD labels on locally reused classes are retained separately in `webuild.ttl`.
4. Preserve all eight `rdfs:subClassOf` edges whose subject and object are both selected classes. In particular, `dcterms:PeriodOfTime` remains a subclass of `dcterms:LocationPeriodOrJurisdiction`.
5. Add the module's own identity, version and explanatory provenance header, and declare `dcterms:source` and `dcterms:description` as annotation properties for the metadata used here. No source property hierarchy, domain or range is copied.

The following two source statements concern the RDF metamodel and are deliberately not represented as OWL domain-class axioms:

```turtle
dcterms:Agent rdf:type dcterms:AgentClass .
dcterms:AgentClass rdfs:subClassOf rdfs:Class .
```

Both named DCMI classes remain present. The module neither introduces an alternative superclass for AgentClass nor models Agent as an individual of AgentClass. Source property definitions, datatypes, encoding schemes and issuance metadata are excluded. No additional superclass, equivalence, disjointness or restriction axioms are invented. No alignment between `prov:Agent` and `dcterms:Agent` is asserted.

The unmodified full schema was tested with the central model and PROV-O before this projection was approved. The OWL 2 DL profile check failed, including annotation/data property typing conflicts and declaration/datatype findings. That result does not invalidate the source as RDF and does not establish logical inconsistency. The class module avoids importing the unrelated property and metamodel content, rather than weakening the central checks or silently repairing the official file.

## Reproduction and validation

### Class declarations and the class hierarchy

In the original schema, `dcterms:Agent rdf:type rdfs:Class` states that Agent is a class. It does not state `dcterms:Agent rdfs:subClassOf rdfs:Class`, which would classify every agent as a class. See the [RDF Schema distinction between class membership and subclass relations](https://www.w3.org/TR/rdf-schema/#ch_classes). The standard term is `rdfs:Class`, not `rdf:Class`.

This approved projection explicitly declares the selected terms as `owl:Class`; Protégé therefore shows their OWL hierarchy under `owl:Thing`. This is not a claim that the original DCMI schema explicitly contained these OWL declarations. No additional hierarchy edge to `rdfs:Class`, or from `owl:Thing` to `rdfs:Class`, is added for display purposes. Class typing and domain-class specialisation must remain distinct.

### Regeneration

From the repository root, regenerate only when reviewing a dependency change:

```sh
.local/quality-venv/bin/python -B semantics/quality/dcterms_classes.py
```

Turtle ordering can vary without changing the RDF graph. Review the result, update the manifest file checksum for the reviewed bytes if necessary, and run the complete quality suite. Do not replace the upstream snapshot or broaden the projection without an explicit source and modelling review.

The dependency loader verifies the source and module hashes and reconstructs the exact approved projection. Graph equality must hold even if a module checksum is updated. Regression tests check the source class set, copied text, exact class-to-class hierarchy, excluded metamodel/property content, and rejection of an extra superclass axiom. These checks supplement the OWL 2 DL and HermiT checks; they do not establish the meaning of a future WEBUILD-to-DCMI mapping.

Validation on 23 November 2026: the full suite passed all 42 regression tests, authored structural/editorial checks (43 triples), both pinned dependency checks, OWL 2 DL checks and HermiT consistency/named-class satisfiability across all three ontology documents. All six SHACL examples returned their expected results. The PROV-O source and its exact two-triple correction remain unchanged.

After the PROV import-identity fix and removal of redundant authored declarations on the same date, the suite passed all 44 tests with a 38-triple authored graph. Both controlled imports, HermiT and all six SHACL examples passed. The Dublin Core source and derived module are unchanged. The complete effective graph before and after declaration cleanup is isomorphic (1,287 triples); the local PeriodOfTime preferred label and source link remain in `webuild.ttl`.
