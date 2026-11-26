# Current semantic model decisions

Consolidated on 23 November 2026 from the discussion with Bart. This is the current local draft and distinguishes implemented meanings from open mappings. The [working guide](PROTEGE_GITHUB.md) records authoring conventions and historical validation. The [traceability register](USE_CASE_TRACEABILITY.md) records use-case rationale. Approval of the resulting revision by both modellers remains required before merging.

## Working ontology and dependencies

Open [model/webuild.ttl](model/webuild.ttl), ontology IRI `https://w3id.org/ebwv/semantic-model`, term namespace `https://w3id.org/ebwv/semantic-model#` (`ebwsm:`). Existing published EBWV IRIs retain their original namespace when reused; the full EBWV vocabulary is not imported.

The catalogue resolves the unchanged, checksum-pinned PROV-O core (2013-04-30, approved two-annotation correction) and Dublin Core class-only projection. Their original sources and exact transformations are recorded in [imports/manifest.json](imports/manifest.json). Importing them does not itself align their classes with WEBUILD classes. Archived models and the selected local General Authorisation Model remain source evidence rather than imported axioms.

## Agents and machines

- Reuse `prov:Agent` directly. No separate `ebwv:Agent` or `ebwsm:Agent` is defined in the active extension.
- Reuse imported `prov:Person`, `prov:Organization` and `prov:SoftwareAgent`. “Actor” in the discussion means Agent; it is not another class.
- `ebwsm:Machine` is the physical, software-controlled Agent subtype for autonomous execution of predetermined processes. A payment terminal and an autonomous robot such as Optimus motivated the category.
- `runsSoftwareAgent` can link hardware to a separately represented running software actor. It has no minimum count and does not identify hardware and software or infer delegation.
- The separate `dcterms:Agent` remains imported. No PROV/Dublin Core Agent alignment is asserted.
- Being an Agent or Machine is not a mandate, legal personhood or permission to act.

See [Agent decisions](model/modelling_considerations/Agents_and_Machines.md), the [Agent diagram](model/Agents.PlantUML) and [machine/software example](examples/agents/machine-software.ttl).

## Human actor, legal classification and legal form

`prov:Person` describes the human Agent. NaturalPerson is being discussed as the human's legal classification, rather than merely a different display name. The same human can be considered from both perspectives; this does not require two individual identities. No class equivalence, subclass or disjointness mapping to `ebwv:NaturalPerson` is adopted. LegalPerson is not a subclass of PROV Person.

The earlier local alternative label “Natural Person” on `prov:Person` is withdrawn in this consolidation. Its preferred label remains “Person”. The jurisdiction-specific legal meaning and mappings of NaturalPerson, LegalPerson and any common juridical superclass remain open. No duplicate legal-actor classes are introduced to resolve that question prematurely.

The expression “legal persons/legal subjects” used during the discussion was imprecise: those are not interchangeable categories. In the Dutch discussion distinguish *natuurlijk persoon*, *rechtspersoon*, *rechtssubject*, *rechtspersoonlijkheid* and *rechtsvorm*. Do not infer an OWL hierarchy from that wording alone.

`ebwsm:LegalForm` is now a class of classification values such as BV and sole proprietorship. It is disjoint with `prov:Agent`: the classification BV is not the concrete company Bink beheer BV. `hasLegalForm` links an organisation to such a value. Its target type is expressed by an all-values restriction on `prov:Organization`, not by a global range. There is no universal obligation to supply a legal form, no maximum count, and no inference from a form value to a local NaturalPerson/LegalPerson class. Code-list selection, jurisdiction, versioning and historical forms remain open.

An enterprise operated as a sole proprietorship can be represented organisationally without thereby making that organisation a natural person or granting it separate legal personality. Whether an organisational enterprise and a company/legal subject are separate individuals in a particular dataset depends on what each individual denotes; the diagram does not settle every entity-resolution question.

## Roles, fulfilment and PROV qualification

