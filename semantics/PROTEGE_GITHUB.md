# Working together with Protégé and GitHub

This guide describes the technical setup for collaborative ontology development in `webuild-consortium/wp4-semantics-group`. Protégé edits local files; Git records versions, and GitHub supports sharing and review. The workflow below is a proposal for the team and does not establish substantive modelling rules. English is the working language for new documentation and other files prepared for GitHub.

## Starting file

Open `semantics/model/webuild.ttl` in Protégé. The joint draft declares `https://w3id.org/ebwv` as its ontology IRI and uses `https://w3id.org/ebwv#` for its own terms. The draft contains three local definition annotation properties with British English labels and definitions. It uses the standard annotation properties `skos:prefLabel`, `skos:altLabel`, and `dcterms:source` under their original IRIs.

The three earlier Turtle models have been preserved unchanged in `semantics/model/Archive`, as requested. The new ontology does not import them. `authorisation_part.PlantUML` is also in `Archive`. The `modelling_considerations` directory has been retained and relates to earlier modelling work.

## Confirmed starting decisions

- Working language: English for new documentation and other files prepared for GitHub.
- Term IRIs: use readable American English terms, for example `Organization`.
- IRI capitalisation: use `UpperCamelCase` for class names, such as `RegisteredOrganization`, and `lowerCamelCase` for property names, such as `hasRegisteredAddress`.
- English labels: use British English spelling and the language tag `en-GB`, for example `"Organisation"@en-GB`.
- Label annotations: use `skos:prefLabel` for the preferred display label and `skos:altLabel` for synonyms or alternative names. These annotations apply directly to OWL entities without typing them as `skos:Concept`.
- Definition types: a mandatory taxonomic definition, an optional legal definition quoted verbatim from legislation or regulations, and an optional business definition in everyday language. For a class without a meaningful superclass or a property without a meaningful superproperty, a mandatory base definition fulfils the first requirement. Keep the three definition types distinct.
- OWL reasoning uses HermiT 1.4.3.456 to check consistency and find named classes that cannot have instances. Use OWL axioms when their open-world meaning expresses the intended semantics. Use SHACL for requirements on the data actually supplied. Logical conflicts block merging into `main`.
- Quality checks: run the complete automated suite and the applicable human review before every GitHub synchronisation. GitHub repeats the automated suite on pushes and pull requests.
- Status: draft model intended for joint development, not an approved project release.
- Modelling approach: OWL, using EBUCorePlus as the reference approach. Specific modelling conventions will be agreed individually; this does not imply importing EBUCorePlus domain concepts.
- Property applicability: describe the use of both object and datatype properties in the relevant classes through OWL restrictions, without global `rdfs:domain` statements on those properties.
- Object properties: use class-level OWL restrictions consistently. Do not assert global `rdfs:domain` or `rdfs:range` for object properties in the jointly developed ontology.
- Datatype properties: a global `rdfs:range` is permitted, for example `xsd:date`. This is permission, not a requirement to declare a global range on every datatype property. Do not assert global `rdfs:domain`; describe class-specific use through restrictions on the relevant classes.
- Use-case traceability: record which use cases require each class or property in the separate [use-case traceability register](USE_CASE_TRACEABILITY.md), outside the ontology.
- Model files: keep the central model in the single file `semantics/model/webuild.ttl` for now. Split it only when clear, meaningful module boundaries have been jointly established.
- Store application profiles as separate SHACL Turtle files under `semantics/application_profile` and check their examples with pySHACL. Use `https://w3id.org/ebwv/profile/<profile-id>#` for a profile's named shapes and `https://w3id.org/ebwv#` for references to central classes and properties.
- Central model and application profiles: put only generally applicable restrictions in the central model. Use-case-specific requirements for the presence of relations or values and their cardinalities belong in the relevant application profile.
- The term namespace is `https://w3id.org/ebwv#`. An illustrative term IRI is `https://w3id.org/ebwv#Organization`.
- The ontology IRI is `https://w3id.org/ebwv`. It identifies the ontology as a whole.
- Keep `main` free of logical conflicts. Publish a version containing a known conflict only as a separate publication, with explicit approval from both modellers and a prominent warning. Record the exception in [QUALITY_EXCEPTIONS.md](QUALITY_EXCEPTIONS.md).
- Merging into `main` requires applicable quality checks and approval by both modellers only for changes to the central ontology or its application profiles. A later change to the ontology or any profile invalidates both approvals.
- Namespace stewardship and the release publication process require joint agreement before external use of the draft.

