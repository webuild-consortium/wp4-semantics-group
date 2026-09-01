# Candidate Sources for a WEBUILD Action Hierarchy

**Date:** 1 September 2026\
**Context:** Research into existing standards, ontologies, industry
vocabularies and legal models that could provide or inform the `Action`
Restriction hierarchy used by the WEBUILD Authorisation model.

## 1. Executive summary

WEBUILD needs an Action hierarchy whose hierarchy edges can safely
support the authorisation rule:

``` text
required ⊆ granted
```

For Actions this means that, if:

``` text
SpecificAction ⊆ BroaderAction
```

then authority granted for the broader Action covers a requirement for
the more specific Action.

The research found **no single existing vocabulary that should be
adopted wholesale** as the WEBUILD Action hierarchy. However, several
mature standards provide strong reusable material.

The most important finding is **W3C ODRL 2.2**. ODRL already defines an
explicit transitive relation, `odrl:includedIn`, for stating that the
operational semantics of one Action are encompassed by another Action.
This is considerably stronger and more suitable for authorisation
reasoning than treating generic `skos:broader` as subsumption.

Other important candidates are:

-   **LKIF-Core / ESTRELLA** for legal and ontological Action concepts;
-   **Schema.org Actions** as a large source of candidate verbs and
    specialization structures;
-   **UN/CEFACT** for authoritative business, trade, regulatory and
    government-domain Actions;
-   **OAGIS** for its explicit separation of `Verb` (Action) and `Noun`
    (Object);
-   **corporate Delegation-of-Authority (DoA) schemes** as an accidental
    but highly relevant source of recurring legally consequential
    Actions;
-   **ELI / Akoma Ntoso and related legal vocabularies** for specialist
    legal-action branches;
-   **RPaM** as a small seed vocabulary directly connected to powers and
    mandates.

The likely WEBUILD solution is therefore:

> **A small, governed upper Action hierarchy with explicit subset
> semantics, extended by independently governed domain-specific
> branches.**

------------------------------------------------------------------------

# 2. WEBUILD requirement

WEBUILD currently models Power limitations through extensible
`Restriction` dimensions such as:

``` text
Restriction
│
├── Action
├── Region
├── NACE
├── Organisation
└── restricted value range
```

The general evaluation rule is:

``` text
SATISFIES(G,R) ⇔ ⟦R⟧ ⊆ ⟦G⟧
```

For an Action hierarchy, this means a hierarchy edge must justify actual
semantic containment.

For example:

``` text
SignPurchaseContract
    ⊆
SignContract
```

would mean:

> Every act that counts as `SignPurchaseContract` also counts as
> `SignContract`.

Therefore:

``` text
Granted:
    Action = SignContract

Required:
    Action = SignPurchaseContract
```

satisfies the requirement.

The reverse does not.

This is stronger than saying that two concepts are merely related,
associated, grouped together, or placed in the same taxonomy branch.

------------------------------------------------------------------------

# 3. Evaluation criterion for candidate hierarchies

Every proposed Action hierarchy edge should pass this test:

> **Does every instance of the child Action necessarily constitute an
> instance of the parent Action?**

Equivalently:

``` text
ChildAction ⊆ ParentAction
```

If the answer is not clearly yes, the relation should not be used for
automated `SATISFIES` reasoning.

This distinguishes:

### Valid specialization

``` text
SubmitTaxDeclaration
    ⊆
SubmitDeclaration
    ⊆
Submit
```

from relationships such as:

### Composition

``` text
ManagingDirectorPower
    entails SignContract
```

### Means / method

``` text
SignContract
    may realise EnterIntoAgreement
```

### Context

``` text
SubmitApplication
    occurs in StartingBusiness
```

### Object relationship

``` text
Sign
    acts upon Contract
```

Only genuine specialization/containment belongs in the Action hierarchy
used by the subset algorithm.

------------------------------------------------------------------------

# 4. W3C ODRL 2.2

## 4.1 Why ODRL is particularly important

ODRL --- the **Open Digital Rights Language** --- is a W3C
Recommendation for expressing permissions, prohibitions, duties and
constraints.

