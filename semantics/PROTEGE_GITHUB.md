# Working together with Protégé and GitHub

This guide describes the technical setup for collaborative ontology development in `webuild-consortium/wp4-semantics-group`. Protégé edits local files; Git records versions, and GitHub supports sharing and review. The workflow below is a proposal for the team and does not establish substantive modelling rules. English is the working language for new documentation and other files prepared for GitHub.

## Starting file

Open `semantics/model/webuild.ttl`. This is an empty ontology with no classes, properties, imports, or substantive modelling rules. This is a draft model intended for joint development. Its temporary ontology IRI is `https://example.org/webuild/ontology`, and its temporary term namespace is `https://example.org/webuild/ontology#`. These development placeholders are applied in the file; they are not published project identifiers. The definitive namespace and its governance remain to be agreed before external use.

The three earlier Turtle models have been preserved unchanged in `semantics/model/Archive`, as requested. The new ontology does not import them. `authorisation_part.PlantUML` is also in `Archive`. The `modelling_considerations` directory has been retained and relates to earlier modelling work.

## Confirmed starting decisions

- Working language: English for new documentation and other files prepared for GitHub.
- Status: draft model intended for joint development, not an approved project release.
- Modelling approach: OWL, using EBUCorePlus as the reference approach. Specific modelling conventions will be agreed individually; this does not imply importing EBUCorePlus domain concepts.
- Property applicability: describe the use of both object and datatype properties in the relevant classes through OWL restrictions, without global `rdfs:domain` statements on those properties.
- Object properties: use class-level OWL restrictions consistently. Do not assert global `rdfs:domain` or `rdfs:range` for object properties in the jointly developed ontology.
- Datatype properties: a global `rdfs:range` is permitted, for example `xsd:date`. This is permission, not a requirement to declare a global range on every datatype property. Do not assert global `rdfs:domain`; describe class-specific use through restrictions on the relevant classes.
- Temporary term namespace: `https://example.org/webuild/ontology#`. For example, a term named `Organisation` would have the IRI `https://example.org/webuild/ontology#Organisation`; this example does not introduce a class.
- Temporary ontology IRI: `https://example.org/webuild/ontology`. This identifies the draft ontology as a whole.
- Substantive change approval: Bart and his modelling colleague must both approve a change before it is considered agreed. Until both have approved it, the change remains a proposal.
- Definitive ontology IRI, term namespace, namespace stewardship, and release publication process: pending joint agreement before external use.

This decision supersedes the earlier choice of `https://w3id.org/ebwv` and `https://w3id.org/ebwv#` for this draft. The existing implementation vocabulary uses the EBWV term namespace; keeping a separate development namespace avoids assigning competing definitions to the same term IRIs while the relationship between the models and their governance is unresolved.

The existing implementation vocabulary and publication files remain unchanged. They can inform the joint modelling work, but reuse and any mappings require review of each term's meaning. This draft does not assert replacement of, or equivalence with, that vocabulary. Substantive model changes require joint approval by Bart and his modelling colleague. Their joint approval establishes acceptance of the change; the process for publishing releases remains to be agreed. This documentation does not configure or enforce GitHub branch protection.

Confirm further starting decisions one at a time before implementing them.

## Modelling reference

The agreed reference is [EBUCorePlus](http://www.ebu.ch/metadata/ontologies/ebucoreplus). Its official documentation redirects to the [EBUCorePlus documentation site](https://ebu.github.io/ebucoreplus/). The source inspected for this decision is [`ontology/EBUCorePlus/ebucoreplus.owl` at commit `880d36abfd59b6c08a4794e9a5d4b93b0afda200`](https://github.com/ebu/ebucoreplus/blob/880d36abfd59b6c08a4794e9a5d4b93b0afda200/ontology/EBUCorePlus/ebucoreplus.owl). It declares version 2.0.0 and uses Turtle syntax despite its `.owl` extension. WEBUILD retains the agreed `.ttl` extension.

Verified features of that source include `owl:Class`, `owl:ObjectProperty`, `owl:DatatypeProperty`, and class-level `owl:Restriction` expressions, including value restrictions and qualified cardinalities. No `rdfs:domain` statements occur in the inspected graph. Global `rdfs:range` statements do occur: for 222 datatype properties, one annotation property, and the object property `ec:isAbout`, whose range is `ec:Asset`. Therefore, the reference must not be described as universally avoiding global ranges. These observations concern the inspected source graph, not its imported ontologies.

The confirmed direction is OWL modelling following this reference approach. WEBUILD applies the object property rule below consistently, including where the EBUCorePlus reference has an exception. Permitted restriction patterns, annotations, and validation remain to be agreed one decision at a time. No OWL profile or reasoner has yet been selected. The reference ontology has not been imported into the WEBUILD ontology, and no domain terms have been added.

## Object property modelling rule

For object properties, express class-specific conditions through OWL restrictions on the relevant classes. Do not attach global `rdfs:domain` or `rdfs:range` statements to those properties. In Protégé, record the restrictions in the relevant class descriptions and leave the object property's global Domains and Ranges empty.

This decision establishes where conditions are expressed. It does not prescribe a universal restriction or cardinality for every relation. Decide the appropriate restriction for each intended meaning; do not add existence or cardinality requirements merely because an object property is used by a class. Datatype properties follow the same class-level approach to applicability, while their ranges follow the separate rule below.

This rule governs the new jointly developed model. Archived originals and the existing implementation vocabulary remain unchanged.

## Datatype property modelling rule

A datatype property may have a global `rdfs:range`, such as `xsd:date`. Declaring a global range is optional and must reflect the intended meaning of the property across its uses. Describe the use of a datatype property in the relevant class through OWL restrictions; do not declare a global `rdfs:domain` on the property. In Protégé, leave the datatype property's global Domains empty. This is a class-level modelling convention, not an instruction to attach `rdfs:domain` statements to classes or a claim that class restrictions are semantically equivalent to global domain axioms. No datatype properties or range axioms have been added to the empty draft ontology by recording this decision.

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

The temporary identifiers, draft status, and joint approval of substantive changes are confirmed above. The definitive identifiers, namespace stewardship, and release publication process remain pending. Agree next on term IRI allocation, naming conventions, module boundaries, and source references to use cases. Use English for new GitHub documentation and other newly authored content; preserve existing source material and archived originals. Within the agreed OWL approach, agree on the constructs that Protégé must preserve: a syntactically valid Turtle file cannot necessarily be saved through an OWL editor without changes. Check existing sources using a copy and a comparison of the RDF triples.

A Git merge without textual conflicts can still combine contradictory modelling choices. Always review meaning and relevant use case examples. Consider protecting `main` with mandatory review once the team has agreed on this workflow.

The selected working directory is under OneDrive. The recommendation is to eventually place the active Git working directory outside a synchronised folder and collaborate through GitHub; two independent synchronisation mechanisms make the working directory harder to manage. Until then, keep the files fully available locally and use this checkout on one computer at a time. The directory was not relocated during setup.

The existing GitHub repository is public. A push publishes changes; saving locally or making a local commit does not.

In this local checkout, executable bits changed on many files without content changes. Therefore, `core.filemode=false` is set for this checkout only, so those differences do not clutter the review. This is a local Git setting and is not shared with the repository.

## Sources

- [Protégé menus and save functions](https://protegeproject.github.io/protege/menus/)
- [GitHub documentation on merge conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts)
- [Publication process in this repository](../vocab/README.md)
