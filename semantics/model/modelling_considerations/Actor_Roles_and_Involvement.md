# Actor roles and the General Authorisation Model

Decision and review date: 23 November 2026. Bart agreed to model Economic Operator and Public Sector Body as roles and authorised adding the supporting relations. This document records the implemented local draft and the separate review of Involvement. The other modeller's review of the resulting revision remains required before merging.

## Why these are roles in this model

The actor, its contextual capacity and its particular fulfilment of that capacity have different identities. A person or organisation continues to exist when a capacity ends. One actor can fulfil several capacities at the same time; one role can also have different players. A role may exist without a current fulfilment. A fulfilment can last for years and need not correspond to a single transaction.

The source used here is the Commission proposal [COM(2025) 838 final, 19 November 2025, Article 3(4) and (5)](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:52025PC0838). This is a version-specific modelling source, not an assertion that the proposal is adopted legislation or that later negotiating texts have identical definitions. The source's commercial/professional capacity wording informs EconomicOperator. PublicSectorBody needs an extra distinction: the definition includes institutional categories as well as private entities acting under a qualifying public mandate. Our role represents the legal capacity in its setting; an institution's underlying status is a separate matter. It would be wrong to require every public institution to have a temporary delegation.

The decision to use roles is our interpretation, not an ontology mandated by the proposal. The definitions in the ontology are taxonomic paraphrases of role meanings, not verbatim legal definitions of roles. No `legalDefinition` quotation is asserted.

In OWL a subclass of Agent would not, by itself, assert that membership is permanent. An actor class such as “Agents fulfilling an Economic Operator role” could coexist with the role class. It would have actors as instances, whereas our adopted class has roles as instances. We have not added such a derived actor class.

## Implemented ontology content

The authoritative model is [webuild.ttl](../webuild.ttl). New terms use `https://w3id.org/ebwv/semantic-model#` (`ebwsm:`).

| Term | Adopted meaning / formal consequence |
| --- | --- |
| `EconomicOperator` | Subclass of `Role`; instances are commercial or professional contextual roles. |
| `PublicSectorBody` | Subclass of `Role`; instances are contextual public-sector legal capacities. |
| `hasPlayer` | Links a fulfilment to its player. A generic player need not be an Agent. |
| `fulfillsRole` | Links a fulfilment to a particular role individual. Its object is not a role class IRI. |
| `hasPeriod` | Links a fulfilment to its continuous `dcterms:PeriodOfTime`. |
| `hasContext` | Links the role to context resources, for example an organisation, a legal framework or a mandate. No context cardinality or new Context class is imposed. |

`RoleFulfillment` has exactly one player, one role and one period. Separate all-values restrictions require the role to be a `Role` and the period to be a `dcterms:PeriodOfTime`. Exact unqualified cardinalities avoid accidentally permitting extra fillers outside a qualified class. No global domains, object-property ranges or globally functional properties are introduced.

For each of the two specialised roles an inverse `fulfillsRole` restriction requires every referring subject to be a RoleFulfillment whose players are `prov:Agent` instances (direct reuse adopted later on the same date). This is local to these roles. It does not turn the role into an Agent, require a role to have a current player, or make all generic role players Agents. No mapping of Role or RoleFulfillment to `prov:Role` or `prov:Association` is introduced. The player type uses `prov:Agent` directly, as explained in [the superseding Agent decision](Agents_and_Machines.md).

OWL cardinalities express existence and uniqueness in the interpretation. They do not require explicitly recorded triples. Two asserted fillers may denote the same individual unless their distinctness is established. There is no key, tuple-uniqueness axiom or automatic merging of separate fulfilment nodes. Continuity, interval boundaries, overlap, mandate validity and recorded-data completeness are not checked by these axioms. Any such SHACL or temporal rules need a separate decision.

The role classes are not declared disjoint. This permits one actor to fulfil both kinds of role when the applicable criteria are met; the ontology does not decide when that is legally permitted. Neither fulfilment establishes a representation right.

## Why the existing EBWV IRIs are not redefined

The existing vocabulary already contains `ebwv:EconomicOperator` and `ebwv:PublicSectorBody`, with actor-oriented descriptions. Its surrounding properties attach identifiers, contact information and representation relations to actors. Turning those existing IRIs into classes of role objects would change what existing data denotes. The reuse rule requires a distinct extension IRI for a different meaning.

The new classes therefore use `ebwsm:EconomicOperator` and `ebwsm:PublicSectorBody`, preserving the requested local names but with explicitly different namespace and instance semantics. No equivalence or subclass bridge to the existing actor terms is asserted. Upstream vocabulary files, profiles and identifiers have not been migrated. Any future mapping must specify how the actor is reached through a fulfilment and must respect context and time.

## Review of Involvement in the selected General Authorisation Model

The selected integration source is the local, Git-ignored `Reference_Documents/Authorisation.PlantUML`, SHA-256 `9c5066cf4c8e6af64cf2648cb7e6180b38134a4f6530e83a9f70679d43464931`. It is distinct from [the archived earlier diagram](../Archive/authorisation_part.PlantUML). Neither diagram is an imported ontology. Both are preserved as evidence.

