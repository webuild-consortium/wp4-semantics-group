# WEBUILD Mandate Authorisation: Findings on Power Requirements and Automated Evaluation

**Date:** 1 September 2026\
**Context:** Review of SEMPER, ISA² Representation of Powers and
Mandates (RPaM), and implications for the WEBUILD Authorisation model.

## 1. Executive summary

The investigation started with SEMPER (Cross-border Semantic
Interoperability of Powers and Mandates) and the question of what
mandate information was exchanged across borders. SEMPER appears
primarily to provide a cross-border **powers-validation mechanism**,
building on earlier semantic work rather than defining the richest
reusable mandate domain model itself.

The preceding ISA² Action 2016.12, **Semantic interoperability for
representation powers and mandates**, produced the **Representation of
Powers and Mandates (RPaM) Ontology**, including an OWL/Turtle ontology,
conceptual model, business rules, eAuthorisation Criteria, Power Use
Constraints, and an EU Powers Taxonomy in SKOS/SKOS-XL.

RPaM is valuable prior art, but several concerns arise for WEBUILD:

1.  RPaM does not consistently provide the clean separation now
    desirable between:
    -   mandate/power payload;
    -   attestation, evidence, trust and lifecycle metadata;
    -   relying-party authorisation requirements and policy.
2.  A monolithic Powers Taxonomy risks mixing semantic dimensions and
    governance responsibilities.
3.  `skos:broader` / `skos:narrower` cannot safely be interpreted as
    authorisation subsumption unless the compared concepts belong to the
    **same semantic dimension** and the hierarchy has suitable normative
    semantics.
4.  The current WEBUILD Authorisation model already has a more
    extensible foundation through **Restrictions**, but it currently
    assumes a relatively direct mapping between service requirements and
    granted powers and does not yet formalise the general `SATISFIES`
    process.
5.  The proposed solution is to keep the comparison rule extremely
    simple:

> **A granted Power satisfies a Power Requirement iff the set denoted by
> the required restrictions is a subset of the set denoted by the
> granted restrictions.**

Formally:

`SATISFIES(G, R) ⇔ ⟦R⟧ ⊆ ⟦G⟧`

All complexity is placed in the semantics of the Restriction expressions
and their governed vocabularies, not in the core comparison algorithm.

------------------------------------------------------------------------

## 2. Separation of concerns

For WEBUILD, four concepts should remain distinct.

### 2.1 Power

A **Power** describes the authority that has been granted: what a
representative may do, and within what boundaries.

### 2.2 Mandate

A **Mandate** records or represents the grant of one or more Powers from
a principal/mandator to a representative/mandatee.

### 2.3 Mandate Attestation

A **Mandate Attestation** is evidence about the Mandate or granted
Power. It carries the information needed to establish trust in the
assertion, such as issuer, provenance, status and attestation lifecycle
information.

This leads to an important distinction:

``` text
Mandate validity
      ≠
Attestation validity
      ≠
Evidence validity
      ≠
RP acceptance
```

The attestation may expire without the underlying legal authority
necessarily ceasing to exist. Conversely, the legal authority may
terminate while an old attestation remains cryptographically intact.

### 2.4 Power Requirement

A **Power Requirement** expresses the authority the Relying Party (RP)
requires for a service, transaction or action.

The RP owns this requirement and evaluates presented evidence against
it.

``` text
Mandate Attestation
        │
        │ attests
        ▼
   Granted Power
        │
        │ SATISFIES?
        ▼
 Power Requirement
        ▲
        │ defined by
        │
  Relying Party
```

The source or issuer is responsible for the assertions it makes. The RP
remains responsible for deciding whether those assertions are sufficient
for the transaction it permits.

------------------------------------------------------------------------

## 3. Findings from RPaM and SEMPER

### 3.1 RPaM is the more relevant semantic predecessor

ISA² Action 2016.12 produced a substantial semantic package:

-   RPaM conceptual model;
-   RPaM OWL ontology in Turtle;
-   EU Powers Taxonomy in SKOS/SKOS-XL;
-   business rules;
-   eAuthorisation Criteria;
-   Power Use Constraints;
-   sample information requirements and constraints;
-   mappings and implementation material.

RPaM therefore contains more of the reusable semantic model than was
initially apparent from reviewing SEMPER.

### 3.2 SEMPER is closer to a validation/exchange architecture

SEMPER extended the eIDAS environment for cross-border exchange and
validation of representation powers. Its material describes a Powers
Validation Request and a Powers Declaration/validation result.