| Class | Scope |
| --- | --- |
| `prov:Role` | Function of an Entity or Agent with respect to an Activity, within a qualified provenance relation such as Usage, Generation or Association. |
| `ebwsm:Role` | A context-dependent capacity in an activity, event, relationship or situation, including legal/economic and ownership relationships. |
| `ebwsm:RoleFulfillment` | A particular entity fulfilling a particular contextual role during one continuous interval. |

No subclass, equivalence or disjointness mapping between the Role classes is asserted. The same applies to RoleFulfillment versus `prov:Association`. The direct reuse of PROV Agent does not change this boundary.

The role holds its setting through `hasContext`. A fulfilment has exactly one `hasPlayer`, one `fulfillsRole` and one `hasPeriod`, with the interval represented by `dcterms:PeriodOfTime`. These are OWL constraints, not requirements for explicitly supplied triples. Unknown dates, temporal evaluation, repeated fulfilments, identity/deduplication and profile completeness remain separate matters. Generic players need not be Agents.

The implemented role subclasses EconomicOperator, PublicSectorBody, EnterpriseOwner and Shareholder require Agent players through role-scoped inverse restrictions. This is necessary typing, not a complete legal eligibility rule. Roles need not have a current player and are not declared disjoint or exhaustive.

The first two role meanings are informed by the version-specific Commission proposal COM(2025) 838 final, Article 3(4) and (5). PublicSectorBody distinguishes contextual legal capacity from institutional status: not every public institution requires a temporary mandate. Their extension IRIs do not redefine the existing actor-oriented EBWV terms. See [the reasoning and Involvement review](model/modelling_considerations/Actor_Roles_and_Involvement.md).

## Enterprise ownership, shareholding and the two examples

An ownership role relates a player to the concrete enterprise or other specified subject matter, not to its legal-form value. The role's context points to the relevant enterprise/company in these examples. Its player may be a concrete organisation as well as a human, where the applicable legal requirements are met. “Only a BV may be an owner” is not a valid general eligibility rule: a concrete BV is a legal subject; BV as a classification cannot play the role.

- `EnterpriseOwner` means the party to whom the enterprise belongs in the applicable legal/registration setting. It is deliberately narrower than a universal Owner class for every organisation or asset.
- `Shareholder` means holding shares in the contextual company. It does not automatically give direct ownership of that company's assets or equate the holder with the party to whom the enterprise belongs.
- No subclass/equivalence/disjointness bridge between these role classes is asserted. They must be selected according to the relationship actually described.
- Do not assert that every organisation has an owner, or infer ownership of a public organisation from institutional status, membership, governance or representation.
- Apply future eligibility restrictions to the appropriate role/fulfilment classes. Keep generic `hasPlayer` open and do not use global domains/ranges to turn every Agent into an eligible owner.

The [simple PlantUML examples](examples/ownership/Organization_LegalForm_Ownership.PlantUML) abbreviate the role pattern on arrows. The [RDF example](examples/ownership/ownership.ttl) expands it into actual roles, fulfilments and periods:

| Example | Organisation | Legal form | Role players |
| --- | --- | --- | --- |
| Fietsenservice Jansen | Organisational enterprise | Sole proprietorship with multiple owners in an undivided estate | Two distinct sons, each with a co-owner/EnterpriseOwner fulfilment. No single-owner maximum is imposed. |
| Braindex | Organisation/company | BV | Bink beheer BV fulfils a Shareholder role towards Braindex. Bink beheer BV is also an organisation with the same legal-form value BV. |

These are Bart's conceptual examples, not verified real-world register statements. No dates, percentages, assets or undocumented family details are asserted.

The legal review found that Article 10 Handelsregisterwet distinguishes the enterprise from the party to whom it belongs, including a third category that is neither natural nor legal person. KVK explicitly supports a sole-proprietorship-with-multiple-owners case for an undivided estate after inheritance. Its ordinary one-owner guidance must not be made an exception-free axiom. Having employees is independent of that ownership count. This does not establish that every public organisation has an external owner.

Reviewed sources:

- [Handelsregisterwet 2007, Articles 5, 9, 10 and 12, national text supplied to EUR-Lex](https://eur-lex.europa.eu/legal-content/NL/TXT/PDF/?uri=NIM:202604833), snapshot bearing a June 2026 retrieval date, reviewed during this discussion on 23 November 2026.
- [BW Boek 2, Articles 1, 3, 5 and 175, national text supplied to EUR-Lex](https://eur-lex.europa.eu/legal-content/NL/TXT/PDF/?uri=CELEX:72019L1151NLD_202604827), snapshot bearing a 30 June 2026 retrieval date, reviewed during this discussion on 23 November 2026. These sources were reviewed for the cited distinctions, not to certify every subsequent legislative amendment.
- [Directive (EU) 2017/1132, consolidated text of 12 August 2022](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:02017L1132-20220812), Article 13, Article 13 octies and Annex II: concrete company forms and the persons involved are different concepts. [TFEU Article 54](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:12012E054) likewise distinguishes companies and natural persons for establishment rights.
- [KVK Gegevenscatalogus 3.0.4h, April 2022, page 9](https://production-site-nl.kvk.bloomreach.cloud/binaries/content/assets/kvkwebsite-nl/categorie/producten-bestellen/gegevenscatalogus.pdf#page=9), [KVK Form 12](https://www.kvk.nl/over-het-handelsregister/formulier-12-inschrijving-overige-functionarissen//) and [KVK API test scenarios](https://developers.kvk.nl/documentation/testing/swagger-vestigingen-api): the inherited co-ownership case.
- [KVK: sole-proprietorship staffing](https://www.kvk.nl/personeel/als-eenmanszaak-personeel-aannemen-dit-moet-je-weten/) and [KVK: extract contents](https://www.kvk.nl/producten-bestellen/wat-staat-er-op-een-uittreksel/): roles, enterprise, legal subject and staff must not be collapsed.

## Involvement remains an integration question

The selected General Authorisation Model permits an Involvement to identify an actor or select eligible holders of a role in an organisation. A selector can identify multiple current/future actors and is therefore not equated with one concrete RoleFulfillment. Its validity period also need not equal a player's fulfilment period.

There are two role levels: an organisation/other eligible actor can fulfil EconomicOperator or PublicSectorBody, and a person or other eligible actor can fulfil an internal role with that actor as context. An organisation's legal-form value is neither that actor nor its contextual role. The selected reference's mandatory/optional `inOrganisation` discrepancy remains recorded in the detailed review. Involvement, actor resolution, action-time checks and authorisation-rule migration are not silently adopted from the drawings.

## Used versus Usage

`prov:used` is the direct Activity-to-Entity property. `prov:Usage` is a qualified influence/event class. The imported property-chain axiom states:

```turtle
prov:used owl:propertyChainAxiom (prov:qualifiedUsage prov:entity) .
```

An Activity linked by qualifiedUsage to a Usage linked by entity to an Entity therefore entails the direct used relation. The reverse inference does not create a Usage individual. The `qualifiedForm`/`unqualifiedForm` annotations document the correspondence but are not that inference mechanism. The [full core diagram](model/PROV_O.PlantUML) omits property-chain axioms; the [pinned RDF source](imports/prov-o/prov-o-20130430.ttl) supplies them.

## Validation of this consolidation

The full suite passed on 23 November 2026: 45 checker/dependency regression tests, structural/editorial checks on the 180-triple authored graph, both unchanged checksum-pinned dependencies, OWL 2 DL conformance, consistency and no unsatisfiable named classes across the complete three-document model. All 37 actor/role HermiT controls passed, including co-ownership, classification-versus-Agent separation, legal-form target inference, ownership/shareholding separation and the absence of unapproved PROV Role/Association mappings. The same reasoner and controls also passed with all three synthetic RDF example graphs loaded together. All six unchanged SHACL examples returned their expected outcomes. The three updated Agent/ownership diagrams rendered successfully and were visually inspected. Legal eligibility, date evaluation and completeness rules remain outside these checks. Historic counts in the working guide remain evidence of earlier revisions, not the current graph size.
