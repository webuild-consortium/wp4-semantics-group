# Controlled dependencies of the WEBUILD semantic model

Open `../model/webuild.ttl` as the single working ontology. Its adjacent `catalog-v001.xml` maps the imports below to local, relative file paths. `manifest.json` pins the exact bytes, upstream snapshots and approved derivations/corrections. Keep these dependency files with the model when sharing the branch; do not edit them as parallel working ontologies.

| Dependency | Active import IRI | Scope and record |
| --- | --- | --- |
| PROV-O core, published version 2013-04-30 | `http://www.w3.org/ns/prov#` | Complete pinned core, with exactly the two approved duplicate annotation-property declarations removed. `prov:wasRevisionOf` and `prov:specializationOf` remain object properties with their other original axioms. [Correction, ontology identity and validation](../PROTEGE_GITHUB.md#controlled-prov-o-import). |
| Dublin Core Terms class module | `https://w3id.org/ebwv/semantic-model/imports/dcterms-classes/2026-11-23` | Locally derived OWL module containing 22 unchanged class IRIs and eight mutual subclass relations, with source definition text. It is not the full DCMI schema. [Exact projection and exclusions](dcterms/README.md). |

The PROV import IRI is the ontology identity recognised in the observed Protégé session. The version-IRI import previously loaded the file without joining that session's active import closure; switching to the recognised identity corrected the display. The published version metadata and both file hashes remain verified. Neither the historical source headers nor additional PROV axioms were changed to obtain this fix.

Imports carry their axioms into reasoning; they do not automatically establish subclass or equivalence mappings between WEBUILD, Dublin Core and PROV terms. The authored extension's editorial conventions are checked separately from imported conventions. In particular, source PROV global domains/ranges remain effective. The complete dependency closure participates in OWL 2 DL and HermiT checks, while profile examples retain their separately documented SHACL settings.

The working file does not repeat the imported Agent/PeriodOfTime class declarations or the two PROV object-property declarations. It retains the WEBUILD-specific `skos:prefLabel "Period of time"@en-GB` and the term-specific source link on PeriodOfTime. An RDF comparison confirmed that removing the redundant declarations and copied definition left the complete graph unchanged.

The full upstream EBWV vocabulary is not imported: the pinned reuse baseline and its outstanding serialization issue are recorded in the [source ownership decision](../PROTEGE_GITHUB.md#source-ownership-and-ebwv-reuse). The passing dependency checks cover only the controlled sources listed above.

Current validation on 23 November 2026: all 44 regression tests passed, the authored graph contains 38 triples, the two pinned dependencies resolve locally, and the three ontology documents pass OWL 2 DL/HermiT checks with no inconsistency or unsatisfiable named classes. All six SHACL examples return their expected results. Validation is automated evidence, not a substitute for semantic review and both modellers' approval before merging into `main`.