This is useful interoperability architecture, but it can obscure the
distinction between:

-   transmitting semantic evidence about granted authority; and
-   making the RP's authorisation decision.

For WEBUILD, enough semantic information should be available to permit
**RP-side evaluation**.

### 3.3 RPaM recognised RP requirements

RPaM's `eAuthorisationCriterion` is an important concept. It recognises
that the Service Provider defines information requirements and
constraints in order to determine whether a representative may use a
service.

This is conceptually aligned with the WEBUILD distinction between:

``` text
Granted Power  <---- evaluation ---->  Power Requirement
```

However, RPaM does not appear to provide the general, formally defined
power-subsumption calculus required for the simple and deterministic
`SATISFIES` model proposed here.

------------------------------------------------------------------------

## 4. Concern with a monolithic Powers Taxonomy

A power such as:

> "Power to submit a corporate tax declaration"

can combine several semantic dimensions:

-   action: submit;
-   object: corporate tax declaration;
-   context/domain: taxation;
-   represented organisation;
-   jurisdiction;
-   possible value, temporal or other limitations.

Encoding combinations of these dimensions as single Power codes can lead
to a rapidly expanding taxonomy and unclear governance.

Different semantic dimensions also have different natural owners.

For example:

  Semantic information     Likely governance/source
  ------------------------ -----------------------------------------------
  Action vocabulary        shared/legal/domain vocabulary
  NACE economic activity   competent NACE authority
  Region                   authoritative geographic vocabulary
  Organisation             authoritative registry
  Legal role               competent legal/domain authority
  Service requirement      Relying Party / service owner
  Granted mandate          principal and/or authoritative mandate source
  Named statutory power    competent legal authority

A single centrally governed Powers Taxonomy risks combining information
belonging to different authorities.

------------------------------------------------------------------------

## 5. WEBUILD's existing Restriction pattern

WEBUILD already models the extent of a Power through extensible
**Restrictions**.

Current examples include:

``` text
Restriction
│
├── Action
│    specialization hierarchy
│
├── Region
│    containment hierarchy
│
├── NACE
│    classification/containment hierarchy
│
├── Organisation
│    registry list
│
└── Restricted Value Range
     ├── operator
     ├── value
     └── unit
```

Additional managed code lists can be introduced as additional
Restriction dimensions.

This is preferable to requiring a universal enumeration of every
possible Power.

A suitable broad interpretation of `Restriction` is:

> **A condition or semantic boundary that defines or limits the extent
> within which a Power may be exercised.**

Under this interpretation, an Action can legitimately be a Restriction
because it defines the set of acts covered by the Power.

------------------------------------------------------------------------

## 6. The fundamental authorisation rule

The proposed WEBUILD rule is:

> **Required ⊆ Granted**

A Power denotes a set of permitted transactions or acts. A Power
Requirement denotes the set for which authority must be demonstrated.

A Power satisfies a Power Requirement exactly when:

``` text
required-set ⊆ granted-set
```

Formally:

``` text
SATISFIES(G, R) ⇔ ⟦R⟧ ⊆ ⟦G⟧
```

where `⟦x⟧` denotes the set represented by expression `x`.

This should be the core comparison rule rather than defining separate
top-level algorithms for numeric ranges, regions, actions, NACE codes,
etc.

------------------------------------------------------------------------

## 7. Examples

### 7.1 Numeric range

Granted:

``` text
Amount <= 100,000 EUR
```

Required transaction:

``` text
Amount = 10,000 EUR
```

Semantically:

``` text
{10,000} ⊆ [0, 100,000]
```

Result: `SATISFIES`.

### 7.2 Action specialization

Assume the governed Action hierarchy establishes:

``` text
SignPurchaseContract
    specializes
SignContract
```

Granted:

``` text
Action = SignContract
```

Required:

``` text
Action = SignPurchaseContract
```

The value `SignContract` denotes the action and its valid
specialisations. Therefore:

``` text
SignPurchaseContract ⊆ SignContract
```

Result: `SATISFIES`.

The reverse does not hold.

### 7.3 NACE hierarchy

Granted:

``` text
NACE = 41
Construction of buildings
```

Required:

``` text
NACE = 41.20
Construction of residential and non-residential buildings
```

If the authoritative NACE hierarchy establishes that `41.20` is within
`41`, then:

``` text
41.20 ⊆ 41
```