The joint draft and the existing generated implementation vocabulary use the same EBWV term namespace. Before reusing an existing IRI or assigning a new one, check its meaning in the implementation vocabulary to avoid conflicting definitions. Substantive model changes require joint approval by Bart and his modelling colleague.

Confirm further starting decisions one at a time before implementing them.

## Modelling reference

The agreed reference is [EBUCorePlus](http://www.ebu.ch/metadata/ontologies/ebucoreplus). Its official documentation redirects to the [EBUCorePlus documentation site](https://ebu.github.io/ebucoreplus/). The source inspected for this decision is [`ontology/EBUCorePlus/ebucoreplus.owl` at commit `880d36abfd59b6c08a4794e9a5d4b93b0afda200`](https://github.com/ebu/ebucoreplus/blob/880d36abfd59b6c08a4794e9a5d4b93b0afda200/ontology/EBUCorePlus/ebucoreplus.owl). It declares version 2.0.0 and uses Turtle syntax despite its `.owl` extension. WEBUILD retains the agreed `.ttl` extension.

Verified features of that source include `owl:Class`, `owl:ObjectProperty`, `owl:DatatypeProperty`, and class-level `owl:Restriction` expressions, including value restrictions and qualified cardinalities. No `rdfs:domain` statements occur in the inspected graph. Global `rdfs:range` statements do occur: for 222 datatype properties, one annotation property, and the object property `ec:isAbout`, whose range is `ec:Asset`. Therefore, the reference must not be described as universally avoiding global ranges. These observations concern the inspected source graph, not its imported ontologies.

The confirmed direction is OWL modelling following this reference approach. WEBUILD applies the object property rule below consistently, including where the EBUCorePlus reference has an exception. The annotation properties for the three definition types are agreed below. Permitted restriction patterns and other annotations remain to be agreed one decision at a time. The automated suite runs the editorial checks and the HermiT logical checks described below. HermiT checks models within OWL 2 DL. The reference ontology has not been imported into the WEBUILD ontology, and no domain terms have been added.

## Object property modelling rule

For object properties, express class-specific conditions through OWL restrictions on the relevant classes. Do not attach global `rdfs:domain` or `rdfs:range` statements to those properties. In Protégé, record the restrictions in the relevant class descriptions and leave the object property's global Domains and Ranges empty.

This decision establishes where conditions are expressed. It does not prescribe a universal restriction or cardinality for every relation. Decide the appropriate restriction for each intended meaning; do not add existence or cardinality requirements merely because an object property is used by a class. Datatype properties follow the same class-level approach to applicability, while their ranges follow the separate rule below.

This rule governs the new jointly developed model. Archived originals and the existing implementation vocabulary remain unchanged.

## Central model and application profiles

The central model contains only restrictions that hold generally for the meaning of the relevant class or property, independently of a particular use case. Requirements that apply only within a specific use case, including mandatory relations or values and minimum or maximum counts, belong in that use case's application profile.

For example, an address may be mandatory for a particular application without requiring every organisation in the central model to have an address. This is an illustration of the separation, not a new class, property, or cardinality axiom.

This agreement does not prohibit cardinalities in the central model: include them there when they express a generally valid condition for the modelled concept. Do not promote a use-case-specific requirement into the central model merely because one implementation needs it. Reviewers must check the scope and justification of each restriction. Application profiles use SHACL in separate Turtle files under `semantics/application_profile`. Use `https://w3id.org/ebwv/profile/<profile-id>#` for the profile's named shapes and `https://w3id.org/ebwv#` for references to central model terms. pySHACL checks the example graphs without additional inference. Any profile-specific inference remains to be agreed. See the [application profile guide](application_profile/README.md).

## Datatype property modelling rule

A datatype property may have a global `rdfs:range`, such as `xsd:date`. Declaring a global range is optional and must reflect the intended meaning of the property across its uses. Describe the use of a datatype property in the relevant class through OWL restrictions; do not declare a global `rdfs:domain` on the property. In Protégé, leave the datatype property's global Domains empty. This is a class-level modelling convention, not an instruction to attach `rdfs:domain` statements to classes or a claim that class restrictions are semantically equivalent to global domain axioms. No datatype properties or range axioms have been added to the draft ontology by recording this decision.

## Term names and label language

Use readable American English terms for the local names in term IRIs. Use British English for English labels, with the RDF language tag `en-GB`. For example, the IRI `https://w3id.org/ebwv#Organization` would have the English label `"Organisation"@en-GB`. The IRI spelling and the label spelling deliberately differ.

These conventions apply to newly authored WEBUILD terms and labels. Preserve identifiers and original annotations in imported sources and archived material. Use `UpperCamelCase` for class local names and `lowerCamelCase` for property local names. For example, use `RegisteredOrganization` and `hasRegisteredAddress`. These are IRI naming conventions; they do not require CamelCase in human-readable labels. Use `skos:prefLabel` and `skos:altLabel` as specified below. The example illustrates naming only; it does not add an Organization class to the ontology or determine the spelling convention for all prose documentation.

## Preferred labels and synonyms

For each newly authored WEBUILD class or property, provide exactly one British English preferred label using `skos:prefLabel` with `en-GB`. Use zero or more `skos:altLabel` annotations for synonyms and alternative names of the same meaning, each with a language tag. Related but distinct meanings require separate terms rather than alternative labels.

For each term, allow at most one preferred label per language tag. Do not use the same literal, including its language tag, as both preferred and alternative label on that term. The automated quality checker enforces these structural label rules; spelling and whether alternative labels express the same meaning require human review.

Both properties are OWL annotation properties and can annotate OWL classes and properties directly. Their use does not require or imply `rdf:type skos:Concept`. The ontology declares these two reused annotation properties under their original SKOS IRIs; it does not import the complete SKOS ontology or add SKOS concept classifications. Separate duplicate `rdfs:label` annotations are not required by this convention.

Protégé is configured on this workstation to display `skos:prefLabel`, with the language preference field set to `en-GB, en, !` so British English has first priority. Both the Annotation Renderer and Preferences dialogs were confirmed. The ontology has no domain entities with labels yet, so display of actual domain labels has not been exercised.

To reproduce the setting, open **View → Custom rendering…**, select **Render by annotation property**, and click **Configure…**. Use `http://www.w3.org/2004/02/skos/core#prefLabel` as the annotation IRI, enter `en-GB, en, !` in **Set Language**, and confirm both dialogs with **OK**. Do not select `skos:altLabel` as the display property.

Rendering preferences are local application settings and are not distributed by the Turtle file; each modeller needs to configure them. These preferences affect the local Protégé display, not the ontology's term IRIs or stored label values.

Reference: [W3C SKOS lexical labels, including their domain and integrity conditions](https://www.w3.org/TR/skos-reference/#labels).

## Definition types

Keep three distinct types of definition rather than one undifferentiated definition field:

| Definition type | Requirement | Content |
| --- | --- | --- |
| Taxonomic definition | Mandatory | For a class, name its meaningful superclass and the distinguishing characteristics; if none exists, provide a base definition of the class. For a property, name its meaningful superproperty and the distinguishing characteristics; if none exists, provide a base definition of the relation. |
| Legal definition | Optional | A definition quoted verbatim from the relevant legislative or regulatory text when the term is used in law or regulation. |
| Business definition | Optional | A definition in everyday language. |

For example, if `CentrifugalPump` is a subclass of `Pump`, the taxonomic definition is: “A centrifugal pump is a pump with a rotating impeller.” This illustrates the definition pattern only; neither class has been added to the WEBUILD ontology.

The optional legal and business definitions do not replace the mandatory taxonomic definition or, for a class or property without a meaningful superclass or superproperty respectively, its mandatory base definition. Use the three local OWL annotation properties listed below. Their IRIs use the EBWV term namespace `https://w3id.org/ebwv#`. The proposal to use a single `skos:definition` field has not been adopted.

| Annotation property | Use |
| --- | --- |
| `:taxonomicDefinition` | Mandatory taxonomic definition; also holds the mandatory base definition for a class without a meaningful superclass or a property without a meaningful superproperty. |
| `:legalDefinition` | Optional verbatim legal definition; a source reference is mandatory whenever a legal definition is provided, preferably as a URI. |
| `:businessDefinition` | Optional definition in everyday language. |

In Protégé, add these annotations to the class or property being defined. The mandatory definition is an editorial requirement; declaring an annotation property does not enforce its presence. The automated quality checker verifies the presence of non-empty definition text; reviewers assess its meaning and taxonomic structure. No extra definition type or formal hierarchy is introduced by these declarations.

For both object and datatype properties, apply the following agreed rule:

- If a meaningful superproperty exists, the taxonomic definition names it and explains the distinguishing characteristic. Every relation asserted using the subproperty must also be a valid relation of the superproperty.
- If no meaningful superproperty exists, provide a mandatory base definition stating the relation, its direction, and the meaning of the related entities or value. Do not introduce an artificial superproperty solely to satisfy the definition format. The base definition is the fallback for the required definition, not an additional optional definition type.

For example, if `hasRegisteredAddress` is a subproperty of `hasAddress`, a definition can state: “Has registered address is a has-address relation in which the address is officially registered for the entity.” For a datatype property without a meaningful superproperty, a base definition can state: “Birth date is a relation between an entity and the date on which it was born.” These are illustrative examples only; no corresponding properties or hierarchy axioms have been added.

Record the definition as an annotation and the formal property hierarchy separately using `rdfs:subPropertyOf`. Definition text alone does not establish the formal hierarchy. Sharing a datatype alone does not justify a subproperty relationship. The existing rules for class-level applicability and global ranges remain unchanged.

Every legal definition must have a source reference identifying the relevant legislation or regulation and the specific article. Prefer a URI pointing to the official source and, where available, the specific article. The source reference is mandatory; use of a URI is a preference, not an absolute requirement when no suitable URI is available.

Use `dcterms:source` (`http://purl.org/dc/terms/source`) as an OWL annotation property on the specific `:legalDefinition` annotation assertion. This associates the source with that definition text. A source annotation on the class or property alone does not establish which definition it supports. The ontology declares `dcterms:source` without importing the Dublin Core vocabulary.

In Protégé, add the legal definition to the entity, then annotate that definition assertion with `dcterms:source`. Enter the source as an IRI value when a suitable URI is available, rather than a text literal containing a URL. If several legal definitions exist for one term, attach the appropriate source to each definition separately. The automated quality checker verifies that every legal definition has a source on its exact annotation assertion. Reviewers verify the source and quotation.

The following Turtle illustrates the agreed pattern with the EBWV term namespace, a fictional term, and a placeholder source URI.

```turtle
@prefix : <https://w3id.org/ebwv#> .
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

For a class without a meaningful named superclass, provide a mandatory base definition explaining what instances of the class are and what characterises them. Store it in `:taxonomicDefinition`. Do not invent a superclass solely to satisfy the definition format. A superclass of `owl:Thing` alone does not supply an informative taxonomic definition. The base definition fulfils the mandatory definition requirement; it is not a fourth definition type. This editorial rule does not add or change formal class hierarchy axioms.

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
6. Run the complete quality suite described below and review the applicable human checks before every synchronisation. Resolve errors before pushing; repeat the suite after any changes or incoming merge. Passing the automated suite does not establish semantic correctness.
7. Commit the intended files, push the working branch, and create a pull request. For a change to the central ontology or an application profile, record the quality results and both modellers' approvals of the reviewed version before merging it into `main`. The author's explicit agreement and the other modeller's review can record their respective approvals.
8. Reopen the file after a pull, merge, or branch switch. Otherwise, an open Protégé window may write an outdated in-memory copy back to disk.

Branches isolate changes, but do not prevent merge conflicts when both contributors change the same lines. When sharing one file, agree on who edits which part, keep branches short-lived, and coordinate overlapping work. The agreed initial arrangement is one central model file, `semantics/model/webuild.ttl`, with each modeller working on a separate branch. Keep this arrangement until clear, meaningful module boundaries have been jointly established. At that point, agree on the split and record each module's ontology IRI, filename, responsibility for changes, and imports; avoid duplicate definitions across files. Do not split the model solely by use case or modeller without an agreed conceptual boundary. This decision concerns the central model; application profiles and the external traceability register keep their separate roles.

## Conservative use of OWL reasoning

HermiT 1.4.3.456 checks whether the central ontology is logically consistent and whether each named class other than `owl:Nothing` can have instances. A failing check reports the inconsistency or lists the affected class IRIs. To inspect a finding in Protégé, select HermiT in the **Reasoner** menu and start the reasoner. Review the relevant axioms before changing the model. [HermiT documentation](https://github.com/owlcs/hermit-reasoner)

OWL reasoning uses open-world semantics. Missing assertions may represent unknown information, and a consistent ontology does not establish that supplied data are complete or conform to a use-case profile. The open-world assumption cannot be switched off for selected OWL restrictions. Adopt an OWL axiom only when its formal meaning matches the intended general semantics of the concept.

Use SHACL when a requirement concerns the values actually supplied in a data graph, including checking that required values are present and that recorded counts meet a profile's requirements. For example, an OWL existential restriction may remain consistent when no address is explicitly recorded; a SHACL minimum-count requirement can report that absence in the validated graph. This example introduces no terms or axioms into the draft.

The earlier separation remains in force: generally applicable conceptual restrictions belong in the central model, while use-case-specific requirements belong in separate application profiles. Where a generally applicable data-validation rule is also needed, document its scope before deciding how to share it across profiles; open-world reasoning alone is not its completeness check.

Logical inconsistency and unsatisfiable named classes reported by HermiT block merging into `main`. Approval of an exception authorises only a separate publication of the documented revision. Both modellers must explicitly approve the exception, and the publication must display a clear warning that identifies the conflict and its consequences. The [quality exception register](QUALITY_EXCEPTIONS.md) records the finding, rationale, scope, approvals, and resolution plan.

Use the [ontology pull request template](../.github/PULL_REQUEST_TEMPLATE/ontology.md) to record the quality evidence and both approvals. The local suite and GitHub workflow run HermiT after the structural and editorial checks. The automated check currently requires a model without imports because the project has yet to configure how to load a complete import closure. Its status fails on logical findings and on incomplete checks, including models outside OWL 2 DL. GitHub enforcement of the scoped merge requirements and any profile-specific SHACL inference settings are still to be configured.

References: [W3C OWL 2 Primer on open-world semantics](https://www.w3.org/TR/owl2-primer/) and [W3C SHACL minimum-count constraints](https://www.w3.org/TR/shacl/#MinCountConstraintComponent).

## Use-case traceability outside the ontology

Maintain the links between classes or properties and their supporting use-case requirements in [USE_CASE_TRACEABILITY.md](USE_CASE_TRACEABILITY.md). Use the full term IRI, the project's use-case identifier, the source requirement or passage, and the reason the term is needed. Update the register alongside the related model change so reviewers can assess both together.

These links belong in repository documentation, not in ontology annotations or domain relations. Review use-case coverage and unresolved mappings through the register. No use-case links have been added to `model/webuild.ttl` by this decision.

## Quality checks before every GitHub synchronisation

The merge requirements apply when a pull request changes the active central ontology (currently `semantics/model/webuild.ttl`) or files belonging to an application profile under `semantics/application_profile`, including its SHACL shapes and examples. A pull request with other changes as well is in scope as soon as it touches either area. GitHub may still run the quality suite for unrelated changes, whose merges are outside this policy.

Record the reviewed revision with each approval. If the central ontology or an application profile changes after approval, treat both approvals as expired. Run the applicable quality checks again and obtain fresh approval from both modellers for the revised content before merging into `main`. Changes confined to files outside the scope above do not trigger a new review under this rule.

Run all automated checks on the saved files before every push, including a push to a working branch. Complete the applicable human review below and review the Git diff. If a pull or merge changes the model, run the checks again on the resulting files before continuing or pushing. Protégé changes must be saved first; these checks read the files on disk.

Install a JDK (version 17 or later) and ensure Maven is available on your path. Maven downloads the pinned HermiT dependency on the first run. From the repository root, install the pinned Python dependencies once in a local virtual environment.

```sh
python3 -m venv .local/quality-venv
.local/quality-venv/bin/python -m pip install -r semantics/quality/requirements.txt
```

Run the full automated suite:

```sh
.local/quality-venv/bin/python -B semantics/quality/run.py
```

A non-zero exit status means the checks failed. Fix the reported errors before synchronising. The suite runs the checker regression tests, validates the active model, runs HermiT on the same model files, and checks application-profile examples with pySHACL. The same suite is configured in `.github/workflows/ontology-quality.yml` for every push, pull request, and manual workflow run. It runs on GitHub once the workflow is pushed. Local execution is a working agreement, not an installed Git hook. This workflow does not configure branch protection or enforce the human approval process.

The checks parse all `.ttl` files under `semantics/model` except `Archive` and `modelling_considerations`, and validate their combined graph. `webuild.ttl` must exist. Archived originals, `vocab`, and generated `docs/ebwv` are outside this draft model's validation scope. Imports and source URIs are not fetched. The checker expects the ontology declaration for `https://w3id.org/ebwv` and applies namespace-specific checks to terms under `https://w3id.org/ebwv#`.

Automated checks cover:

- Valid Turtle, the agreed ontology declaration, and the required annotation property declarations.
- Logical consistency and named classes that cannot have instances, checked by HermiT within OWL 2 DL.
- SHACL shape validity and expected conformance of each profile example, checked by pySHACL. See the [application profile guide](application_profile/README.md).
- UpperCamelCase class names and lowerCamelCase property names for authored terms; this checks the lexical pattern, not English spelling.
- Exactly one non-empty `en-GB` preferred label, at most one preferred label per language, language-tagged synonyms, and no identical preferred and alternative label on one term.
- A non-empty taxonomic or base definition for authored classes and properties, including local annotation properties. Optional legal and business definitions must contain text when present.
- No global domain for declared object or datatype properties in the authored graph, and no global range for object properties. Datatype ranges remain optional and permitted.
- A source attached to each exact legal-definition assertion, including its language tag or datatype. Stale or mismatched source annotations fail. A non-empty textual citation is accepted with a review warning because a URI is preferred rather than mandatory.

Human review covers what these checks cannot establish: meaningful superclass/superproperty choices and differentiae, correct use of class restrictions and separation of general conditions from use-case-specific requirements, American English term names and British English labels, genuine synonymy, exact legal quotations and the relevance of the cited article and version, business-language clarity, use-case coverage through the separate traceability register, and approval by both modellers before merging substantive changes. Source availability is not automatically tested. Reviewers confirm that application-profile examples exercise the intended requirements and that failures occur for the expected reasons. A green automated result does not certify these human checks.

## Local imports

An ontology IRI identifies the ontology; the path to the `.ttl` file specifies its storage location. Do not make that identity depend on someone's local user directory.

Protégé can resolve local imports through a `catalog-v001.xml` file. Share such a catalogue only with reviewed, relative file paths. Do not automatically ignore catalogues: they may be needed to open the model correctly on another computer. Do not silently redirect a missing import to an ontology with a different IRI.

The following was observed in the archived models on 30 September 2026:

- `Archive/PRIMER.ttl` declares `http://data.webuildconsortium.eu/PRIMER`.
- `Archive/authorisation_part.ttl` imports `http://www.braindex.nl/data/PRIMER` and uses both the Braindex namespace and `http://data.webuildconsortium.eu/primer#`, with lowercase `primer`.
- `Archive/authorisation_part_instance.ttl` imports `http://data.webuildconsortium.eu/authorisation.ttl`, the ontology IRI of `authorisation_part.ttl`.

The different PRIMER IRIs do not automatically identify the same ontology. The team must determine the intended identity; these sources were not changed during the technical setup.

## Agreements before modelling

The ontology IRI, term namespace, draft status, and joint approval process are recorded above. Namespace stewardship and the release publication process remain open. Readable American English term IRIs and British English labels are agreed above. IRI capitalisation is also agreed above. Preferred and alternative label properties are also agreed above. Use-case traceability is recorded outside the ontology as agreed above. The central model initially stays in one `webuild.ttl` file; a future split requires jointly agreed, meaningful module boundaries. Use English for new GitHub documentation and other newly authored content; preserve existing source material and archived originals. Within the agreed OWL approach, agree on the constructs that Protégé must preserve: a syntactically valid Turtle file cannot necessarily be saved through an OWL editor without changes. Check existing sources using a copy and a comparison of the RDF triples.

A Git merge without textual conflicts can still combine contradictory modelling choices. Always review meaning and relevant use case examples. GitHub enforcement of the required checks and reviews for ontology and application-profile changes remains to be configured.

The selected working directory is under OneDrive. The recommendation is to eventually place the active Git working directory outside a synchronised folder and collaborate through GitHub; two independent synchronisation mechanisms make the working directory harder to manage. Until then, keep the files fully available locally and use this checkout on one computer at a time. The directory was not relocated during setup.

The existing GitHub repository is public. A push publishes changes; saving locally or making a local commit does not.

In this local checkout, executable bits changed on many files without content changes. Therefore, `core.filemode=false` is set for this checkout only, so those differences do not clutter the review. This is a local Git setting and is not shared with the repository.

## Sources

- [Protégé menus and save functions](https://protegeproject.github.io/protege/menus/)
- [GitHub documentation on merge conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts)
- [Publication process in this repository](../vocab/README.md)