It has a first-class concept:

``` text
odrl:Action
```

More importantly, ODRL defines:

``` text
odrl:includedIn
```

for relationships between Actions.

The intended semantics are that the operational semantics of one Action
are included within an encompassing Action.

The relation is transitive.

Conceptually:

``` text
Specific Action
      │
      │ includedIn
      ▼
Broader Action
```

This is very close to the WEBUILD requirement:

``` text
SpecificAction ⊆ BroaderAction
```

## 4.2 Why this is better than generic SKOS

SKOS gives generic knowledge-organisation relations such as:

``` text
skos:broader
skos:narrower
```

Those relations do not by themselves assert that the extension of one
Action is a subset of another.

ODRL's `includedIn` is explicitly about Action semantics.

For WEBUILD, the ODRL pattern could therefore inspire something like:

``` text
SignPurchaseContract
    actionIncludedIn SignContract .

SignContract
    actionIncludedIn PerformContractualAct .
```

with transitivity:

``` text
SignPurchaseContract
    actionIncludedIn PerformContractualAct .
```

## 4.3 ODRL also distinguishes implication

ODRL has a separate concept:

``` text
odrl:implies
```

This is useful because WEBUILD also needs to keep two relationships
apart:

``` text
SPECIALIZATION

SignPurchaseContract
    includedIn
SignContract
```

versus:

``` text
ENTAILMENT / COMPOSITION

ManagingDirectorRepresentationPower
    entails
SignContract
```

ODRL therefore provides useful precedent for **not conflating inclusion
with implication**.

## 4.4 ODRL Action vocabulary

ODRL contains Actions such as:

``` text
Action
├── use
│   ├── aggregate
│   ├── annotate
│   ├── anonymize
│   ├── archive
│   ├── distribute
│   ├── execute
│   ├── index
│   ├── install
│   ├── modify
│   ├── move
│   ├── present
│   ├── read
│   ├── reproduce
│   ├── transform
│   └── translate
│
└── transfer
    ├── give
    └── ...
```

Other useful concepts include actions such as:

``` text
pay
sell
inform
obtainConsent
grantUse
```

## 4.5 Reuse assessment

**Formal pattern: VERY HIGH**

**Actual Action vocabulary: MEDIUM**

The vocabulary is primarily designed for rights over digital/content
assets. WEBUILD should therefore consider reusing or aligning with the
**Action inclusion semantics**, not adopting the entire ODRL Action list
as its legal-representation vocabulary.

### Recommended investigation

Determine whether WEBUILD can:

1.  reuse `odrl:Action`;
2.  reuse `odrl:includedIn` directly; or
3.  define a WEBUILD relation with equivalent subset semantics and map
    it to ODRL where appropriate.

Primary sources:

-   W3C ODRL Information Model 2.2\
    https://www.w3.org/TR/odrl-model/
-   W3C ODRL Vocabulary & Expression 2.2\
    https://www.w3.org/TR/odrl-vocab/

------------------------------------------------------------------------

# 5. LKIF-Core / ESTRELLA

## 5.1 Background

LKIF-Core was developed in the European **ESTRELLA** legal knowledge
project.

It is an ontology of foundational legal concepts intended to support
legal knowledge representation and reasoning.

This makes it particularly relevant to WEBUILD because it is not merely
a generic web vocabulary.

## 5.2 Action ontology

LKIF models Actions as intentional processes performed by agents.

Its modules include concepts related to:

``` text
Action
Process
Legal Action
Legal Role
Norm
```

The legal-action module contains concepts such as:

``` text
Public Act
Act of Law
Assignment
Delegation
Mandate
Decision
Legal Speech Act
```

Notably, LKIF therefore already treats concepts such as **Mandate** and
**Delegation** as legal Actions.

## 5.3 Relevance to WEBUILD

LKIF is useful for answering questions such as:

-   What is an Action?
-   What distinguishes an Action from a Process?
-   What is a Legal Action?
-   Is Delegation an Action?
-   Is a Decision an Action?
-   Is a Mandate itself a legal act?
-   How do legal speech acts relate to other acts?

