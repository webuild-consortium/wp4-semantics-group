# Working together with Protégé and GitHub

This guide describes the technical setup for collaborative ontology development in `webuild-consortium/wp4-semantics-group`. Protégé edits local files; Git records versions, and GitHub supports sharing and review. The workflow below is a proposal for the team and does not establish substantive modelling rules. English is the working language for new documentation and other files prepared for GitHub.

For the current implemented model, superseded naming choices, legal-form/ownership examples and open mappings, see [Current semantic model decisions](MODEL_STATUS.md). Historical validation entries below refer to the graph at that point in the discussion.

## Starting file

Open `semantics/model/webuild.ttl` in Protégé. The extension ontology IRI is `https://w3id.org/ebwv/semantic-model`; new terms use `https://w3id.org/ebwv/semantic-model#` (`ebwsm:`). Existing EBWV terms retain `https://w3id.org/ebwv#` (`ebwv:`). The draft directly reuses `prov:Agent` and its imported Person, Organization and SoftwareAgent subtypes. It defines the physical-actor subtype `ebwsm:Machine`, Role and RoleFulfillment, the EconomicOperator, PublicSectorBody, EnterpriseOwner and Shareholder role subtypes, LegalForm and supporting object properties and three extension definition annotations. It also defines [Involvement and its relations](MODEL_STATUS.md#involvement) and reuses dcterms:PeriodOfTime. No separate WEBUILD Agent class is defined. It imports the approved local PROV-O core through the ontology identity `http://www.w3.org/ns/prov#`, resolved through the adjacent catalog-v001.xml to the checksum-pinned 2013-04-30 copy, and obtains prov:wasRevisionOf and prov:specializationOf as object properties from that import. It uses the standard annotation properties `skos:prefLabel`, `skos:altLabel`, and `dcterms:source` under their original IRIs.

The model also imports the approved [Dublin Core class module](imports/dcterms/README.md), containing all 22 DCMI Terms classes and their eight mutual subclass relations under their original IRIs. This is a class-only OWL projection, not the full DCMI RDF schema. Both dependencies load from `webuild.ttl`; keep that as the single working file. In Protégé select **View → Show the imports closure of the active ontology** and **Render by prefixed name** to see the combined hierarchy. After external file changes, reopen the current saved model so the session loads the updated imports; do not overwrite it from an older in-memory session. Prefixes should map `ebwv:` to `https://w3id.org/ebwv#`, `ebwsm:` to `https://w3id.org/ebwv/semantic-model#`, `prov:` to `http://www.w3.org/ns/prov#` and `dcterms:` to `http://purl.org/dc/terms/`.

The three earlier Turtle models have been preserved unchanged in `semantics/model/Archive`, as requested. The new ontology does not import them. `authorisation_part.PlantUML` is also in `Archive`. The `modelling_considerations` directory has been retained and relates to earlier modelling work.

## Protégé display and prefix settings

Keep `webuild.ttl` as the single working file. Dependency documents are loaded through its imports and the adjacent catalogue; a separate inspection ontology or additional modelling window is not needed. The [dependency overview](imports/README.md) distinguishes the complete PROV-O core from the class-only Dublin Core projection.

Select **View → Render by prefixed name**. Prefix declarations in Turtle are normally read on loading, but a session can retain older mappings after external edits. If an entity is shown as a full IRI, check **Active ontology → Ontology prefixes**. The view can also be added through **Window → Views → Ontology views → Ontology prefixes**.

| Prefix | Exact namespace |
| --- | --- |
| `ebwv:` | `https://w3id.org/ebwv#` |
| `ebwsm:` | `https://w3id.org/ebwv/semantic-model#` |
| `prov:` | `http://www.w3.org/ns/prov#` |
| `dcterms:` | `http://purl.org/dc/terms/` |

The current display includes `ebwsm:Role`, `ebwsm:RoleFulfillment`, `ebwsm:Machine`, `prov:Agent` and its imported subtypes. The separately imported `dcterms:Agent` is not a superclass or equivalent of PROV Agent in this model. The earlier requested `ebwv:Agent` display was superseded by direct PROV reuse on 23 November 2026. Prefix spelling is a presentation/serialization choice; replacing `#` with `/` in a namespace changes term IRIs and must not be used as a display fix.

Select **View → Show the imports closure of the active ontology** to see the dependencies together with WEBUILD. **File → Loaded ontology sources…** shows which files have loaded. If classes appear only under **Show all loaded ontologies**, verify the import identity and its membership in the active import closure; the PROV-O correction below records the observed instance of that problem. After external changes, reopen or reload the saved working model while preserving any unsaved work; changes on disk do not automatically update the ontology already held in memory.

On 23 November 2026 Bart decided to retain the standard Protégé class hierarchy. The proposed custom display grouping under a visual `rdfs:Class` root was discussed and declined; no custom view/plugin will be introduced for that purpose. No class axioms are added to obtain a particular display grouping. The [standard Class Hierarchy view](https://protegeproject.github.io/protege/views/class-hierarchy/) places classes without another asserted named parent under `owl:Thing`. The Dublin Core dependency explicitly projects its source `rdfs:Class` declarations into `owl:Class`; this is documented source selection, not an assertion that the official schema already contained those OWL declarations.

## Confirmed starting decisions

- Working language: English for new documentation and other files prepared for GitHub.
- Term IRIs: use readable American English terms for new extension terms, for example `ebwsm:Organization`; preserve existing reused EBWV IRIs.
- IRI capitalisation: use `UpperCamelCase` for class names, such as `RegisteredOrganization`, and `lowerCamelCase` for property names, such as `hasRegisteredAddress`.
- English labels: use British English spelling and the language tag `en-GB`, for example `"Organisation"@en-GB`.
- Label annotations: use `skos:prefLabel` for the preferred display label and `skos:altLabel` for synonyms or alternative names. These annotations apply directly to OWL entities without typing them as `skos:Concept`.
- Definition types: a mandatory taxonomic definition, an optional legal definition quoted verbatim from legislation or regulations, and an optional business definition in everyday language. For a class without a meaningful superclass or a property without a meaningful superproperty, a mandatory base definition fulfils the first requirement. Keep the three definition types distinct.
- OWL reasoning uses HermiT 1.4.3.456 to check consistency and find named classes that cannot have instances. Use OWL axioms when their open-world meaning expresses the intended semantics. Use SHACL for requirements on the data actually supplied. Logical conflicts block merging into `main`.
- Quality checks: run the complete automated suite and the applicable human review before every GitHub synchronisation. GitHub repeats the automated suite on pushes and pull requests.
- Status: draft model intended for joint development, not an approved project release.
- Modelling approach: OWL, using EBUCorePlus as the reference approach. Specific modelling conventions will be agreed individually; this does not imply importing EBUCorePlus domain concepts.
- Top-level class structure: use multiple meaningful top-level domain classes without introducing a custom common root class. These classes remain under `owl:Thing` through OWL semantics; explicit `rdfs:subClassOf owl:Thing` statements are not required. Agree the meaning and placement of each top-level domain class individually before adding it. This decision does not establish disjointness or an exhaustive partition. The local OJA reference models may inform discussion without adopting their common root, hierarchy, or axioms.
- Property applicability: describe the use of both object and datatype properties in the relevant classes through OWL restrictions, without global `rdfs:domain` statements on those properties.
- Object properties: use class-level OWL restrictions consistently. Do not assert global `rdfs:domain` or `rdfs:range` for object properties in the jointly developed ontology.
- Datatype properties: a global `rdfs:range` is permitted, for example `xsd:date`. This is permission, not a requirement to declare a global range on every datatype property. Do not assert global `rdfs:domain`; describe class-specific use through restrictions on the relevant classes.
- Use-case traceability: record which use cases require each class or property in the separate [use-case traceability register](USE_CASE_TRACEABILITY.md), outside the ontology.
- Model files: keep the central model in the single file `semantics/model/webuild.ttl` for now. Split it only when clear, meaningful module boundaries have been jointly established.
- Store application profiles as separate SHACL Turtle files under `semantics/application_profile` and check their examples with pySHACL. Keep `https://w3id.org/ebwv/profile/<profile-id>#` for named shapes. Reference existing vocabulary terms with `ebwv:` and new extension terms or candidates with `ebwsm:`. Use a readable English profile name in lowercase with hyphens between words as the profile ID, for example `authorised-signatories`.
- Central model and application profiles: put only generally applicable restrictions in the central model. Use-case-specific requirements for the presence of relations or values and their cardinalities belong in the relevant application profile.
- The extension term namespace is `https://w3id.org/ebwv/semantic-model#` (`ebwsm:`). Existing terms from the published vocabulary keep `https://w3id.org/ebwv#` (`ebwv:`).
- The extension ontology IRI is `https://w3id.org/ebwv/semantic-model`. It identifies the extension, separately from the published EBWV vocabulary.
- The extension Turtle model and separate SHACL Turtle profiles are its authoritative sources. The existing EBWV publication remains generated from YAML until its maintainers agree and implement a separate migration.
- Keep `main` free of logical conflicts. Publish a version containing a known conflict only as a separate publication, with explicit approval from both modellers and a prominent warning. Record the exception in [QUALITY_EXCEPTIONS.md](QUALITY_EXCEPTIONS.md).
- Merging into `main` requires applicable quality checks and approval by both modellers only for changes to the central ontology, its imported dependency files or resolution metadata, or its application profiles. A later change to the ontology, an imported dependency or its resolution metadata, or any profile invalidates both approvals.
- Namespace stewardship and the release publication process require joint agreement before external use of the draft.

Before reusing an existing EBWV IRI, check its meaning and axioms in the pinned upstream version. Additional statements about that IRI must preserve its meaning; a distinct or incompatible meaning requires a new extension IRI and a justified mapping. New extension terms must not be minted in the EBWV namespace. Substantive model changes require joint approval by Bart and his modelling colleague.

Confirm further starting decisions one at a time before implementing them.

## Next modelling source: General Authorisation Model

Bart selected [Reference_Documents/Authorisation.PlantUML](../Reference_Documents/Authorisation.PlantUML) as the integration source, ahead of further Authorised Signatories candidate-class adoption. The selected file contains 613 lines; its SHA-256 at selection/review is `9c5066cf4c8e6af64cf2648cb7e6180b38134a4f6530e83a9f70679d43464931`. It describes proposed RDF classes, object-property relations and datatype properties. On 24 November 2026 Bart requested that this exact reference and `Reference_Documents/ebucoreplus.ttl` be included in version control, with all other contents of `Reference_Documents` remaining excluded. The reference diagram is not an additional imported ontology or a published normative requirement. It is distinct from `semantics/model/Archive/authorisation_part.PlantUML`.

Review the classes one at a time: source meaning and use-case need, compatibility with reviewed EBWV/Dublin Core/PROV concepts, an appropriate existing superclass if justified, the taxonomic or base definition, and only then the relevant property and OWL/SHACL decisions. Implement substantive mappings after agreement. The approved Agent, Role and RoleFulfillment meanings provide discussion context; the source selection does not itself map them to PROV-O or adopt further classes, properties or cardinalities. A shared local name alone does not establish equivalence.

## Source ownership and EBWV reuse

On 20 November 2026 Bart approved reusing existing EBWV terms, placing new terms in `ebwsm:`, and treating the extension's RDF sources as authoritative. The namespace is adopted for the local joint draft; external publication and namespace stewardship remain subject to team agreement. The namespace change preserves the approved Agent meaning and superclass relation.

| Source | Responsibility |
| --- | --- |
| `semantics/model/webuild.ttl` | Authoritative OWL model for extension terms and reviewed, compatible augmentations of existing terms. |
| `semantics/application_profile/*/shapes.ttl` | Authoritative SHACL constraints for each application profile. Keep these separate from the Protégé OWL editing workflow. |
| `vocab/src/vocabulary.yml` | Current source of the existing published EBWV vocabulary and its generated outputs. |
| `docs/ebwv/vocabulary.ttl` | Generated EBWV output; not an editable source for the extension. The current local copy predates the pinned upstream revision. |

The EBWV reuse baseline is repository revision [`c34c0f810c1ba4155360a36c590c81f0ccd41c43`](https://github.com/webuild-consortium/wp4-semantics-group/commit/c34c0f810c1ba4155360a36c590c81f0ccd41c43), dated 2 November 2026 and inspected on 20 November 2026. Consult the [vocabulary at that revision](https://github.com/webuild-consortium/wp4-semantics-group/blob/c34c0f810c1ba4155360a36c590c81f0ccd41c43/docs/ebwv/vocabulary.ttl) and its [YAML source](https://github.com/webuild-consortium/wp4-semantics-group/blob/c34c0f810c1ba4155360a36c590c81f0ccd41c43/vocab/src/vocabulary.yml), rather than assuming that local generated files equal current upstream files. The retrieved Turtle file's SHA-256 is `022b65e1c5753353eeba8d4911bbdc710b64f6e5760c2a09b4b0cf48e8c8e7c4`.

**Full vocabulary import is pending.** The pinned Turtle fails parsing at line 2762: the regular-expression backslash in the EUID pattern is not escaped for a Turtle string. The upstream original has not been patched, imported or replaced by a modified copy in the active model. The extension currently reuses reviewed IRIs, with local OWL declarations where needed, and records the baseline as `dcterms:source`. A source link is not `owl:imports` and does not load the vocabulary's axioms. A passing extension suite does not certify the full EBWV graph. Resolve the upstream serialization defect, establish reproducible local dependency resolution and check the complete imported graph before enabling a full import; syntax repair alone is not proof of OWL 2 DL compatibility.

Existing EBWV properties have global domain and range axioms. These remain effective if the vocabulary is imported; a new namespace does not override or remove them. The authored extension follows the class-level modelling rules below. Review the consequences of every reused property and propose an upstream correction or a distinct extension property when meanings differ. For example, the current `ebwv:role` is an object property whose range includes an enumeration of existing roles; it is not automatically suitable for arbitrary context-specific role objects.

The extension is not generated from YAML. Future HTML or RDF serializations of it must be derived from the authoritative RDF sources. A JSON-LD context additionally needs explicit mapping and coercion decisions where relevant; a lossless context must not be assumed from the ontology alone. Replacing YAML as the source of the published EBWV vocabulary requires a separate team decision, generator migration and validation of existing outputs. No such upstream migration is implemented by this extension change.

The three new definition annotation properties moved from `ebwv:` to `ebwsm:`. The Authorised Signatories profile's 25 candidate IRIs also moved to `ebwsm:` in its shapes and six examples; the ten selected existing EBWV term IRIs remain unchanged. None of the 25 candidates is declared in the pinned vocabulary. This is a namespace migration, not adoption of those candidates into the central ontology. The later Role, RoleFulfillment and Dublin Core period decisions are recorded below; `InformationObject` remains a proposal.

Validation after the namespace migration on 20 November 2026: the full suite passed all 27 checker regression tests, structural and editorial checks on the 23-triple extension graph, HermiT consistency and named-class satisfiability checks, and all six SHACL examples with their expected results. A separate RDF graph comparison confirmed that the shapes and examples differ from their previous graphs only by migration of the 25 candidate IRIs. The approved Agent superclass relation is preserved. This evidence covers the authored extension, not a full EBWV import.

## Modelling reference

The [shared local EBUCorePlus snapshot](../Reference_Documents/ebucoreplus.ttl) is included in version control at Bart's request on 24 November 2026. Its SHA-256 is `3f0162826e4f242586c1c06b4fbf519f2ddd5854d9e4aa97a70913fae820d76b`. The snapshot and the selected Authorisation diagram are preserved without content changes. The `.gitignore` exceptions cover only these two exact paths; other reference files and subdirectories remain local. Versioning this snapshot does not add an EBUCorePlus import to WEBUILD.

The agreed reference is [EBUCorePlus](http://www.ebu.ch/metadata/ontologies/ebucoreplus). Its official documentation redirects to the [EBUCorePlus documentation site](https://ebu.github.io/ebucoreplus/). The source inspected for this decision is [`ontology/EBUCorePlus/ebucoreplus.owl` at commit `880d36abfd59b6c08a4794e9a5d4b93b0afda200`](https://github.com/ebu/ebucoreplus/blob/880d36abfd59b6c08a4794e9a5d4b93b0afda200/ontology/EBUCorePlus/ebucoreplus.owl). It declares version 2.0.0 and uses Turtle syntax despite its `.owl` extension. WEBUILD retains the agreed `.ttl` extension.

Verified features of that source include `owl:Class`, `owl:ObjectProperty`, `owl:DatatypeProperty`, and class-level `owl:Restriction` expressions, including value restrictions and qualified cardinalities. No `rdfs:domain` statements occur in the inspected graph. Global `rdfs:range` statements do occur: for 222 datatype properties, one annotation property, and the object property `ec:isAbout`, whose range is `ec:Asset`. Therefore, the reference must not be described as universally avoiding global ranges. These observations concern the inspected source graph, not its imported ontologies.

The confirmed direction is OWL modelling following this reference approach. WEBUILD applies the object property rule below consistently, including where the EBUCorePlus reference has an exception. The annotation properties for the three definition types are agreed below. Permitted restriction patterns and other annotations remain to be agreed one decision at a time. The automated suite runs the editorial checks and the HermiT logical checks described below. HermiT checks models within OWL 2 DL. The reference ontology has not been imported into the WEBUILD ontology. The adopted Agent, Role, RoleFulfillment and time-interval decisions are described below.

## Agent modelling decision

On 23 November 2026 Bart confirmed that the intended actors fit the PROV responsibility concept, explicitly included software agents and requested direct `prov:Agent` reuse without a separate `ebwv:Agent`. This supersedes the 19 November augmentation of the existing EBWV term under Dublin Core Agent and the earlier open software-scope decision. The local declaration, definition and superclass axiom for `ebwv:Agent` have been removed. The published EBWV vocabulary and archived references are preserved; the external IRI is not deprecated or declared equivalent by this local change.

| Term | Current modelling decision |
| --- | --- |
| `prov:Agent` | Direct reuse of the pinned PROV-O class and responsibility-based meaning. |
| `prov:Person` | Existing imported human Agent subtype, reused directly with preferred label “Person”. The earlier Natural Person alternative label is withdrawn; legal classification and mappings remain separate questions. |
| `prov:Organization` | Existing imported Agent subtype, reused directly; local British English label “Organisation”. |
| `prov:SoftwareAgent` | Existing imported Agent subtype for running software, now explicitly within scope. |
| `ebwsm:Machine` | New subclass of `prov:Agent`: a physical actor able to execute predetermined processes autonomously under software control. |
| `ebwsm:runsSoftwareAgent` | Optional link from Machine to a separately represented running software actor; a class-level all-values restriction types the target as SoftwareAgent. |

The [decision and migration rationale](model/modelling_considerations/Agents_and_Machines.md) distinguishes the physical actor, running software, software artifacts and permission. It records Bart's payment-terminal and autonomous-robot examples, the software-link choice and the consequences for role players and Involvement. The [Agent hierarchy diagram](model/Agents.PlantUML) and [synthetic example](examples/agents/machine-software.ttl) illustrate the distinction. No duplicate local declarations of imported classes are needed; preferred labels are local annotations only.

The two specialised role classes now require `prov:Agent` players. Generic role players remain unrestricted. Classification as Agent, SoftwareAgent or Machine does not grant a mandate, legal personhood, representation rights or eligibility for a particular legal role. The existing profiles have not been changed to admit new signatory types. No global domain/range, sibling disjointness or exhaustive Agent partition has been added. PROV Agent's imported disjointness with InstantaneousEvent participates in reasoning.

The separate `dcterms:Agent` stays available from its pinned class module. No superclass or equivalence between PROV Agent and Dublin Core Agent is asserted. The former local inference to Dublin Core Agent is therefore not preserved merely by using the new actor type. Approval by the other modeller of the resulting model revision remains required before merging.

During the discussion Bart initially requested `skos:altLabel "Natural Person"@en-GB` for `prov:Person`. The later legal-context discussion distinguishes that classification from the human actor. The alternative label is therefore withdrawn in the consolidated revision. The [terminology note](model/modelling_considerations/Agents_and_Machines.md#person-and-the-webuild-term-natural-person) records the sequence. No LegalPerson subclass of prov:Person, NaturalPerson equivalence or disjointness, extra human identity, legal-capacity rule or profile change is asserted.

Validation on 23 November 2026: all 45 checker/dependency regression tests passed, the 125-triple authored graph passed structural/editorial checks, both pinned dependencies resolved and verified unchanged, and HermiT found the complete three-document model OWL 2 DL conformant, consistent and free of unsatisfiable named classes. All 20 actor/role HermiT controls passed, including software/machine Agent inference, the software-target restriction, distinct physical/software individuals, optional software links, imported Agent/event disjointness and the absence of a global Dublin Core alignment. All six unchanged SHACL examples returned their expected outcomes. Both synthetic examples were additionally checked together with the full model and passed OWL 2 DL, consistency and satisfiability checks. The quality checker now rejects reintroduction of ebwv:Agent in active authored triples. The new Agent diagram and updated PROV core diagram rendered successfully.

Historical validation of the subsequently superseded Natural Person label revision: all 45 regression tests, 20 HermiT actor/role controls and six expected SHACL results passed; the authored graph contains 127 triples. RDF graph comparison with the preceding revision found exactly two added annotations on prov:Person (the alternative label and explanatory comment) and no removed or changed logical axioms. The updated Agent diagram rendered successfully.

## Role, fulfilment and time decisions

On 20 November 2026 Bart approved the following meanings for the joint draft. Role and RoleFulfillment are new top-level extension classes with base definitions and no artificial named superclass. Dublin Core PeriodOfTime is reused directly as the interval class. Approval by the other modeller is still required before merging the resulting revision into main.

| IRI | Preferred label | Definition |
| --- | --- | --- |
| `https://w3id.org/ebwv/semantic-model#Role` | `"Role"@en-GB` | A role is a context-dependent capacity that an entity can fulfil when participating in an activity, event, relationship, or situation. |
| `https://w3id.org/ebwv/semantic-model#RoleFulfillment` | `"Role fulfilment"@en-GB` | A role fulfilment is the participation of a particular entity in a particular role during one continuous time interval. |
| `http://purl.org/dc/terms/PeriodOfTime` | `"Period of time"@en-GB` | The existing DCMI class describes an interval named or defined by its start and end dates. Its original definition is supplied by the imported class module; the local display label and source link remain in the working file. No new definition is assigned to the external class. |

The player, role and role fulfilment retain distinct identities. A role can exist without a current player, and its player is not restricted to Agent. A particular role fulfilment associates one player with one role during one continuous interval; a later separate period is represented by a different fulfilment. The context belongs to the role and is reached through it, avoiding a second context assertion on the fulfilment. An ended fulfilment remains a historical fact. The general class definition does not assert that every classification of a thing is immutable throughout its existence.

The local OJA Role reference in Reference_Documents/OJA/ebio.ttl supplies the distinction between a player, its role and the time qualification of playing the role. Its IRI is recorded as a source, not as a superclass or equivalence mapping. The OJA FunctionalEntity hierarchy and organisation/name SHACL obligations are not adopted. The [W3C n-ary relation pattern](https://www.w3.org/TR/swbp-n-aryRelations/) informs modelling a fulfilment as a separate object when the relation has its own time qualification.

The selected external class is the official [dcterms:PeriodOfTime](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/terms/PeriodOfTime), with the exact IRI http://purl.org/dc/terms/PeriodOfTime. It represents an interval rather than merely a duration. It is distinct from dcterms:Period, which is an encoding datatype. Reusing the interval class does not itself specify properties for its boundaries or require both dates to be supplied. Missing or not-yet-known boundaries must not be interpreted as an assertion of endless fulfilment.

At that stage the model contained the approved class declarations, labels, definitions and explanatory annotations only. The player/role/interval properties and restrictions were subsequently implemented on 23 November 2026 as described below. Time boundaries and SHACL completeness rules remain open. No mapping from the candidate SignatoryRole or change to the existing profile constraints follows from these decisions.

The existing ebwv:PeriodOfTime is not imported, modified, deprecated or declared equivalent to the Dublin Core class by this change. Bart approved the shortened issue text, and [GitHub issue #67](https://github.com/webuild-consortium/wp4-semantics-group/issues/67) was published from his account on 20 November 2026 to review direct Dublin Core reuse and the continued meaning and use of the EBWV IRI. The issue does not itself adopt a mapping or change the vocabulary. Source changes to that vocabulary still follow its current YAML build process.

Validation after adding the role and interval classes on 20 November 2026: the full suite passed all 27 checker regression tests, structural/editorial checks on the 37-triple active extension graph, HermiT consistency and named-class satisfiability checks, and all six existing SHACL examples with their expected results. This verifies the declarations and authored graph; it does not validate fulfilment relations that have not yet been formalised.

## Economic Operator, Public Sector Body and supporting role relations

On 23 November 2026 Bart agreed to model Economic Operator and Public Sector Body as roles, authorised the supporting properties and requested that the reasoning and the consequences for Involvement be recorded. The local draft now declares `ebwsm:EconomicOperator` and `ebwsm:PublicSectorBody` as subclasses of `ebwsm:Role`. Neither is a subclass of Agent. These new role meanings deliberately use extension IRIs: the existing `ebwv:` terms describe actors and must not silently be redefined as role objects. No equivalence mapping is asserted.

The [decision and General Authorisation Model review](model/modelling_considerations/Actor_Roles_and_Involvement.md) records the source version, the capacity-versus-institutional-status distinction, namespace rationale, exact OWL consequences and remaining Involvement decisions. The legal source is [COM(2025) 838 final, Article 3(4) and (5)](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:52025PC0838), not an assertion of the current legislative outcome. Taxonomic role definitions are our interpretation; no verbatim legal-definition annotation is added.

The properties `hasPlayer`, `fulfillsRole` and `hasPeriod` implement the existing one-player/one-role/one-continuous-interval meaning of RoleFulfillment with class-level exact cardinalities. Additional all-values restrictions type the role and interval. `hasContext` links a role to its setting; no context count is imposed. Inverse restrictions on each specialised role require referring fulfilments to have Agent players. Generic role players remain unrestricted, and specialised roles can exist without current players. Context stays on the role. No global property domain/range, globally functional property, key, tuple uniqueness, PROV mapping, date-boundary rule or SHACL requirement is introduced.

The [synthetic two-level example](examples/roles/actor-roles.ttl) distinguishes the business actor's EconomicOperator role from a person's internal role with that business as context. Involvement in the selected reference can designate an eligible set without naming a particular actor, so it is not adopted as a subclass of RoleFulfillment. The review identifies actor-targeting source relations and identifiers that must not be redirected to role individuals. The selected and archived references are preserved; their review does not adopt the complete General Authorisation Model. The other modeller's approval of the resulting revision remains pending before merging.

Validation on 23 November 2026: the complete suite passed all 44 checker/dependency regression tests, structural/editorial checks on the 114-triple authored graph, both pinned dependency checks, OWL 2 DL conformance, HermiT consistency and named-class satisfiability, and all six SHACL examples with their expected outcomes. Thirteen additional HermiT semantic controls passed and now run within the suite: specialised roles infer Agent players and reject explicitly non-Agent players; generic roles permit non-Agent players; unfulfilled non-Agent roles and unrecorded fillers are consistent; two explicitly different players, roles or periods on one fulfilment are inconsistent; role/period types are inferred; and one actor may fulfil two distinct capacities. The synthetic actor-role example was additionally checked together with the complete imported model and passed OWL 2 DL, consistency and satisfiability checks. These checks do not establish legal eligibility, authority, date validity or completeness of supplied data.

## Organisation, legal form, ownership and Role boundaries

The [current status](MODEL_STATUS.md) consolidates the subsequent discussion and its legal sources. The organisation/enterprise is distinguished from its legal-form classification and from the Agents fulfilling roles towards it. `ebwsm:LegalForm` and `ebwsm:hasLegalForm` implement that classification distinction. The class is disjoint with prov:Agent; the target type is expressed on prov:Organization by an all-values restriction. No organisation-level existence or maximum-count restriction is imposed.

`ebwsm:EnterpriseOwner` and `ebwsm:Shareholder` are separate Role subclasses implementing the two illustrative ownership meanings. Their fulfilments require Agent players through role-scoped restrictions, without closing eligibility to only natural/legal persons. They are not equated or made subclasses of each other. An enterprise's owner is distinct from an owner of shares or company assets. No rule makes every organisation have an owner or infers an owner of a public organisation. The inherited sole-proprietorship co-ownership example prevents an unconditional single-owner limit.

The [simple drawings](examples/ownership/Organization_LegalForm_Ownership.PlantUML) have an [expanded RDF counterpart](examples/ownership/ownership.ttl) with actual contextual roles, fulfilments and unknown-bound intervals. These are illustrative data, not verified register assertions. The requested update implements these working meanings in the local joint draft; definitions and restrictions remain reviewable through the normal joint process before merging.

The distinction between prov:Role (activity-related qualification) and ebwsm:Role (broader contextual capacities) remains. No subclass, equivalence or disjointness mapping is added in either direction. RoleFulfillment is likewise not mapped to prov:Association. These boundaries are now explicit in model comments as well as documentation.

Validation of the consolidated revision: The full suite passed on 23 November 2026: 45 checker/dependency regression tests, structural/editorial checks on the 180-triple authored graph, both unchanged checksum-pinned dependencies, OWL 2 DL conformance, consistency and no unsatisfiable named classes across the complete three-document model. All 37 actor/role HermiT controls passed, including co-ownership, classification-versus-Agent separation, legal-form target inference, ownership/shareholding separation and the absence of unapproved PROV Role/Association mappings. The same reasoner and controls also passed with all three synthetic RDF example graphs loaded together. All six unchanged SHACL examples returned their expected outcomes. The three updated Agent/ownership diagrams rendered successfully and were visually inspected. Legal eligibility, date evaluation and completeness rules remain outside these checks.

## Controlled PROV-O import

On 23 November 2026 Bart approved the previously tested local PROV-O copy and requested that prov:wasRevisionOf and prov:specializationOf be retained as object properties. The central model imports the pinned core version, which supplies both object-property declarations; redundant local declarations were subsequently removed. Their original property axioms are supplied by the import, without copying global domain/range statements into the authored extension.

| Item | Value |
| --- | --- |
| Term namespace | `http://www.w3.org/ns/prov#` (`prov:`) |
| Imported ontology IRI recognised by Protégé | `http://www.w3.org/ns/prov#` |
| Published version recorded in the pinned source | `http://www.w3.org/ns/prov-o-20130430` |
| Catalogue | `model/catalog-v001.xml`, with a relative path to the corrected local file |
| Imported file | `imports/prov-o/prov-o-20130430.ttl` |
| Unchanged upstream snapshot | `imports/prov-o/prov-o-20130430.original.ttl` |
| Source | https://www.w3.org/ns/prov-o, retrieved on 20 November 2026 |
| Dependency metadata and checksums | `imports/manifest.json` |

The original file declares each of the two properties as both an annotation property and an object property. The original therefore fails the OWL 2 DL profile check. This [known source defect](https://lists.w3.org/Archives/Public/public-prov-comments/2017May/0000.html) is corrected locally by removing exactly these two triples:

```turtle
prov:wasRevisionOf rdf:type owl:AnnotationProperty .
prov:specializationOf rdf:type owl:AnnotationProperty .
```

Their object-property declarations, domain/range axioms, property hierarchies, chains and all other source triples remain unchanged. The original has 1,146 triples; the corrected copy has 1,144. The dependency checker verifies both file checksums and RDF graph equality after the two authorised removals. This is a documented local correction, not a claim that the W3C publication has changed. The original remains available as evidence and is not loaded for reasoning.

The source includes historical ontology-header declarations under both the PROV namespace and the PROV-O ontology IRI. In the observed Protégé session the earlier version-IRI import loaded the document under `http://www.w3.org/ns/prov#`, but its classes appeared only under **Show all loaded ontologies**, not under **Show the imports closure of the active ontology**. The active import now uses the loaded ontology identity `http://www.w3.org/ns/prov#`. Its catalogue target, file hash, source hash and exact two-triple correction remain unchanged; the manifest additionally verifies that the published version IRI is present in the source metadata. No further source-header correction is made. The OJA reference file prov.ttl bundles additional PROV modules and is not used as this dependency; the selected PROV-O core has no further imports.

The central model remains a single authored file. External snapshots under semantics/imports are separate dependencies. Protégé uses the catalogue when opening the model. The automated checks resolve the same mapping, verify the full direct/transitive dependency closure and pass explicit local mappings to OWLAPI. Missing mappings, unexpected ontology/version identities, checksum changes or broader edits to the corrected source fail the suite. The automated import loader does not fall back to network retrieval.

Authoring conventions apply to axioms written in the extension. Imported PROV-O axioms retain their original conventions, including global domains/ranges; these participate in reasoning. HermiT checks the complete imported combination for OWL 2 DL conformance, logical consistency and unsatisfiable named classes. The SHACL examples continue to be checked without additional inference or an ontology graph; importing PROV-O into the OWL model does not silently change that profile-validation setting. General PROV temporal/data constraints are not all enforced merely by loading PROV-O.

Importing PROV-O introduces no superclass, equivalence or property mapping between existing WEBUILD concepts and PROV concepts. In particular, the imported prov:Role and prov:Association remain distinct from ebwsm:Role and ebwsm:RoleFulfillment until mappings are individually agreed. At import time no Agent alignment was adopted either. The later direct-reuse decision above now uses prov:Agent as the actor class and adds Machine beneath it; it introduces no alignment with Dublin Core Agent or the published EBWV Agent. Use PROV properties only after reviewing their meanings and inferred domain/range effects. No new use-case obligation is introduced by this import.

Validation on 23 November 2026: all 39 checker/dependency regression tests, the 41-triple authored graph and complete pinned dependency resolution passed. HermiT checked the root and imported ontology together: OWL 2 DL conformance, consistency and no unsatisfiable named classes. All six SHACL examples returned their expected results. A temporary negative control made prov:Activity a subclass of prov:Entity and was correctly rejected because of the imported disjointness axiom; the active model was unchanged by that control.

After this import-identity correction on 23 November 2026, PROV classes including Agent, Activity, Entity and Role were visually confirmed in the same WEBUILD class tree with **Show the imports closure of the active ontology** selected. The suite passed all 44 regression tests, the 43-triple authored graph, both pinned imports, explicit direct-import resolution checks, OWL 2 DL/HermiT checks and all six expected SHACL results. No class hierarchy or definition was changed by this correction.

## Controlled Dublin Core class import

On 23 November 2026 Bart approved a controlled class-only Dublin Core module and reaffirmed the PROV-O correction for `prov:wasRevisionOf` and `prov:specializationOf` as object properties. The central model resolves both checksum-pinned dependencies through the same local catalogue. Dublin Core uses the derived module's version IRI; PROV-O uses its ontology identity recognised by Protégé as documented above. There is one working ontology, `model/webuild.ttl`; the dependency files are background sources, not extra modelling windows.

The module imports all 22 classes explicitly declared in the downloaded DCMI Terms schema, preserves their IRIs, labels, definition comments, descriptive notes and all eight class-to-class subclass relations. It includes `dcterms:PeriodOfTime rdfs:subClassOf dcterms:LocationPeriodOrJurisdiction`. It adds no alignment to PROV-O and does not change the adopted WEBUILD Agent, Role or RoleFulfillment definitions or their own superclass decisions.

This is explicitly a local OWL projection, with its own ontology/version IRI, not an official DCMI OWL distribution or a complete schema import. The original RDF metamodel statements `dcterms:Agent rdf:type dcterms:AgentClass` and `dcterms:AgentClass rdfs:subClassOf rdfs:Class` are excluded. The classes themselves remain available. Source property definitions, datatypes, encoding schemes and issuance metadata are also excluded. The full unmodified schema had failed the OWL 2 DL profile check in a separate trial; that finding was not a logical inconsistency result. See the [dependency record](imports/dcterms/README.md) for the preserved upstream snapshot, exact selection recipe, source limitations and reproduction command.

The catalogue resolves `https://w3id.org/ebwv/semantic-model/imports/dcterms-classes/2026-11-23` to `imports/dcterms/dcterms-classes-2026-11-23.ttl`. The dependency manifest pins both the source and derived file hashes. Validation reconstructs the approved projection and requires exact RDF graph equality, so updating a checksum alone cannot authorise a new hierarchy edge or other content. The full suite includes all three ontology documents in OWL 2 DL and HermiT checks.

Validation on 23 November 2026 after adding the class module: all 42 regression tests passed; the authored graph has 43 triples and both dependency documents resolve and verify locally. HermiT found the complete combination OWL 2 DL conformant and consistent, with no unsatisfiable named classes. All six SHACL examples returned their expected results. The PROV-O files and their exact approved two-triple correction were preserved. The earlier local `Reference_Documents/Import_Review` workspace is superseded for everyday modelling; no switching to it is needed.

## Removal of redundant imported declarations

On 23 November 2026 Bart requested review of the local declarations now that both imports display correctly. The working file no longer repeats the imported OWL class declarations of `dcterms:Agent` and `dcterms:PeriodOfTime`, the object-property declarations of `prov:wasRevisionOf` and `prov:specializationOf`, or the imported `rdfs:comment` definition of PeriodOfTime. The approved PROV-O correction remains in the imported dependency; removing the duplicate declarations does not undo it.

The local `skos:prefLabel "Period of time"@en-GB` and the term-specific `dcterms:source` link are retained on PeriodOfTime. These are WEBUILD annotations absent from the imports, rather than duplicate source declarations. The Dublin Core import supplies the original definition, class declaration and superclass relation.

Validation after cleanup: all 44 regression tests, OWL 2 DL/HermiT checks across all three ontology documents and all six expected SHACL results passed. The authored graph has 38 triples. An RDF graph-isomorphism comparison of the complete graph including imports before and after the removal confirmed that the effective 1,287-triple graph is unchanged.

## Object property modelling rule

For object properties, express class-specific conditions through OWL restrictions on the relevant classes. Do not attach global `rdfs:domain` or `rdfs:range` statements to those properties. In Protégé, record the restrictions in the relevant class descriptions and leave the object property's global Domains and Ranges empty.

This decision establishes where conditions are expressed. It does not prescribe a universal restriction or cardinality for every relation. Decide the appropriate restriction for each intended meaning; do not add existence or cardinality requirements merely because an object property is used by a class. Datatype properties follow the same class-level approach to applicability, while their ranges follow the separate rule below.

This rule governs axioms authored in the extension, including any authored statements about reused properties. Existing axioms from the upstream vocabulary are not rewritten by this rule. Archived originals and the existing implementation vocabulary remain unchanged.

## Central model and application profiles

The central model contains only restrictions that hold generally for the meaning of the relevant class or property, independently of a particular use case. Requirements that apply only within a specific use case, including mandatory relations or values and minimum or maximum counts, belong in that use case's application profile.

For example, an address may be mandatory for a particular application without requiring every organisation in the central model to have an address. This is an illustration of the separation, not a new class, property, or cardinality axiom.

This agreement does not prohibit cardinalities in the central model: include them there when they express a generally valid condition for the modelled concept. Do not promote a use-case-specific requirement into the central model merely because one implementation needs it. Reviewers must check the scope and justification of each restriction. Application profiles use SHACL in separate Turtle files under `semantics/application_profile`. Use `https://w3id.org/ebwv/profile/<profile-id>#` for named shapes, `ebwv:` for reused vocabulary terms and `ebwsm:` for new extension terms or candidates. pySHACL checks the example graphs without additional inference. Any profile-specific inference remains to be agreed. See the [application profile guide](application_profile/README.md).

## Datatype property modelling rule

A datatype property may have a global `rdfs:range`, such as `xsd:date`. Declaring a global range is optional and must reflect the intended meaning of the property across its uses. Describe the use of a datatype property in the relevant class through OWL restrictions; do not declare a global `rdfs:domain` on the property. In Protégé, leave the datatype property's global Domains empty. This is a class-level modelling convention, not an instruction to attach `rdfs:domain` statements to classes or a claim that class restrictions are semantically equivalent to global domain axioms. No datatype properties or range axioms have been added to the draft ontology by recording this decision.

## Term names and label language

Use readable American English terms for the local names of new extension term IRIs. Use British English for English labels, with the RDF language tag `en-GB`. For example, an illustrative new IRI `https://w3id.org/ebwv/semantic-model#Organization` would have the English label `"Organisation"@en-GB`. The IRI spelling and the label spelling deliberately differ. Preserve existing EBWV IRIs when reusing their meanings.

In `semantics/model/webuild.ttl`, use explicit prefixes: `ebwv:` for reused terms under `https://w3id.org/ebwv#`, and `ebwsm:` for new terms under `https://w3id.org/ebwv/semantic-model#`. Avoid the empty prefix.

These conventions apply to newly authored WEBUILD terms and labels. Preserve identifiers and original annotations in imported sources and archived material. Use `UpperCamelCase` for class local names and `lowerCamelCase` for property local names. For example, use `RegisteredOrganization` and `hasRegisteredAddress`. These are IRI naming conventions; they do not require CamelCase in human-readable labels. Use `skos:prefLabel` and `skos:altLabel` as specified below. The example illustrates naming only; it does not add an Organization class to the ontology or determine the spelling convention for all prose documentation.

## Preferred labels and synonyms

For each newly authored WEBUILD class or property, provide exactly one British English preferred label using `skos:prefLabel` with `en-GB`. Use zero or more `skos:altLabel` annotations for synonyms and alternative names of the same meaning, each with a language tag. Related but distinct meanings require separate terms rather than alternative labels.

For each term, allow at most one preferred label per language tag. Do not use the same literal, including its language tag, as both preferred and alternative label on that term. The automated quality checker enforces these structural label rules; spelling and whether alternative labels express the same meaning require human review.

Both properties are OWL annotation properties and can annotate OWL classes and properties directly. Their use does not require or imply `rdf:type skos:Concept`. The ontology declares these two reused annotation properties under their original SKOS IRIs; it does not import the complete SKOS ontology or add SKOS concept classifications. Separate duplicate `rdfs:label` annotations are not required by this convention.

Protégé is configured on this workstation to display `skos:prefLabel`, with the language preference field set to `en-GB, en, !` so British English has first priority. Both the Annotation Renderer and Preferences dialogs were confirmed during setup. The model now contains the preferred label for Agent; its display in Protégé has not yet been checked.

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

The optional legal and business definitions do not replace the mandatory taxonomic definition or, for a class or property without a meaningful superclass or superproperty respectively, its mandatory base definition. Use the three local OWL annotation properties listed below. Their IRIs use the extension namespace `https://w3id.org/ebwv/semantic-model#` (`ebwsm:`). The proposal to use a single `skos:definition` field has not been adopted.

| Annotation property | Use |
| --- | --- |
| `ebwsm:taxonomicDefinition` | Mandatory taxonomic definition; also holds the mandatory base definition for a class without a meaningful superclass or a property without a meaningful superproperty. |
| `ebwsm:legalDefinition` | Optional verbatim legal definition; a source reference is mandatory whenever a legal definition is provided, preferably as a URI. |
| `ebwsm:businessDefinition` | Optional definition in everyday language. |

In Protégé, add these annotations to the class or property being defined. The mandatory definition is an editorial requirement; declaring an annotation property does not enforce its presence. The automated quality checker verifies the presence of non-empty definition text; reviewers assess its meaning and taxonomic structure. No extra definition type or formal hierarchy is introduced by these declarations.

For both object and datatype properties, apply the following agreed rule:

- If a meaningful superproperty exists, the taxonomic definition names it and explains the distinguishing characteristic. Every relation asserted using the subproperty must also be a valid relation of the superproperty.
- If no meaningful superproperty exists, provide a mandatory base definition stating the relation, its direction, and the meaning of the related entities or value. Do not introduce an artificial superproperty solely to satisfy the definition format. The base definition is the fallback for the required definition, not an additional optional definition type.

For example, if `hasRegisteredAddress` is a subproperty of `hasAddress`, a definition can state: “Has registered address is a has-address relation in which the address is officially registered for the entity.” For a datatype property without a meaningful superproperty, a base definition can state: “Birth date is a relation between an entity and the date on which it was born.” These are illustrative examples only; no corresponding properties or hierarchy axioms have been added.

Record the definition as an annotation and the formal property hierarchy separately using `rdfs:subPropertyOf`. Definition text alone does not establish the formal hierarchy. Sharing a datatype alone does not justify a subproperty relationship. The existing rules for class-level applicability and global ranges remain unchanged.

Every legal definition must have a source reference identifying the relevant legislation or regulation and the specific article. Prefer a URI pointing to the official source and, where available, the specific article. The source reference is mandatory; use of a URI is a preference, not an absolute requirement when no suitable URI is available.

Use `dcterms:source` (`http://purl.org/dc/terms/source`) as an OWL annotation property on the specific `ebwsm:legalDefinition` annotation assertion. This associates the source with that definition text. A source annotation on the class or property alone does not establish which definition it supports. The ontology declares `dcterms:source` without importing the Dublin Core vocabulary.

In Protégé, add the legal definition to the entity, then annotate that definition assertion with `dcterms:source`. Enter the source as an IRI value when a suitable URI is available, rather than a text literal containing a URL. If several legal definitions exist for one term, attach the appropriate source to each definition separately. The automated quality checker verifies that every legal definition has a source on its exact annotation assertion. Reviewers verify the source and quotation.

The following Turtle illustrates the agreed pattern with the extension namespace, a fictional term, and a placeholder source URI.

```turtle
@prefix ebwsm: <https://w3id.org/ebwv/semantic-model#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .

ebwsm:legalDefinition a owl:AnnotationProperty .
dcterms:source a owl:AnnotationProperty .
ebwsm:ExampleTerm a owl:Class ;
    ebwsm:legalDefinition "Placeholder legal definition."@en-GB .

[] a owl:Axiom ;
    owl:annotatedSource ebwsm:ExampleTerm ;
    owl:annotatedProperty ebwsm:legalDefinition ;
    owl:annotatedTarget "Placeholder legal definition."@en-GB ;
    dcterms:source <https://example.org/legislation/example/article/1> .
```

The `owl:annotatedTarget` must match the definition literal exactly, including its language tag or datatype. When editing a definition, preserve or update its source annotation on the resulting assertion. This pattern uses the standard OWL axiom annotation representation; it does not introduce an intermediate domain class for definitions.

References: [Dublin Core source](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/source/) and [W3C OWL axiom annotations in RDF](https://www.w3.org/TR/owl2-mapping-to-rdf/#Axioms_that_Generate_a_Main_Triple).

Legal definitions must be literal quotations from the cited source. Preserve the source wording, including its spelling; do not paraphrase or silently rewrite the text to match the label spelling convention. Explanations in everyday language belong in `ebwsm:businessDefinition` and must not be presented as quotations from legislation. Each legal quotation retains its own required source reference as described above.

For a class without a meaningful named superclass, provide a mandatory base definition explaining what instances of the class are and what characterises them. Store it in `ebwsm:taxonomicDefinition`. Do not invent a superclass solely to satisfy the definition format. A superclass of `owl:Thing` alone does not supply an informative taxonomic definition. The base definition fulfils the mandatory definition requirement; it is not a fourth definition type. This editorial rule does not add or change formal class hierarchy axioms.

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

Use the [ontology pull request template](../.github/PULL_REQUEST_TEMPLATE/ontology.md) to record the quality evidence and both approvals. The local suite and GitHub workflow run HermiT after the structural and editorial checks. The automated check resolves the complete import closure from the local catalogue and dependency manifest, verifies pinned files and approved corrections, and checks all imported axioms with HermiT. Imports that are missing, unpinned or outside the catalogue fail the suite. Its status fails on logical findings and on incomplete checks, including models outside OWL 2 DL. GitHub enforcement of the scoped merge requirements and any profile-specific SHACL inference settings are still to be configured.

References: [W3C OWL 2 Primer on open-world semantics](https://www.w3.org/TR/owl2-primer/) and [W3C SHACL minimum-count constraints](https://www.w3.org/TR/shacl/#MinCountConstraintComponent).

## Use-case traceability outside the ontology

Maintain the links between classes or properties and their supporting use-case requirements in [USE_CASE_TRACEABILITY.md](USE_CASE_TRACEABILITY.md). Use the full term IRI, the project's use-case identifier, the source requirement or passage, and the reason the term is needed. Update the register alongside the related model change so reviewers can assess both together.

These links belong in repository documentation, not in ontology annotations or domain relations. Review use-case coverage and unresolved mappings through the register. No use-case links have been added to `model/webuild.ttl` by this decision.

## Quality checks before every GitHub synchronisation

The merge requirements apply when a pull request changes the active central ontology (currently `semantics/model/webuild.ttl`) or its imported dependency files under `semantics/imports`, the local catalogue, or files belonging to an application profile under `semantics/application_profile`, including its SHACL shapes and examples. A pull request with other changes as well is in scope as soon as it touches any of these areas. GitHub may still run the quality suite for unrelated changes, whose merges are outside this policy.

Record the reviewed revision with each approval. If the central ontology, an imported dependency, its resolution metadata or an application profile changes after approval, treat both approvals as expired. Run the applicable quality checks again and obtain fresh approval from both modellers for the revised content before merging into `main`. Changes confined to files outside the scope above do not trigger a new review under this rule.

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

The checks parse all `.ttl` files under `semantics/model` except `Archive` and `modelling_considerations`, and validate their combined graph. `webuild.ttl` must exist. Archived originals, `vocab`, and generated `docs/ebwv` are outside this extension graph's validation scope. A passing suite must not be represented as validation of the upstream EBWV vocabulary. Source URIs and import URLs are not fetched during validation; approved imports are resolved to pinned local files through the catalogue and manifest. Imported graphs are kept separate from the authored graph for editorial checks and are included in logical checks. The checker expects the extension ontology declaration for `https://w3id.org/ebwv/semantic-model`. Editorial checks cover new `ebwsm:` terms and any reused `ebwv:` terms annotated with extension definitions. Bare reused class declarations do not require replacing their original annotations. The checker rejects the obsolete EBWV IRIs for our three extension definition properties. Declarations in the EBWV namespace must be listed as reviewed reuse in `REVIEWED_EBWV_DECLARATIONS` in `semantics/quality/check.py` (currently Agent); new terms belong in `ebwsm:`. Add an existing term to that reviewed set only alongside its agreed model change and traceability record. Correct reuse of other EBWV IRIs remains a human review obligation against the pinned source.

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

Protégé can resolve local imports through a `catalog-v001.xml` file. Share such a catalogue only with reviewed, relative file paths. Do not automatically ignore catalogues: they may be needed to open the model correctly on another computer. Do not silently redirect a missing import to an ontology with a different IRI. The active PROV-O ontology identity, pinned version and exact approved correction, and the locally identified Dublin Core class projection, are documented in their respective controlled-import sections above. Confirm that dependency classes appear in the active import closure; a document being listed as loaded does not by itself establish that.

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
