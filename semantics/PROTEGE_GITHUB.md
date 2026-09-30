# Working together with Protégé and GitHub

This guide describes the technical setup for collaborative ontology development in `webuild-consortium/wp4-semantics-group`. Protégé edits local files; Git records versions, and GitHub supports sharing and review. The workflow below is a proposal for the team and does not establish substantive modelling rules. English is the working language for new documentation and other files prepared for GitHub.

## Starting file

Open `semantics/model/webuild.ttl`. The ontology contains its ontology declaration and the two reused label annotation properties, `skos:prefLabel` and `skos:altLabel`, and the three local definition annotation properties, `taxonomicDefinition`, `legalDefinition`, and `businessDefinition`. The local definition properties have British English preferred labels and definitions. The reused annotation property `dcterms:source` records the source of a specific legal definition. No domain classes, object properties, datatype properties, or imports have been added. This is a draft model intended for joint development. Its temporary ontology IRI is `https://example.org/webuild/ontology`, and its temporary term namespace is `https://example.org/webuild/ontology#`. These development placeholders are applied in the file; they are not published project identifiers. The definitive namespace and its governance remain to be agreed before external use.

The three earlier Turtle models have been preserved unchanged in `semantics/model/Archive`, as requested. The new ontology does not import them. `authorisation_part.PlantUML` is also in `Archive`. The `modelling_considerations` directory has been retained and relates to earlier modelling work.

## Confirmed starting decisions

- Working language: English for new documentation and other files prepared for GitHub.
- Term IRIs: use readable American English terms, for example `Organization`.
- IRI capitalisation: use `UpperCamelCase` for class names, such as `RegisteredOrganization`, and `lowerCamelCase` for property names, such as `hasRegisteredAddress`.
- English labels: use British English spelling and the language tag `en-GB`, for example `"Organisation"@en-GB`.
- Label annotations: use `skos:prefLabel` for the preferred display label and `skos:altLabel` for synonyms or alternative names. These annotations apply directly to OWL entities without typing them as `skos:Concept`.
- Definition types: a mandatory taxonomic definition, an optional legal definition quoted verbatim from legislation or regulations, and an optional business definition in everyday language. For a property without a meaningful superproperty, a mandatory base definition fulfils the first requirement. Keep the three definition types distinct.
- Status: draft model intended for joint development, not an approved project release.
- Modelling approach: OWL, using EBUCorePlus as the reference approach. Specific modelling conventions will be agreed individually; this does not imply importing EBUCorePlus domain concepts.
- Property applicability: describe the use of both object and datatype properties in the relevant classes through OWL restrictions, without global `rdfs:domain` statements on those properties.
- Object properties: use class-level OWL restrictions consistently. Do not assert global `rdfs:domain` or `rdfs:range` for object properties in the jointly developed ontology.
- Datatype properties: a global `rdfs:range` is permitted, for example `xsd:date`. This is permission, not a requirement to declare a global range on every datatype property. Do not assert global `rdfs:domain`; describe class-specific use through restrictions on the relevant classes.
- Temporary term namespace: `https://example.org/webuild/ontology#`. For example, a term named `Organization` would have the IRI `https://example.org/webuild/ontology#Organization`; this example does not introduce a class.
- Temporary ontology IRI: `https://example.org/webuild/ontology`. This identifies the draft ontology as a whole.
- Substantive change approval: Bart and his modelling colleague must both approve a change before it is considered agreed. Until both have approved it, the change remains a proposal.
- Definitive ontology IRI, term namespace, namespace stewardship, and release publication process: pending joint agreement before external use.

This decision supersedes the earlier choice of `https://w3id.org/ebwv` and `https://w3id.org/ebwv#` for this draft. The existing implementation vocabulary uses the EBWV term namespace; keeping a separate development namespace avoids assigning competing definitions to the same term IRIs while the relationship between the models and their governance is unresolved.