Result: `SATISFIES`.

### 7.4 Region with exclusions

WEBUILD's operator model allows:

``` text
Granted:
    Region IN EU
    AND Region NOT IN {BE, ES}
```

The granted set is:

``` text
EU \ {BE, ES}
```

Requirement:

``` text
Region = NL
```

Therefore:

``` text
{NL} ⊆ EU \ {BE, ES}
```

Result: `SATISFIES`.

For:

``` text
Region = BE
```

the subset relation fails.

This demonstrates that exclusions do not require a different
authorisation algorithm. They only alter the set denoted by the
Restriction expression.

------------------------------------------------------------------------

## 8. Hierarchies must stay within semantic dimensions

A crucial rule is:

> Hierarchical relations may participate in `SATISFIES` only when they
> describe containment or specialization within the same semantic
> dimension.

For example:

``` text
Action:
SignPurchaseContract ⊆ SignContract
```

is meaningful.

Likewise:

``` text
Region:
Netherlands ⊆ EU
```

and:

``` text
NACE:
41.20 ⊆ 41
```

But a relation between:

``` text
NACE: Construction
```

and:

``` text
Action: Build
```

must not be used for subset reasoning simply because the terms are
semantically related.

This is a key limitation of blindly interpreting generic `skos:broader`
/ `skos:narrower` links as authorisation relations.

SKOS can remain a useful vocabulary publication mechanism, but a
hierarchy intended for automated authorisation must have sufficiently
precise, governed semantics.

------------------------------------------------------------------------

## 9. Specialization versus composition

Two kinds of hierarchy must not be confused.

### 9.1 Specialization

``` text
SignPurchaseContract
    specializes
SignContract
```

This supports subset reasoning:

``` text
SignPurchaseContract ⊆ SignContract
```

### 9.2 Composition or entailment

A genuinely named legal concept can contain several powers.

For example, a competent authority might define:

``` text
ManagingDirectorRepresentationPower
    entails:
        SignContract
        RepresentBeforeAuthority
        SubmitCorporateFiling
```

This does **not** mean that these three actions are subclasses of
`ManagingDirectorRepresentationPower`.

The named legal concept is a governed definition that entails several
capabilities.

A useful conceptual pattern is:

``` text
PowerDefinition
      │
      └── entails Power / Power pattern
```

For example:

``` text
ManagingDirectorRepresentationPower
      │
      ├── entails Power:
      │      Action = SignContract
      │
      ├── entails Power:
      │      Action = RepresentBeforeAuthority
      │
      └── entails Power:
             Action = SubmitCorporateFiling
```

Each entailed Power may itself contain additional Restrictions.

This permits authoritative legal concepts to coexist with compositional
WEBUILD Powers.

------------------------------------------------------------------------

## 10. Named legal powers

WEBUILD should not prohibit named legal Power concepts.

Where legislation or another competent authority genuinely defines a
named representation power, that authority can issue and govern the
definition.

For example:

``` text
ManagingDirectorRepresentationPower
    a PowerDefinition .
```

Its authoritative semantic definition can then be expanded into ordinary
Power/Restriction expressions before or during evaluation.

This has two advantages:

1.  a mandate can refer directly to a legally recognised concept;
2.  an RP can still evaluate that concept against its own granular Power
    Requirement.

The legal authority owns the meaning and decomposition of the named
concept rather than WEBUILD maintaining a universal central list of all
European powers.

------------------------------------------------------------------------

## 11. Implications for managed code lists

WEBUILD's extensible Restriction approach allows each semantic authority
to maintain its own vocabulary.

The important requirement is not that all values belong to one code
list. It is that a managed vocabulary used for automated authorisation
provides enough semantics to determine the set represented by a
Restriction.

Examples:

``` text
Action hierarchy
    → specialization

Region hierarchy
    → territorial containment

NACE hierarchy
    → economic-activity containment/specialization

Organisation registry
    → normally singleton identity values

Numeric range
    → mathematically defined interval

Date range
    → temporal interval
```

The core authorisation algorithm remains unaware of the domain-specific
meaning beyond the ability to determine the denoted set and test
containment.

------------------------------------------------------------------------

## 12. Proposed conceptual architecture

