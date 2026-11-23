# Direct PROV Agent reuse and physical machines

Decision date: 23 November 2026. Bart confirmed that every actor intended here fits PROV-O's responsibility-based Agent meaning, explicitly included software agents and requested a physical Machine subtype. He requested direct use of `prov:Agent` without a separate `ebwv:Agent` definition. This supersedes the 19 November local augmentation of the EBWV Agent class. The resulting draft still requires the other modeller's review before merging.

## Why direct reuse

The model now uses the exact imported `prov:Agent` IRI and source meaning. WEBUILD is the application setting rather than a reason to duplicate that class. The earlier narrower description of social/legal actors in business/legal processes is no longer the definition of our general Agent category. There is no new WEBUILD Agent class, alias class or equivalence axiom.

The [pinned PROV-O core](../../imports/prov-o/prov-o-20130430.ttl) already supplies Agent and its Person, Organization and SoftwareAgent subclasses. No duplicate declarations or replacement definitions are needed. Local British English preferred labels are presentation annotations only. In particular, the IRI stays `prov:Organization` while the preferred label is “Organisation”.

The [PROV-O SoftwareAgent definition](https://www.w3.org/TR/prov-o/#SoftwareAgent) describes running software. An installed program, source-code file or executable artifact is not automatically that running actor. The [Agent definition](https://www.w3.org/TR/prov-o/#Agent) concerns responsibility for activities, entities or other agents' activities; this does not by itself confer legal personhood or authority.

## Adopted hierarchy and physical/software distinction

### Person and the WEBUILD term Natural Person

Bart initially requested `"Natural Person"@en-GB` as a `skos:altLabel` of `prov:Person`. The subsequent legal-context discussion showed that he wants to distinguish the human actor from the legal classification. The alternative label is withdrawn in the consolidated revision of 23 November 2026. The preferred label stays “Person” and the imported IRI and definition are unchanged.

PROV Person denotes human Agents. A natural-person legal classification may describe that same human individual; distinguishing concepts does not establish different individual identities or disjoint classes. It also does not prove a global equivalence. LegalPerson must not be placed under PROV Person or treated as a legal-form code. The discussion's phrase “legal persons/legal subjects” was imprecise; Dutch *rechtspersoon* and *rechtssubject* are not synonyms. Any common juridical superclass and mappings to existing EBWV terms remain separately reviewable.

The [WEBUILD terminology draft](https://sanastot.suomi.fi/terminology/webuild/concept/concept-6005) inspected on 23 November lists person/individual as synonyms and Agent as broader concept. That is terminology evidence, not approval of an OWL equivalence or of a hierarchy with a broad juridical Person parent. The local generated vocabulary has NaturalPerson and LegalPerson under LegalEntity and CredentialSubject, but predates the pinned reuse baseline. Neither source is silently changed.

No local NaturalPerson or LegalPerson class, equivalence, subclass mapping, disjointness or profile constraint is added by this consolidation. See [the current legal-form and ownership conclusions](../../MODEL_STATUS.md#human-actor-legal-classification-and-legal-form).

### Actor hierarchy

```text
prov:Agent
  prov:Person          (imported; human Agent)
  prov:Organization    (imported)
  prov:SoftwareAgent   (imported)
  ebwsm:Machine        (new extension class)
```

Machine is a PROV agent embodied in physical hardware that can autonomously execute predetermined processes under software control. “Autonomous” means that execution can proceed without step-by-step human intervention. It does not require the device to choose its own goals, and it does not make every passive hardware component an Agent.

Bart's motivating examples are a payment terminal and an autonomous robot such as Optimus. These are examples of the intended physical-actor category, not assertions about a manufacturer's current capabilities or a particular product's legal status.

`ebwsm:runsSoftwareAgent` links the machine to a separately represented executing software actor. A class-level all-values restriction on Machine types every such object as `prov:SoftwareAgent`, from which PROV Agent membership follows. The relation does not identify hardware and software, assert delegation, or automatically associate either actor with a particular activity.

The link has no minimum or maximum count. Software-controlled operation is part of the Machine definition, but the model does not require a recorded SoftwareAgent link or imply that every piece of firmware is a responsible software actor. The physical character and execution capability are described in the definition, not automatically verified by the reasoner. No global domains/ranges, sibling-class disjointness, exhaustive partition, deployment-time model or generic software-asset class is introduced.

The [synthetic example](../../examples/agents/machine-software.ttl) distinguishes the physical terminal/robot and running controller with separate IRIs and explicit inequality. Its activity associations are explicitly asserted rather than inferred from hosting. Do not type hardware as SoftwareAgent merely because it runs software, or assume those two IRIs denote the same thing.

## Permission and role fulfilment

The word “may” in the motivating description concerns permitted operations. Agent or Machine membership alone does not grant permission. Applicable authorisations, roles and scope determine which operations are allowed; that mechanism is not invented by the machine class or software link.

The EconomicOperator and PublicSectorBody role restrictions now require `prov:Agent` players. Generic RoleFulfillment remains open to non-Agent players. An Agent type, including SoftwareAgent or Machine, does not automatically establish the legal criteria for either economic/public-sector role. A robot or controller can be considered for an operational role without thereby becoming a legal person, Economic Operator or Public Sector Body. Current SHACL profiles remain unchanged.

The [Involvement review](Actor_Roles_and_Involvement.md) now accepts machines and software within the general actor scope. The selected reference's Person/Machine alternatives do not become an exhaustive partition: its selector semantics, target relations and time checks still require their own integration decision.

## Migration and compatibility boundary

- Remove the local declaration, definition and Dublin Core superclass axiom for `ebwv:Agent` from `webuild.ttl`.
- Use `prov:Agent` in the new role-player restrictions and their reasoning controls. Update synthetic role examples to the imported Person/Organization types.
- Leave the separately published EBWV vocabulary and archived source files unchanged. This local migration does not deprecate the external EBWV IRI or claim it is equivalent to PROV Agent.
- Keep imported `dcterms:Agent` available as a separate dependency class. Do not assert a global subclass/equivalence between the PROV and Dublin Core Agent classes. Previous local data's inference to Dublin Core Agent therefore no longer follows merely from the actor type.
- Reject reintroduction of the former Agent IRI in active authored triples through the quality checker. Reviewed reuse of other EBWV terms remains a separate mechanism.

The existing PROV-O disjointness between Agent and InstantaneousEvent now applies directly to role players and machines through these axioms. It does not make Agent and Entity disjoint. The dependency snapshot and its approved correction are unchanged.

## Validation history

The full suite passed: 45 checker/dependency regression tests, structural/editorial checks on the 125-triple authored graph, unchanged pinned dependency verification, complete-import OWL 2 DL/HermiT consistency and named-class satisfiability, 20 actor/role HermiT semantic controls, and all six unchanged SHACL outcomes. Both synthetic examples were also combined with the model and passed OWL 2 DL, consistency and satisfiability checks. Controls specifically cover SoftwareAgent/Machine inference to PROV Agent, Machine software targets, explicit hardware/software inequality, optional software links, inherited Agent/event disjointness and absence of a global Dublin Core Agent alignment. The quality checker rejects the old EBWV Agent in active authored triples. The new Agent hierarchy diagram and corrected PROV core diagram rendered successfully.

For the subsequent Natural Person naming revision, the same 45 regression tests, 20 HermiT controls and six SHACL examples passed on the 127-triple authored graph. Graph comparison confirmed exactly two new annotation triples and unchanged logical axioms. The Agent diagram was updated and visually verified.

The Natural Person label revision above is historical and superseded. The current naming choice and latest validation are recorded in [MODEL_STATUS.md](../../MODEL_STATUS.md).
