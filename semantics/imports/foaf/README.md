# FOAF Agent class module

On 26 November 2026 Bart approved four FOAF classes for comparison with WEBUILD Agent. The module preserves the published IRIs, labels, comments, available `rdfs:isDefinedBy` annotations and these four logical axioms:

| Class | Relation | Class |
| --- | --- | --- |
| `foaf:Person` | subclass of | `foaf:Agent` |
| `foaf:Group` | subclass of | `foaf:Agent` |
| `foaf:Organization` | subclass of | `foaf:Agent` |
| `foaf:Agent` | equivalent to | `dcterms:Agent` |

The [module](foaf-classes-2026-11-26.ttl) imports the pinned Dublin Core class module for the definition of `dcterms:Agent`. Other FOAF axioms, including property definitions, disjointness and alignments to external Person classes, are outside this selection. The [central ontology](../../model/webuild.ttl) places WEBUILD Agent under FOAF Agent. Its relationship to PROV Agent remains open.

## Conditions of reuse

Approval applies to the pinned four-class projection above. Any expansion requires review of the additional axioms and their dependencies, followed by OWL 2 DL and HermiT checks on the resulting import closure.

Two dependencies in the full FOAF source remain only partially checked. FOAF equates `foaf:Person` with Schema.org's `http://schema.org/Person` and uses `skos:Concept` as the domain of `foaf:focus`. The full-import experiment identified missing declarations. Both axioms fall outside the approved module, and the HermiT result for this module does not establish compatibility with the Schema.org or SKOS ontologies.

## Source and verification

Dan Brickley and Libby Miller published FOAF 0.99 on 14 January 2014. The [unaltered RDF/XML snapshot](foaf-20140114.original.rdf) is byte-identical in two independent archives. Direct byte comparison with the publisher's distribution was unavailable. [FOAF specification and licence](https://xmlns.com/foaf/spec/) · [Dated distribution](https://xmlns.com/foaf/spec/20140114.rdf) · [FAIR-IMPACT archive](https://github.com/FAIR-IMPACT/MOD/blob/30c5411179e8b9caf8bb22ffdc7b96600fce71c7/resources/FOAF_20140114.rdf) · [Common Workflow Language archive](https://github.com/common-workflow-language/common-workflow-language/blob/98e95c4f90c8fc7eaf0e3ab6a423782ab6b6707c/v1.0/v1.0/foaf.rdf).

The [projection script](../../quality/foaf_classes.py) declares the four source classes as OWL classes. The dependency check verifies the source and module checksums in the [manifest](../manifest.json) and reproduces the projection from the snapshot. The HermiT controls verify both directions of Agent equivalence and the inferred types of each subclass.

In the full-import experiment, six datatype properties also carried inverse-functional declarations, which OWL 2 DL permits only for object properties. OWLAPI also reported incompatible uses of `foaf:name` as a datatype and annotation property, and missing class declarations for external terms including `schema:Person` and `skos:Concept`. The profile check stopped before HermiT could assess consistency.