The selected source has `Involvement.member`, `Involvement.hasRole`, `Involvement.inOrganisation` and `dct:temporal`. Its note explicitly allows `member` to be absent when a role and organisation select eligible holders. AssignmentRule counts distinct eligible actors at the time of action, rather than counting Involvement entries or roles.

There are two independent role levels:

1. A represented organisation or other qualifying actor fulfils an EconomicOperator or PublicSectorBody role in its legal setting.
2. A particular person or other eligible actor fulfils an internal role in the setting of that organisation. An authorisation rule can select that actor or select eligible holders of that internal role.

The organisation is the **player** of the EconomicOperator role. The same organisation can provide the **context** of the internal role. The internal role and the EconomicOperator role must not be collapsed into one role. The [synthetic example](../../examples/roles/actor-roles.ttl) records these two levels with separate fulfilments.

| Source element | Finding / required review |
| --- | --- |
| `Involvement.inOrganisation -> EconomicOperator` | Its target behaves as an actor. Changing that target to our role class would conflate context actor and role. A future relation must reach the actor, or explicitly reference that actor's qualifying fulfilment if capacity and validity are material. The name also needs review because an Economic Operator player can be a natural person or group. |
| `Role.inOrganisation -> EconomicOperator` | An internal role's context should refer to the setting actor. `hasContext` can express that setting without asserting that the organisation itself is a role. A legal framework remains the context of the EconomicOperator role. |
| `Involvement.member` | Identifies a selected actor when one is specified; it does not identify a role object. Person, Organization and SoftwareAgent are reused from PROV-O; Machine is now adopted as another Agent subtype in the [Agent decision](Agents_and_Machines.md). The source's Person/Machine alternatives are not an exhaustive actor partition, and its selector relationships still need integration review. |
| `Involvement.hasRole` | In role-based selection this denotes a contextual internal role. Its precise target, counts and relation to fulfilment evidence require review. |
| Member-less Involvement | Selects potentially several current or future actors. It is not a RoleFulfillment, which has one particular player. No subclass or equivalence between Involvement and RoleFulfillment is adopted. |
| Actual actor at action time | A selector must be resolved against applicable fulfilments and the action time. Neither a RoleFulfillment assertion alone nor a role-selection rule grants representation authority. |
| `Involvement.dct:temporal` | The validity period of an authorisation selector and a player's fulfilment period are separate concepts; they need not coincide. The action time must be checked against the applicable periods. |
| `legalName`, `registryNumber`, `EUID` on EconomicOperator | These describe or identify the actor in the source diagram. They must not be copied as mandatory properties of our role class. Whether an identifier identifies an actor, registration or something else requires its own review. |
| `PrivateEvaluationDefinition.evaluatedBy -> EconomicOperator` | The source expects an evaluator actor. A future mapping must not replace that actor by a role individual. Its qualification and the evidence for a private result require separate consideration. |

There is also a source inconsistency: `inOrganisation` is marked mandatory in the Involvement body, while its drawn target multiplicity is `0..1`. The selected source also discusses role-only selection, which cannot be expressed by simply equating Involvement with a concrete fulfilment. These are explicit review issues, not imported constraints.

No central `Involvement` class or its authorisation-rule relations are added by this decision. Resolving a selector, determining legal eligibility and checking authority remain future integration steps. A concrete role fulfilment can supply evidence for resolving a selection; it cannot replace the selection itself. The archived and selected diagrams and all existing application profiles remain unchanged.

## Subsequent consolidation

The general Role class remains separate from prov:Role; RoleFulfillment remains separate from prov:Association. Neither subclass/equivalence nor disjointness mappings are adopted. The imported activity-related qualification pattern does not replace the broader legal/economic and ownership relationship contexts.

The [current status](../../MODEL_STATUS.md) adds the distinction between an organisation, its LegalForm classification and Agents fulfilling EnterpriseOwner or Shareholder roles. These later additions do not resolve Involvement's selector semantics or make ownership sufficient authority to represent an enterprise. The [expanded ownership examples](../../examples/ownership/ownership.ttl) illustrate the role pattern without changing the selected or archived sources.

## Validation

For the initial role revision, before direct PROV Agent reuse, the full quality suite passed: 44 checker/dependency regression tests, the 114-triple authored graph, pinned import resolution, OWL 2 DL/HermiT consistency and named-class satisfiability, and all six expected SHACL outcomes. Thirteen HermiT semantic controls now run in the suite. They check that specialised-role fulfilments infer Agent players, generic role players remain unrestricted, roles may be unfulfilled, missing asserted fillers remain compatible with OWL's open world, and two explicitly different players cannot belong to one fulfilment. The synthetic example also passed OWL 2 DL and HermiT checks together with the complete imported model. Full results are recorded in the working guide; these are checks of the implemented pattern, not legal eligibility validation.

The later direct Agent reuse and Machine revision updates the player type and adds actor semantic controls. Current validation is recorded in [the working guide](../../PROTEGE_GITHUB.md#agent-modelling-decision).