This could provide the **ontological upper structure** of a WEBUILD
Action hierarchy.

## 5.4 Limitation

LKIF is not a comprehensive vocabulary of operational representation
actions.

It does not appear to provide the depth WEBUILD ultimately needs, such
as:

``` text
Submit
└── SubmitDeclaration
    ├── SubmitTaxDeclaration
    └── SubmitCorporateDeclaration
```

or:

``` text
EnterIntoAgreement
└── EnterIntoCommercialAgreement
    └── EnterIntoPurchaseAgreement
```

## 5.5 Reuse assessment

**Legal upper ontology: HIGH**

**Operational Action vocabulary: LOW--MEDIUM**

LKIF should be mined for legally meaningful upper classes and for
distinctions that prevent WEBUILD from making ontologically incorrect
hierarchy edges.

Sources:

-   LKIF-Core repository\
    https://github.com/RinkeHoekstra/lkif-core
-   Action module\
    https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/action.ttl
-   Legal Action module\
    https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/legal-action.ttl

------------------------------------------------------------------------

# 6. Schema.org Actions

Schema.org contains a surprisingly extensive hierarchy beneath:

``` text
schema:Action
```

Examples include:

``` text
Action
├── AchieveAction
├── AssessAction
│   └── ChooseAction
│       └── VoteAction
├── CommunicateAction
├── ControlAction
├── CreateAction
├── FindAction
├── InteractAction
├── MoveAction
├── OrganizeAction
├── PlayAction
├── SearchAction
├── TradeAction
├── TransferAction
└── UpdateAction
```

Because these are classes and subclasses, Schema.org provides
considerably more structure than the shallow RPaM Action taxonomy.

## Reuse assessment

**Vocabulary mining: HIGH**

**Normative legal-authorisation hierarchy: MEDIUM--LOW**

Schema.org's purpose is describing things and activities on the Web, not
determining legal representation authority.

Its hierarchy is nevertheless valuable for:

-   discovering Action terminology;
-   finding synonyms;
-   identifying possible upper categories;
-   comparing independent classification decisions.

It should be treated as **evidence/source material**, not automatically
as the normative WEBUILD hierarchy.

Source:

https://schema.org/docs/full.html

------------------------------------------------------------------------

# 7. UN/CEFACT

## 7.1 Why UN/CEFACT matters

UN/CEFACT standardises semantic material for:

-   trade;
-   transport;
-   finance;
-   regulation;
-   conformity;
-   government/business exchanges.

This overlaps strongly with many business-wallet and representation
scenarios.

## 7.2 Action vocabularies

UN/CEFACT includes domain-specific Action lists.

Examples found in government-related material include:

``` text
Clearance
Detention
Fumigation
Inspection
Security
Means of transport admittance
Cargo hold inspection
Container inspection
Cargo packaging inspection
```

These can suggest possible specializations such as:

``` text
Inspection
├── CargoHoldInspection
├── ContainerInspection
└── CargoPackagingInspection
```

However, each proposed hierarchy edge still needs semantic verification.

## 7.3 Reuse assessment

**Domain-specific branches: HIGH**

**Universal upper hierarchy: LOW**

UN/CEFACT may be particularly valuable when WEBUILD needs authoritative
branches for:

``` text
trade
customs
transport
regulatory procedures
conformity
```

The competent international domain standard can then govern those
concepts rather than WEBUILD inventing them.

Sources:

-   UN/CEFACT Web Vocabulary\
    https://vocab.unece.org/
-   UN/CEFACT standards and vocabularies should be reviewed
    branch-by-branch for reusable Action concepts.

------------------------------------------------------------------------

# 8. OAGIS

OAGIS provides an important architectural precedent.

Its Business Object Document model explicitly separates:

``` text
Verb + Noun
```

where:

``` text
Verb = Action
Noun = Object
```

Examples of OAGIS verbs include:

``` text
Acknowledge
Cancel
Change
Confirm
Get
Load
Notify
Post
Process
Show
Sync
```