The existing implementation vocabulary and publication files remain unchanged. They can inform the joint modelling work, but reuse and any mappings require review of each term's meaning. This draft does not assert replacement of, or equivalence with, that vocabulary. Substantive model changes require joint approval by Bart and his modelling colleague. Their joint approval establishes acceptance of the change; the process for publishing releases remains to be agreed. This documentation does not configure or enforce GitHub branch protection.

Confirm further starting decisions one at a time before implementing them.

## Modelling reference

The agreed reference is [EBUCorePlus](http://www.ebu.ch/metadata/ontologies/ebucoreplus). Its official documentation redirects to the [EBUCorePlus documentation site](https://ebu.github.io/ebucoreplus/). The source inspected for this decision is [`ontology/EBUCorePlus/ebucoreplus.owl` at commit `880d36abfd59b6c08a4794e9a5d4b93b0afda200`](https://github.com/ebu/ebucoreplus/blob/880d36abfd59b6c08a4794e9a5d4b93b0afda200/ontology/EBUCorePlus/ebucoreplus.owl). It declares version 2.0.0 and uses Turtle syntax despite its `.owl` extension. WEBUILD retains the agreed `.ttl` extension.

Verified features of that source include `owl:Class`, `owl:ObjectProperty`, `owl:DatatypeProperty`, and class-level `owl:Restriction` expressions, including value restrictions and qualified cardinalities. No `rdfs:domain` statements occur in the inspected graph. Global `rdfs:range` statements do occur: for 222 datatype properties, one annotation property, and the object property `ec:isAbout`, whose range is `ec:Asset`. Therefore, the reference must not be described as universally avoiding global ranges. These observations concern the inspected source graph, not its imported ontologies.

The confirmed direction is OWL modelling following this reference approach. WEBUILD applies the object property rule below consistently, including where the EBUCorePlus reference has an exception. The annotation properties for the three definition types are agreed below. Permitted restriction patterns, other annotations, and validation remain to be agreed one decision at a time. No OWL profile or reasoner has yet been selected. The reference ontology has not been imported into the WEBUILD ontology, and no domain terms have been added.

## Object property modelling rule

For object properties, express class-specific conditions through OWL restrictions on the relevant classes. Do not attach global `rdfs:domain` or `rdfs:range` statements to those properties. In Protégé, record the restrictions in the relevant class descriptions and leave the object property's global Domains and Ranges empty.

This decision establishes where conditions are expressed. It does not prescribe a universal restriction or cardinality for every relation. Decide the appropriate restriction for each intended meaning; do not add existence or cardinality requirements merely because an object property is used by a class. Datatype properties follow the same class-level approach to applicability, while their ranges follow the separate rule below.

This rule governs the new jointly developed model. Archived originals and the existing implementation vocabulary remain unchanged.

## Datatype property modelling rule

A datatype property may have a global `rdfs:range`, such as `xsd:date`. Declaring a global range is optional and must reflect the intended meaning of the property across its uses. Describe the use of a datatype property in the relevant class through OWL restrictions; do not declare a global `rdfs:domain` on the property. In Protégé, leave the datatype property's global Domains empty. This is a class-level modelling convention, not an instruction to attach `rdfs:domain` statements to classes or a claim that class restrictions are semantically equivalent to global domain axioms. No datatype properties or range axioms have been added to the draft ontology by recording this decision.

## Term names and label language

Use readable American English terms for the local names in term IRIs. Use British English for English labels, with the RDF language tag `en-GB`. For example, the IRI `https://example.org/webuild/ontology#Organization` would have the English label `"Organisation"@en-GB`. The IRI spelling and the label spelling deliberately differ.

These conventions apply to newly authored WEBUILD terms and labels. Preserve identifiers and original annotations in imported sources and archived material. Use `UpperCamelCase` for class local names and `lowerCamelCase` for property local names. For example, use `RegisteredOrganization` and `hasRegisteredAddress`. These are IRI naming conventions; they do not require CamelCase in human-readable labels. Use `skos:prefLabel` and `skos:altLabel` as specified below. The example illustrates naming only; it does not add an Organization class to the ontology or determine the spelling convention for all prose documentation.

## Preferred labels and synonyms

For each newly authored WEBUILD class or property, provide exactly one British English preferred label using `skos:prefLabel` with `en-GB`. Use zero or more `skos:altLabel` annotations for synonyms and alternative names of the same meaning, each with a language tag. Related but distinct meanings require separate terms rather than alternative labels.

For each term, allow at most one preferred label per language tag. Do not use the same literal, including its language tag, as both preferred and alternative label on that term. These are editorial rules to be checked during review; automated enforcement has not yet been configured.

Both properties are OWL annotation properties and can annotate OWL classes and properties directly. Their use does not require or imply `rdf:type skos:Concept`. The ontology declares these two reused annotation properties under their original SKOS IRIs; it does not import the complete SKOS ontology or add SKOS concept classifications. Separate duplicate `rdfs:label` annotations are not required by this convention.

Protégé is configured on this workstation to display `skos:prefLabel`, with the language preference field set to `en-GB, en, !` so British English has first priority. Both the Annotation Renderer and Preferences dialogs were confirmed. The ontology has no domain entities with labels yet, so display of actual domain labels has not been exercised.

To reproduce the setting, open **View → Custom rendering…**, select **Render by annotation property**, and click **Configure…**. Use `http://www.w3.org/2004/02/skos/core#prefLabel` as the annotation IRI, enter `en-GB, en, !` in **Set Language**, and confirm both dialogs with **OK**. Do not select `skos:altLabel` as the display property.

Rendering preferences are local application settings and are not distributed by the Turtle file; each modeller needs to configure them. These preferences affect the local Protégé display, not the ontology's term IRIs or stored label values.

Reference: [W3C SKOS lexical labels, including their domain and integrity conditions](https://www.w3.org/TR/skos-reference/#labels).

## Definition types

Keep three distinct types of definition rather than one undifferentiated definition field:

| Definition type | Requirement | Content |
| --- | --- | --- |
| Taxonomic definition | Mandatory | For a class, name its superclass and the distinguishing characteristics. For a property, name its meaningful superproperty and the distinguishing characteristics; if none exists, provide a base definition of the relation. |
| Legal definition | Optional | A definition quoted verbatim from the relevant legislative or regulatory text when the term is used in law or regulation. |
| Business definition | Optional | A definition in everyday language. |

For example, if `CentrifugalPump` is a subclass of `Pump`, the taxonomic definition is: “A centrifugal pump is a pump with a rotating impeller.” This illustrates the definition pattern only; neither class has been added to the WEBUILD ontology.

The optional legal and business definitions do not replace the mandatory taxonomic definition or, for a property without a meaningful superproperty, its mandatory base definition. Use the three local OWL annotation properties listed below. They have been added to the ontology under the temporary term namespace `https://example.org/webuild/ontology#`. The proposal to use a single `skos:definition` field has not been adopted.

| Annotation property | Use |
| --- | --- |
| `:taxonomicDefinition` | Mandatory taxonomic definition; also holds the mandatory base definition for a property without a meaningful superproperty. |
| `:legalDefinition` | Optional verbatim legal definition; a source reference is mandatory whenever a legal definition is provided, preferably as a URI. |
| `:businessDefinition` | Optional definition in everyday language. |

In Protégé, add these annotations to the class or property being defined. The mandatory definition is an editorial requirement; declaring an annotation property does not enforce its presence. Automated validation has not yet been configured. No extra definition type or formal hierarchy is introduced by these declarations.

For both object and datatype properties, apply the following agreed rule:

- If a meaningful superproperty exists, the taxonomic definition names it and explains the distinguishing characteristic. Every relation asserted using the subproperty must also be a valid relation of the superproperty.
- If no meaningful superproperty exists, provide a mandatory base definition stating the relation, its direction, and the meaning of the related entities or value. Do not introduce an artificial superproperty solely to satisfy the definition format. The base definition is the fallback for the required definition, not an additional optional definition type.

For example, if `hasRegisteredAddress` is a subproperty of `hasAddress`, a definition can state: “Has registered address is a has-address relation in which the address is officially registered for the entity.” For a datatype property without a meaningful superproperty, a base definition can state: “Birth date is a relation between an entity and the date on which it was born.” These are illustrative examples only; no corresponding properties or hierarchy axioms have been added.

Record the definition as an annotation and the formal property hierarchy separately using `rdfs:subPropertyOf`. Definition text alone does not establish the formal hierarchy. Sharing a datatype alone does not justify a subproperty relationship. The existing rules for class-level applicability and global ranges remain unchanged.

Every legal definition must have a source reference identifying the relevant legislation or regulation and the specific article. Prefer a URI pointing to the official source and, where available, the specific article. The source reference is mandatory; use of a URI is a preference, not an absolute requirement when no suitable URI is available.

Use `dcterms:source` (`http://purl.org/dc/terms/source`) as an OWL annotation property on the specific `:legalDefinition` annotation assertion. This associates the source with that definition text. A source annotation on the class or property alone does not establish which definition it supports. The ontology declares `dcterms:source` without importing the Dublin Core vocabulary.

In Protégé, add the legal definition to the entity, then annotate that definition assertion with `dcterms:source`. Enter the source as an IRI value when a suitable URI is available, rather than a text literal containing a URL. If several legal definitions exist for one term, attach the appropriate source to each definition separately. The source requirement remains an editorial rule until automated validation is configured.

The following Turtle illustrates the agreed pattern using placeholders only. It is documentation, not a legal assertion or an addition of domain terms to `webuild.ttl`:

```turtle
@prefix : <https://example.org/webuild/ontology#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .

:legalDefinition a owl:AnnotationProperty .
dcterms:source a owl:AnnotationProperty .
:ExampleTerm a owl:Class ;
    :legalDefinition "Placeholder legal definition."@en-GB .

[] a owl:Axiom ;
    owl:annotatedSource :ExampleTerm ;
    owl:annotatedProperty :legalDefinition ;
    owl:annotatedTarget "Placeholder legal definition."@en-GB ;
    dcterms:source <https://example.org/legislation/example/article/1> .
```

The `owl:annotatedTarget` must match the definition literal exactly, including its language tag or datatype. When editing a definition, preserve or update its source annotation on the resulting assertion. This pattern uses the standard OWL axiom annotation representation; it does not introduce an intermediate domain class for definitions.

References: [Dublin Core source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/source/) and [W3C OWL axiom annotations in RDF](https://www.w3.org/TR/owl2-mapping-to-rdf/#Axioms_that_Generate_a_Main_Triple).

Legal definitions must be literal quotations from the cited source. Preserve the source wording, including its spelling; do not paraphrase or silently rewrite the text to match the label spelling convention. Explanations in everyday language belong in `:businessDefinition` and must not be presented as quotations from legislation. Each legal quotation retains its own required source reference as described above.

The handling of classes without a meaningful named superclass is not yet determined by the property-specific decision above.

Reference: [W3C OWL 2 object subproperties](https://www.w3.org/TR/owl2-syntax/#Object_Subproperties) and [data subproperties](https://www.w3.org/TR/owl2-syntax/#Data_Subproperties).

## Files and storage

Use Turtle with the `.ttl` extension for manually edited ontologies in `semantics/model`. When saving a new file in Protégé, explicitly select **Turtle Syntax** through **File → Save as…**. Changing the extension alone does not change the storage format. Then use **File → Save** for subsequent saves to the same file.

Agree on the same Protégé version and save settings. Turtle makes textual differences readable, but an editor may reorder and reformat content when saving. Therefore, also check a save cycle without substantive changes. Keep meaningful explanations as annotations, such as `rdfs:comment`, or in documentation: standalone Turtle comments are not RDF triples and may disappear when the file is saved again.

According to `vocab/README.md`, `docs/ebwv` contains generated publication files. Do not use these as manually edited Protégé sources; the source files and generator are under `vocab`. The team still needs to define the relationship between that publication process and the ontology under `semantics/model`.

## A working session

1. Save your work in Protégé and close the relevant ontology window before Git replaces files.
2. Review your local changes. Commit completed work before switching branches.
3. Update `main` to the latest version and create a short-lived working branch, such as `bart/topic`. The local setup branch is called `bart/protege-setup`.
4. Open the local `.ttl` file from that working directory in Protégé. Work on one clearly scoped change.
5. Save, review the diff, and check for unexpected deletions, IRI changes, or import changes.
6. Check the Turtle syntax. Also use the agreed reasoner or SHACL validation where appropriate for the model. Passing a syntax check does not establish semantic correctness.
7. Commit the intended files, push the working branch, and create a pull request. Record approval by both Bart and his modelling colleague before treating a substantive change as agreed and merging it into `main`. The author's explicit agreement and the other modeller's review can record their respective approvals.
8. Reopen the file after a pull, merge, or branch switch. Otherwise, an open Protégé window may write an outdated in-memory copy back to disk.

Branches isolate changes, but do not prevent merge conflicts when both contributors change the same lines. When sharing one file, agree on who edits which part, keep branches short-lived, and coordinate overlapping work. Separate files can help if they follow meaningful module boundaries. Record each module's ontology IRI, filename, responsibility for changes, and imports; avoid duplicate definitions across files.

## Local imports

An ontology IRI identifies the ontology; the path to the `.ttl` file specifies its storage location. Do not make that identity depend on someone's local user directory.

Protégé can resolve local imports through a `catalog-v001.xml` file. Share such a catalogue only with reviewed, relative file paths. Do not automatically ignore catalogues: they may be needed to open the model correctly on another computer. Do not silently redirect a missing import to an ontology with a different IRI.

The following was observed in the archived models on 30 September 2026:

- `Archive/PRIMER.ttl` declares `http://data.webuildconsortium.eu/PRIMER`.
- `Archive/authorisation_part.ttl` imports `http://www.braindex.nl/data/PRIMER` and uses both the Braindex namespace and `http://data.webuildconsortium.eu/primer#`, with lowercase `primer`.
- `Archive/authorisation_part_instance.ttl` imports `http://data.webuildconsortium.eu/authorisation.ttl`, the ontology IRI of `authorisation_part.ttl`.

The different PRIMER IRIs do not automatically identify the same ontology. The team must determine the intended identity; these sources were not changed during the technical setup.

## Agreements before modelling

The temporary identifiers, draft status, and joint approval of substantive changes are confirmed above. The definitive identifiers, namespace stewardship, and release publication process remain pending. Readable American English term IRIs and British English labels are agreed above. IRI capitalisation is also agreed above. Preferred and alternative label properties are also agreed above. Agree next on module boundaries and source references to use cases. Use English for new GitHub documentation and other newly authored content; preserve existing source material and archived originals. Within the agreed OWL approach, agree on the constructs that Protégé must preserve: a syntactically valid Turtle file cannot necessarily be saved through an OWL editor without changes. Check existing sources using a copy and a comparison of the RDF triples.

A Git merge without textual conflicts can still combine contradictory modelling choices. Always review meaning and relevant use case examples. Consider protecting `main` with mandatory review once the team has agreed on this workflow.

The selected working directory is under OneDrive. The recommendation is to eventually place the active Git working directory outside a synchronised folder and collaborate through GitHub; two independent synchronisation mechanisms make the working directory harder to manage. Until then, keep the files fully available locally and use this checkout on one computer at a time. The directory was not relocated during setup.

The existing GitHub repository is public. A push publishes changes; saving locally or making a local commit does not.

In this local checkout, executable bits changed on many files without content changes. Therefore, `core.filemode=false` is set for this checkout only, so those differences do not clutter the review. This is a local Git setting and is not shared with the repository.

## Sources

- [Protégé menus and save functions](https://protegeproject.github.io/protege/menus/)
- [GitHub documentation on merge conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts)
- [Publication process in this repository](../vocab/README.md)