``` text
Principal
    │
    │ grants
    ▼
Representative
    │
    ▼
Granted Power
    │
    ├── Restriction: Action
    ├── Restriction: Region
    ├── Restriction: NACE
    ├── Restriction: Organisation
    ├── Restriction: Value Range
    └── extensible Restrictions
    │
    │ attested by
    ▼
Mandate Attestation
    │
    │ presented to
    ▼
Relying Party
    │
    │ defines
    ▼
Power Requirement
    │
    ├── Restriction: Action
    ├── Restriction: Region
    ├── Restriction: NACE
    ├── Restriction: Organisation
    ├── Restriction: Value Range
    └── extensible Restrictions
```

Evaluation:

``` text
        Granted Power G

               ▲
               │
       is R a subset of G?
               │
               │
        Power Requirement R


SATISFIES(G,R) ⇔ ⟦R⟧ ⊆ ⟦G⟧
```

Both sides therefore use the **same Restriction semantics**. There is no
need for separate "granted power codes" and "required power codes" with
mappings between them.

------------------------------------------------------------------------

## 13. Consequence for the current WEBUILD Authorisation model

The current model assumes, in effect, that an RP service can be mapped
directly or 1:1 to a Power in the mandate.

That assumption should be relaxed.

Instead:

``` text
Service
    │
    └── defines
         Power Requirement
               │
               ▼
          SATISFIES?
               ▲
               │
          Granted Power
               ▲
               │
       Mandate Attestation
```

A mandate may be substantially broader than the requirement for an
individual service.

Example:

``` text
Granted:
    Action = SignCommercialContract
    Amount <= 100,000 EUR

Required:
    Action = SignPurchaseContract
    Amount = 10,000 EUR
```

The values do not need to match 1:1. The RP needs to establish only:

``` text
Required ⊆ Granted
```

------------------------------------------------------------------------

## 14. Recommended design principles

1.  **Keep one core comparison rule:** `required ⊆ granted`.
2.  **Use the same Restriction model** for Granted Powers and Power
    Requirements.
3.  **Treat Restrictions as set expressions** over a defined semantic
    dimension.
4.  **Keep semantic dimensions separate.** Do not perform hierarchy
    reasoning across dimensions.
5.  **Allow operators and exclusions** so that complex permitted sets
    can be expressed without changing the comparison rule.
6.  **Use authoritative specialization/containment hierarchies** where
    taxonomy reasoning is required.
7.  **Do not assume generic SKOS hierarchy relations automatically have
    authorisation semantics.**
8.  **Keep named legal Power definitions possible**, but let the
    competent authority govern and semantically decompose them.
9.  **Separate specialization from composition/entailment.**
10. **Do not require 1:1 mappings between services and granted Powers.**
11. **Keep mandate payload, attestation/trust metadata, and RP
    requirements conceptually separate.**
12. **Keep the final authorisation decision with the RP.**

------------------------------------------------------------------------

## 15. RPaM reuse question

RPaM should be treated as valuable source material rather than adopted
wholesale.

The most useful next analysis is to inspect the actual RPaM EU Powers
Taxonomy and classify representative hierarchy relations as:

``` text
1. Specialization
   → potentially reusable for subset reasoning

2. Composition / entailment
   → potentially reusable, but through explicit Power definitions

3. Classification
   → useful for navigation/classification, not authorisation

4. Ambiguous / other
   → unsuitable for automatic SATISFIES reasoning without clarification
```

The decisive test for a hierarchy edge is not merely whether one concept
is `skos:broader` than another, but whether the authoritative semantics
justify the corresponding set-containment statement for the relevant
Restriction dimension.

This analysis would determine which parts of the RPaM taxonomy can be
reused safely in WEBUILD and which should instead be decomposed into
independently governed Restriction vocabularies.

------------------------------------------------------------------------

## 16. Core conclusion

The principal finding is that WEBUILD does **not** need to standardise
every possible European Power in a single hierarchy.

Instead, it can standardise:

-   the structure of a Power;
-   the structure of Restrictions;
-   how Restriction expressions denote permitted sets;
-   how authoritative hierarchies are used within individual semantic
    dimensions;
-   how named legal Powers can entail ordinary Power expressions; and
-   one universal authorisation relation:

``` text
required ⊆ granted
```

This keeps the authorisation mechanism simple while allowing the
semantics and governance of Actions, Regions, NACE activities,
Organisations, legal concepts and future Restriction dimensions to
remain with the appropriate authorities.

The missing element in the current WEBUILD Authorisation model is
therefore not another universal Powers Taxonomy, but the explicit
formalisation of **Power Requirement**, **Restriction set semantics**,
and the **SATISFIES** relation between a required and a granted Power.