This strongly supports WEBUILD's decision not to encode every
Action/Object combination as one Power code.

For example:

``` text
Action = Cancel
Object = PurchaseOrder
```

is preferable to creating an atomic concept:

``` text
CancelPurchaseOrderPower
```

unless legislation genuinely defines such a named Power.

## Reuse assessment

**Architectural pattern: HIGH**

**Hierarchy: LOW**

**Business Action vocabulary: MEDIUM--HIGH**

OAGIS is therefore more useful as a source of Action terminology and
evidence for compositional modelling than as a ready-made specialization
hierarchy.

Sources:

-   OAGIS architecture documentation\
    https://docs.huihoo.com/oagis/9.2/Documentation/Architecture.html
-   OAGIS verbs\
    https://www.oagidocs.org/docs/verbs

------------------------------------------------------------------------

# 9. Corporate Delegation-of-Authority schemes

This may be one of the most practically valuable sources even though it
is not normally published as an ontology.

Corporate and public-sector Delegation-of-Authority schemes repeatedly
distinguish actions such as:

``` text
Initiate
Prepare
Recommend
Review
Clear
Approve
Sign
Execute
Commit
Authorize
Consent
Delegate
Notify
```

Other recurring legally consequential actions include:

``` text
Acquire
Dispose
Borrow
Lend
Guarantee
Appoint
Dismiss
Settle
Waive
Terminate
File
Declare
Represent
```

These are much closer to Powers of Representation than many of the
Actions in RPaM.

RPaM concentrates heavily on citizen/service interactions:

``` text
Apply
Buy
Claim
Notify
Obtain
Pay
Register
Request
Submit
```

Corporate PoR and signatory-right systems need Actions concerned with
**creating obligations and exercising organisational authority**.

Examples include:

``` text
Approve
Sign
Execute
Commit
EnterIntoAgreement
TerminateAgreement
Acquire
Dispose
Borrow
Guarantee
Delegate
Represent
Appoint
Dismiss
Settle
Waive
```

## Important research opportunity

A systematic comparison of Delegation-of-Authority matrices from:

-   corporations;
-   international organisations;
-   universities;
-   public authorities;
-   financial institutions;

could reveal a stable de facto Action vocabulary.

This would effectively be an **accidentally standardised legal/business
Action vocabulary**.

## Reuse assessment

**Requirements evidence: VERY HIGH**

**Existing formal hierarchy: LOW**

**Potential basis for WEBUILD core Actions: VERY HIGH**

The next step should be empirical extraction and normalization rather
than selecting a single DoA scheme as normative.

------------------------------------------------------------------------

# 10. ELI, Akoma Ntoso and legal-document vocabularies

Legal and legislative standards provide specialist Actions such as:

``` text
Amend
Repeal
Correct
Commence
Change
```

These are not a general mandate Action hierarchy, but they demonstrate
how specialist branches can be governed externally.

A possible legal-resource branch could eventually resemble:

``` text
ModifyLegalResource
├── Amend
├── Repeal
└── Correct
```

provided the hierarchy semantics are verified.

This supports a general WEBUILD principle:

> WEBUILD should not centrally own every specialist Action branch.

The appropriate legal or industry authority can maintain a branch that
aligns to the WEBUILD Action model.

Sources:

-   European Legislation Identifier material
-   Akoma Ntoso OASIS standard\
    https://www.oasis-open.org/standard/akn-v1-0/

------------------------------------------------------------------------

# 11. RPaM

RPaM remains relevant because it is directly about representation powers
and mandates.

Its Action vocabulary contains:

``` text
Action
├── Apply
├── Buy
├── Claim
├── Notify
├── Obtain
├── Pay
├── Register
├── Request
└── Submit
```

The main weaknesses are:

1.  it is very shallow;
2.  several definitions are incomplete;
3.  the published TTL contains case-sensitive IRI inconsistencies;
4.  it is heavily oriented toward public-service interactions;
5.  it lacks the corporate/legal Actions required for broad
    representation authority.

## Reuse assessment

**Direct domain relevance: HIGH**

**Actual hierarchy quality: LOW**

**Seed vocabulary: MEDIUM**

The terms should be included in the comparison exercise, but RPaM should
not be the foundation of the WEBUILD hierarchy.

------------------------------------------------------------------------

# 12. Emerging Action Mandate work

Recent work on machine-readable Action Mandates also points toward a
domain-extensible architecture rather than one universal global Action
taxonomy.

This is consistent with the WEBUILD direction:

``` text
small common semantic model
        +
governed domain Action vocabularies
```

rather than:

``` text
one enormous centrally maintained
European Powers/Actions taxonomy
```

This emerging work should be monitored, especially where it defines
formal semantics for Actions, targets, constraints, delegation and
authority.

------------------------------------------------------------------------

# 13. Candidate source comparison

  ---------------------------------------------------------------------------------------------
  Source               Formal Action        Legal     Business Subset semantics Best use
                           hierarchy    relevance    relevance                  
  ---------------- ----------------- ------------ ------------ ---------------- ---------------
  **W3C ODRL**                   Yes       Medium       Medium     **Explicit** Formal
                                                                                inclusion model

  **LKIF-Core**                  Yes       **Very       Medium              OWL Legal upper
                                           high**                specialization ontology

  **Schema.org**           **Large**          Low       Medium         subclass Vocabulary
                                                                                mining

  **UN/CEFACT**      Domain-specific       Medium       **Very           varies Governed domain
                                                        high**                  branches

  **OAGIS**                  Limited          Low       **Very          limited Action/Object
                                                        high**                  separation +
                                                                                verbs

  **Corporate       Usually implicit     **High**       **Very          usually Discover core
  DoA**                                                 high**     undocumented PoR Actions

  **ELI / Akoma           Specialist       **Very          Low           varies Specialist
  Ntoso**                                  high**                               legal branches

  **RPaM**              Very shallow     **High**       Medium        SKOS only Seed terms

  **Emerging          Domain-profile         High         High         evolving Monitor /
  Action Mandate            approach                                            alignment
  work**                                                                        
  ---------------------------------------------------------------------------------------------

------------------------------------------------------------------------

# 14. Candidate WEBUILD upper Action hierarchy

The following is **not yet a proposed normative hierarchy**. It is a
research scaffold derived from recurring concepts across the sources.

``` text
Action
│
├── Communicate
│   ├── Notify
│   ├── Declare
│   ├── Report
│   └── Inform
│
├── Request
│   ├── Apply
│   ├── Claim
│   └── RequestApproval
│
├── Decide
│   ├── Approve
│   ├── Reject
│   ├── Consent
│   └── Waive
│
├── Commit
│   ├── EnterIntoAgreement
│   ├── Guarantee
│   └── Bind
│
├── Transfer
│   ├── Sell
│   ├── Give
│   ├── Assign
│   └── Dispose
│
├── Acquire
│   ├── Buy
│   └── Borrow
│
├── Submit
│   ├── File
│   ├── Register
│   └── Lodge
│
├── Modify
│   ├── Amend
│   ├── Terminate
│   ├── Revoke
│   └── Cancel
│
├── Represent
│   ├── RepresentBeforeAuthority
│   └── RepresentInProceedings
│
├── Appoint
│
├── Dismiss
│
├── Pay
│
└── Delegate
```

Every edge in this scaffold still needs validation.

For example:

``` text
SignContract
    ?⊆
EnterIntoAgreement
```

is not automatically valid.

Signing a contract can be a method, evidence, formalisation or
completion of entering into an agreement depending on legal context.

Therefore:

``` text
SignContract
    realizes EnterIntoAgreement
```

might sometimes be more accurate than:

``` text
SignContract
    specializes EnterIntoAgreement
```

This distinction is critical because WEBUILD intends to assign
authorization consequences to the hierarchy.

------------------------------------------------------------------------

# 15. Proposed governance architecture

The research points toward a federated hierarchy.

``` text
WEBUILD Action
│
├── small common upper vocabulary
│
├── legal/governance branch
│
├── corporate authority branch
│
├── trade branch
│       governed/aligned with UN/CEFACT
│
├── procurement branch
│
├── tax branch
│
├── social-security branch
│
└── other managed extensions
```

The core should define the semantics of Action inclusion.

A managed extension would then be able to assert:

``` text
Tax:SubmitVATReturn
    actionIncludedIn
Core:SubmitDeclaration
```

provided the responsible authority can stand behind that semantic
assertion.

The Action vocabulary therefore becomes **federated but interoperable**.

------------------------------------------------------------------------

# 16. Strong candidate: ODRL-style `includedIn`

A particularly important design question is whether WEBUILD should adopt
or align to:

``` text
odrl:includedIn
```

rather than using:

``` text
skos:broader
```

for authorization-significant Action hierarchy edges.

Conceptually:

``` text
SubmitVATReturn
       │
       │ includedIn
       ▼
SubmitTaxDeclaration
       │
       │ includedIn
       ▼
SubmitDeclaration
       │
       │ includedIn
       ▼
Submit
```

would give:

``` text
SubmitVATReturn
    ⊆ SubmitTaxDeclaration
    ⊆ SubmitDeclaration
    ⊆ Submit
```

This makes the semantics needed by WEBUILD explicit.

SKOS relationships can still coexist for navigation and vocabulary
management:

``` text
skos:broader
```

but the authorization engine should depend on the stronger semantic
relation.

------------------------------------------------------------------------

# 17. Recommended next research step

The next step should not yet be to design the hierarchy manually.

Instead, build an evidence table from:

1.  RPaM;
2.  ODRL;
3.  LKIF-Core;
4.  Schema.org;
5.  UN/CEFACT;
6.  OAGIS;
7.  representative corporate/public Delegation-of-Authority schemes;
8.  European legal vocabularies;
9.  emerging Action Mandate specifications.

For every Action term record:

``` text
Action
Source
Definition
Parent proposed by source
Synonyms
Domain
Legal significance
Candidate WEBUILD parent
Subset relation verified?
Question / issue
```

Then apply one decisive test to every proposed hierarchy edge:

> **If a person is granted authority to perform the parent Action, does
> that necessarily include authority to perform the child Action,
> assuming all other Restrictions are equal?**

If yes:

``` text
child ⊆ parent
```

is a candidate authorization-significant hierarchy edge.

If no or uncertain, the relation must instead be represented as
something else:

``` text
entails
realizes
uses
concerns
hasObject
occursInContext
relatedTo
```

or left unresolved.

------------------------------------------------------------------------

# 18. Conclusion

There is no obvious existing universal legal Action taxonomy that
WEBUILD can simply adopt.

There is, however, substantial prior standardisation that can be
combined.

The strongest findings are:

1.  **ODRL provides the strongest existing formal precedent for Action
    subset semantics.**
2.  **LKIF provides the strongest legal ontological foundation.**
3.  **Corporate Delegation-of-Authority schemes may provide the most
    relevant empirical vocabulary for Powers of Representation.**
4.  **UN/CEFACT can provide authoritative domain-specific business/trade
    branches.**
5.  **OAGIS strongly supports separating Action from Object.**
6.  **Schema.org provides a large independent Action hierarchy useful
    for terminology mining.**
7.  **RPaM remains useful as direct domain evidence but is insufficient
    as the hierarchy itself.**
8.  **Specialist legal standards can govern specialist branches rather
    than forcing WEBUILD to own all Action concepts.**

The emerging architecture is therefore:

``` text
                 Action
                   │
          common upper hierarchy
                   │
        ┌──────────┼───────────┐
        │          │           │
      Legal      Trade      Corporate
        │          │           │
   specialist   UN/CEFACT     DoA
   authorities   etc.        vocabularies
        │          │           │
        └──────────┴───────────┘
                   │
          explicit inclusion
              semantics
                   │
                   ▼
          required ⊆ granted
```

The goal should not be a large centrally invented WEBUILD Action
taxonomy. The goal should be a **small semantically rigorous core, an
explicit transitive Action-inclusion relation, and a mechanism for
authoritative domain vocabularies to extend that hierarchy safely**.
