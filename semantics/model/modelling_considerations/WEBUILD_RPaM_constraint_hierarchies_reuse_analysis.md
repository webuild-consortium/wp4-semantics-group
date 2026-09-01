# RPaM hierarchies and constraint concepts potentially reusable by WEBUILD

**Date:** 1 September 2026\
**Scope:** Distillation of RPaM v1.1.0 hierarchy material that may be
relevant to WEBUILD `Restriction` dimensions and the rule
`required ⊆ granted`.

## 1. Purpose

This note does **not** recommend adopting the RPaM EU Powers Taxonomy
wholesale. It extracts the hierarchy-like material that could
potentially be reused as WEBUILD Restriction vocabularies, and
explicitly flags questionable or unsafe elements.

The WEBUILD test applied here is:

> A hierarchy is useful for automated authorisation only when its
> relation can safely be interpreted as set containment within one
> semantic dimension.

Thus, for a granted restriction `G` and required restriction `R`:

``` text
SATISFIES(G,R) ⇔ ⟦R⟧ ⊆ ⟦G⟧
```

A generic `skos:broader` relation is therefore not sufficient by itself.
We need to know what semantic dimension the concepts belong to and
whether "narrower" really denotes a subset of the broader concept for
authorisation purposes.

------------------------------------------------------------------------

## 2. Primary RPaM sources inspected

The principal sources used for this distillation are:

1.  **RPaM Ontology v1.1.0 release**
    -   Interoperable Europe Portal
    -   https://interoperable-europe.ec.europa.eu/collection/isa-action-201612-semantic-interoperability-representation-powers-and-mandates-0/solution/representation-powers-and-mandates-ontology/release/110
2.  **EU Powers Taxonomy TTL**
    -   RPaM repository
    -   https://raw.githubusercontent.com/everis-rpam/RPaM-Ontology/master/02-Vocabularies/RPaM/EU_Powers_Taxonomy.ttl
3.  **Ontology Development Report**
    -   https://github.com/everis-rpam/RPaM-Ontology/wiki/Ontology-Development-Report
4.  **Implementation of eAuthorisation Criteria and Power Use
    Constraints**
    -   https://github.com/everis-rpam/RPaM-Ontology/wiki/Implementation-of-eAC-and-PUC
5.  **Power Use Constraint type vocabulary**
    -   `MorMeeConstraintType.ttl`
    -   https://github.com/everis-rpam/RPaM-Ontology/blob/v1.1.0/03-Syntax_Bindings/OWL-DL-TTL/rpam/thesauri/MorMeeConstraintType.ttl

The RPaM Development Report states that the Power Taxonomy was intended
to be a compound of **three concept schemes/dimensions: action, event,
and object**. However, the published EU Powers Taxonomy TTL inspected
here contains explicit concepts for the Action and Scope/Event
structures, but does **not** contain the promised Object hierarchy.

------------------------------------------------------------------------

# 3. RPaM Action hierarchy

This is the clearest candidate for reuse.

RPaM defines a concept scheme labelled **EU Power Action**. Its intended
top concept is `POWER_ACT`, defined as:

> "The actions that a Mandatee can carry out on behalf of the Mandator."

The published action concepts are:

``` text
Power Action
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

Definitions in RPaM:

  -------------------------------------------------------------------------------
  RPaM concept            RPaM meaning                    WEBUILD assessment
  ----------------------- ------------------------------- -----------------------
  `APPLY`                 petition something officially   **Potentially reusable
                                                          Action**

  `BUY`                   get something by paying money   **Potentially reusable
                                                          Action**

  `CLAIM`                 definition is only `...` in TTL **Questionable until
                                                          defined**

  `NOTIFY`                inform someone officially       **Potentially reusable
                                                          Action**

  `OBTAIN`                obtain/acquire something after  **Questionable overlap
                          asking                          with Request/Apply**

  `PAY`                   give money in exchange for      **Potentially reusable,
                          goods/services                  but definition too
                                                          narrow for taxes/fees**

  `REGISTER`              definition is only `...` in TTL **Questionable until
                                                          defined**

  `REQUEST`               ask formally for something      **Potentially reusable
                                                          Action**

  `SUBMIT`                present                         **Potentially reusable
                          proposal/application/document   Action**
                          for consideration               
  -------------------------------------------------------------------------------

## 3.1 Reuse potential

The *idea* of an Action dimension is strongly reusable:

``` text
Restriction
    dimension = Action
    value = <managed Action concept>
```

A proper WEBUILD Action hierarchy could support:

``` text
SignPurchaseContract
    specializes SignContract

SignContract
    specializes PerformLegalAct
```

and therefore:

``` text
required Action = SignPurchaseContract
⊆
granted Action = SignContract
```

## 3.2 Important limitation

The RPaM action vocabulary is extremely shallow. Every listed action is
directly below the root. It does not contain the specialization depth
required for useful `required ⊆ granted` reasoning.

For example, it gives:

``` text
Submit
```

but not:

``` text
Submit
└── SubmitFiling
    ├── SubmitTaxFiling
    └── SubmitCorporateFiling
```

Therefore the RPaM Action list is better regarded as **seed
vocabulary/source material** than as a reusable authorisation hierarchy.

## 3.3 Technical defect in the published TTL

There is a significant IRI/case inconsistency.

The actual top concept is:

``` text
:POWER_ACT
```

but child concepts use:

``` text
skos:broader :Power_Act
```

RDF IRIs are case-sensitive. Therefore `:POWER_ACT` and `:Power_Act` are
different resources.

As published, the child Action concepts are therefore **not technically
linked to the declared `POWER_ACT` top concept**.

This must be corrected before any reuse.

------------------------------------------------------------------------

# 4. RPaM Scope / Event hierarchy

The second explicit hierarchy in the TTL is called `Power Scope`.

RPaM defines it as:

> "The main areas where powers may be applied: life events and business
> events."

The intended structure is:

``` text
Power Scope
├── Life Event
│   ├── Birth
│   ├── Moving
│   ├── Residence
│   └── Studying
│
├── Business Event
│   ├── Doing Business
│   ├── Retiring
│   ├── Starting Business
│   └── Working
│
└── All EU Powers
```

This hierarchy is much more questionable for WEBUILD authorisation.

------------------------------------------------------------------------

# 5. Life Event branch

## 5.1 Birth

``` text
Power Scope
└── Life Event
    └── Birth
```

RPaM definition:

> Powers related to activities that refer to birth.

Example:

> Power to request proof of registration of birth.

### Assessment

**Questionable as a Power Restriction hierarchy.**

`Birth` is not an Action. It is a context/event/domain in which an
Action takes place.

It could potentially become a separate WEBUILD dimension such as:

``` text
Restriction dimension = LifeEvent
value = Birth
```

but only if WEBUILD has a real need to authorise by life-event context.

It should not be mixed with Action.

------------------------------------------------------------------------

## 5.2 Moving

``` text
Power Scope
└── Life Event
    └── Moving
```

Examples include obtaining emission stickers, registering an address
change and registering a motor vehicle.

### Assessment

**Questionable / contextual grouping.**

This is a service/life-event category containing semantically different
Actions and Objects. It does not itself form an obvious authorisation
subset hierarchy.

Potential reuse is mainly as a **service discovery or contextual
classification vocabulary**, not directly as a WEBUILD Restriction
hierarchy.

------------------------------------------------------------------------

## 5.3 Residence

``` text
Power Scope
└── Life Event
    └── Residence
```

Example: request proof of residence.

### Assessment

**Potential contextual Restriction, but not an Action.**

If representation powers genuinely need to be limited to matters
concerning residence, a governed `SubjectMatter` or `Context` dimension
may be appropriate.

Do not infer:

``` text
Residence ⊆ LifeEvent
```

as an Action-authorisation relation. It is classification of context.

------------------------------------------------------------------------

## 5.4 Studying

``` text
Power Scope
└── Life Event
    └── Studying
```

Examples include applying for study finance and submitting an
application for higher education.

### Assessment

**Context/service-domain classification, not a direct Power hierarchy.**

Could potentially seed a `Context`, `SubjectMatter`, or `LifeEvent`
Restriction vocabulary, but it should not participate in the same
hierarchy as Actions.

------------------------------------------------------------------------

# 6. Business Event branch

## 6.1 Doing Business

``` text
Power Scope
└── Business Event
    └── Doing Business
```

Examples include paying employee social contributions and notifying
social security about termination of employment.

### Assessment

**Questionable hybrid grouping.**

This combines a broad business context with many possible Actions,
Objects, organisations and legal domains.

For WEBUILD this should probably be decomposed, e.g.:

``` text
Action = Pay
Object/SubjectMatter = SocialContribution
```

or:

``` text
Action = Notify
Object/SubjectMatter = EndOfEmployment
Recipient/Organisation = SocialSecurityAuthority
```

`Doing Business` may remain useful as service classification, but not as
the primary semantic unit for `SATISFIES`.

------------------------------------------------------------------------

## 6.2 Starting Business

``` text
Power Scope
└── Business Event
    └── Starting Business
```

Examples include employer registration, employee registration and
business-activity notifications.

### Assessment

Same concern as `Doing Business`.

**Useful contextual/service classification; questionable as
authorisation hierarchy.**

It bundles multiple Actions and Objects.

------------------------------------------------------------------------

## 6.3 Working

``` text
Power Scope
└── Business Event
    └── Working
```

Examples include applying for an EHIC, notifying changes affecting
social-security benefits, and requesting determination of applicable
social-security legislation.

### Assessment

**Questionable classification.**

The concept groups employment/social-security procedures but does not
itself identify a precise permitted act.

Potential reuse as `Context`/`LifeEvent`/service classification only.

------------------------------------------------------------------------

## 6.4 Retiring

``` text
Power Scope
└── Business Event
    └── Retiring
```

Examples include claiming pension benefits and requesting pension
information.

### Assessment

**Especially questionable.**

RPaM places `Retiring` under `Business Event`, although retirement
intuitively behaves like a person's life event and the RPaM definition
itself refers to "a person's retirement".

This is evidence that the hierarchy is primarily a pragmatic service
taxonomy rather than a formally clean specialization hierarchy.

It should not be imported into WEBUILD without reconsidering the
semantic dimension.

------------------------------------------------------------------------

# 7. `All_EU_Powers`

The TTL contains:

``` text
All_EU_Powers
    skos:broader Power_Scope
```

but its definition is:

> "Power to delegate powers."

### Assessment

**Do not reuse as-is.**

The label and definition conflict:

-   `All_EU_Powers` suggests an unrestricted/top power;
-   the definition describes a specific **delegation power**.

Those are entirely different concepts.

If the intended meaning is delegation, WEBUILD should model a clearly
named concept such as:

``` text
DelegatePower
```

or an explicit delegation relation.

If the intended meaning is "all powers", it should denote the universe
of the relevant Power/Restriction dimension and not be defined as
delegation.

This is a strong example of why the RPaM taxonomy requires semantic
review before reuse.

------------------------------------------------------------------------

# 8. Technical defects in the Scope/Event hierarchy

The same case-sensitive IRI problem seen in Actions occurs throughout
this hierarchy.

The TTL declares:

``` text
:POWER_SCOPE
:LIFE_EVENT
:BUSINESS_EVENT
```

but relationships refer to:

``` text
:Power_Scope
:Life_Event
:Business_Event
```

These are different RDF resources.

For example:

``` text
:BIRTH skos:broader :Life_Event .
```

while the actual declared concept is:

``` text
:LIFE_EVENT a skos:Concept .
```

Therefore, as published, much of the apparent hierarchy is **technically
disconnected**.

This does not invalidate the conceptual intent, but the TTL must not be
reused mechanically.

------------------------------------------------------------------------

# 9. The missing RPaM Object dimension

This is important.

The RPaM Ontology Development Report explicitly states that the Powers
Taxonomy was built around three main concepts:

``` text
Action
Event
Object
```

It explains Object as the expected result of combining an Action and
Event, giving examples such as:

``` text
Request + Birth + Certificate
Claim   + Work  + Permit
```

However, the inspected published `EU_Powers_Taxonomy.ttl` contains no
corresponding Object concept scheme/hierarchy.

### Assessment

The **separation of Object from Action is conceptually valuable**, but
RPaM's definition of Object is questionable.

An Object should not normally be defined as "the result of Action +
Event".

For WEBUILD it would be cleaner to treat Object/Subject Matter as its
own Restriction dimension:

``` text
Power
├── ActionRestriction
│   └── Submit
└── ObjectRestriction
    └── CorporateFiling
```

rather than creating a compound code such as:

``` text
Submit + StartingBusiness + Filing
```

The missing Object taxonomy therefore provides a useful **design idea**,
but little directly reusable hierarchy content.

------------------------------------------------------------------------

# 10. RPaM Power Use Constraints (PUC)

RPaM separately defines **Power Use Constraints**, attached to a Power
through CCEV Criterion Properties.

The Development Report says these can express, for example:

-   period of validity;
-   financial thresholds;
-   single-use versus multiple-use;
-   other limitations.

The implementation example contains:

``` text
FinancialCeil
    amount = 10000 EUR
```

and:

``` text
ValidityPeriod
    endDate = 2025-12-12
```

The published `MorMeeConstraintType.ttl` explicitly contains:

``` text
Validity period
One single use
```

## Assessment for WEBUILD

The *concepts* are relevant, but they do not form a useful
specialization hierarchy.

WEBUILD already has a more general representation:

``` text
Restriction
├── operator
├── value
└── unit
```

For example:

``` text
Amount <= 100000 EUR
```

or:

``` text
Date IN [2026-01-01, 2026-12-31]
```

These naturally denote sets and therefore fit:

``` text
required ⊆ granted
```

A code such as `FinancialCeil` is therefore probably unnecessary as a
special constraint type if WEBUILD's operator/value/unit model already
expresses the semantics.

`OneSingleUse` is different: it is a cardinality/consumption constraint
and may require a restriction dimension such as:

``` text
NumberOfUses <= 1
```

Again, WEBUILD can express the semantics compositionally rather than
minting a special-purpose constraint code.

------------------------------------------------------------------------

# 11. CPV hierarchy used in RPaM eAuthorisation Criteria

RPaM's eAC example is highly relevant because it explicitly relies on
hierarchy containment.

The Service Provider specifies a CPV constraint:

``` text
33196000-0
```

and the documentation states that a descendant code such as:

``` text
33196008-2
```

can be a valid response because it is a descendant of the code in the
constraint.

This is essentially the WEBUILD rule:

``` text
required/value ⊆ granted/allowed category
```

or, depending on which side is being constrained, a containment test
over one managed classification dimension.

### Assessment

**Strongly reusable pattern.**

Not necessarily the CPV vocabulary itself for mandate powers, but the
modelling principle:

``` text
Restriction dimension = CPV
value = broader CPV concept
```

with descendants denoting subsets.

This is directly analogous to WEBUILD's NACE restriction.

It is one of the clearest examples in RPaM of hierarchy-based constraint
evaluation.

------------------------------------------------------------------------

# 12. Candidate RPaM material by WEBUILD Restriction dimension

## 12.1 Action

Potential seeds:

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

**Recommendation:** reuse only after semantic cleanup and extension with
real specialization levels.

------------------------------------------------------------------------

## 12.2 Context / Subject Matter / Life Event

Potential seeds:

``` text
Context
├── Birth
├── Moving
├── Residence
├── Studying
├── Doing Business
├── Starting Business
├── Working
└── Retiring
```

**Recommendation:** questionable for direct authorisation. Consider only
if WEBUILD needs a `Context`, `SubjectMatter`, or `LifeEvent`
Restriction dimension.

Do not mix these with Actions.

------------------------------------------------------------------------

## 12.3 Object

RPaM conceptually identifies this dimension but does not provide a
useful published hierarchy in the inspected Powers TTL.

**Recommendation:** retain the idea, not the RPaM implementation.

Potential WEBUILD form:

``` text
Object
├── Contract
│   ├── PurchaseContract
│   └── EmploymentContract
├── CorporateFiling
├── TaxDeclaration
├── Permit
└── Certificate
```

Such a hierarchy could participate directly in `required ⊆ granted`.

------------------------------------------------------------------------

## 12.4 Economic activity / procurement classification

RPaM demonstrates hierarchy reasoning using CPV.

WEBUILD already uses NACE similarly.

**Recommendation:** strong reuse of the *pattern*:

``` text
required classification concept
    narrower than / contained in
granted classification concept
```

provided the hierarchy is authoritative and remains within one
dimension.

------------------------------------------------------------------------

## 12.5 Time

RPaM PUC:

``` text
ValidityPeriod
```

**Recommendation:** model as interval Restriction rather than taxonomy
hierarchy.

``` text
required time interval ⊆ granted time interval
```

------------------------------------------------------------------------

## 12.6 Monetary amount

RPaM example:

``` text
FinancialCeil = 10000 EUR
```

**Recommendation:** model as numeric range.

``` text
required amount range ⊆ granted amount range
```

No taxonomy is needed.

------------------------------------------------------------------------

## 12.7 Number of uses

RPaM:

``` text
OneSingleUse
```

**Recommendation:** model compositionally if possible:

``` text
NumberOfUses <= 1
```

This preserves the universal set-containment model.

------------------------------------------------------------------------

# 13. Overall classification of RPaM hierarchy material

  ---------------------------------------------------------------------------------------
  RPaM material    Semantic dimension               Reuse potential Main concern
  ---------------- ---------------------- ------------------------- ---------------------
  Power Actions    Action                            **High as seed too shallow; broken
                                                       vocabulary** IRI links;
                                                                    definitions
                                                                    incomplete

  Life Events      Context/LifeEvent        **Medium/Questionable** classification rather
                                                                    than authority
                                                                    specialization

  Business Events  Context/Service domain           **Low--Medium** hybrid grouping;
                                                                    questionable
                                                                    placement

  Power Scope root Context umbrella                         **Low** mixes heterogeneous
                                                                    contextual categories

  All EU Powers    unclear/delegation        **Do not reuse as-is** label/definition
                                                                    conflict

  Object dimension Object/SubjectMatter            **High as design hierarchy absent from
                                                        principle** inspected TTL; RPaM
                                                                    definition is
                                                                    compound

  CPV descendant   Classification               **High as reasoning must remain within
  example                                                 pattern** CPV dimension

  Validity Period  Temporal range             **High conceptually** better as interval
                                                                    than taxonomy

  Financial        Numeric range              **High conceptually** better as
  Ceiling                                                           operator/value/unit

  One Single Use   Usage cardinality          **High conceptually** better as
                                                                    numeric/cardinality
                                                                    restriction
  ---------------------------------------------------------------------------------------

------------------------------------------------------------------------

# 14. What can actually be reused

The strongest reusable RPaM ideas are not its complete Powers Taxonomy,
but these components:

### A. Action as an independent dimension

``` text
Restriction → Action
```

This aligns directly with WEBUILD.

### B. Object as an independent dimension

Although poorly realised in the published taxonomy, the separation
itself is useful.

### C. Hierarchical managed classifications

The CPV example confirms the value of using descendants to satisfy
constraints within one dimension. This is directly applicable to NACE
and other managed WEBUILD code lists.

### D. Power Use Constraints

Validity, amount and usage restrictions are all useful, but WEBUILD can
model them more uniformly as set-denoting Restrictions.

### E. RP-defined criteria

RPaM recognises that the Service Provider/RP defines constraints and
information requirements. WEBUILD can improve this by expressing both
the granted Power and Power Requirement using the same Restriction
semantics.

------------------------------------------------------------------------

# 15. What should not be reused without redesign

1.  **Do not treat every RPaM `skos:broader` edge as authorisation
    subsumption.**
2.  **Do not merge Action and Event/Context into one hierarchy.**
3.  **Do not use the existing Powers TTL mechanically; its
    case-sensitive IRIs break intended hierarchy links.**
4.  **Do not reuse `All_EU_Powers` without resolving its contradictory
    meaning.**
5.  **Do not adopt the Event hierarchy as though it were a
    specialization hierarchy of Powers.**
6.  **Do not model compound Action + Event + Object meanings as single
    codes where independently governed dimensions can be composed.**
7.  **Do not require special constraint-type codes where
    operator/value/unit or interval semantics already express the
    restriction.**

------------------------------------------------------------------------

# 16. Proposed WEBUILD distillation of the useful RPaM material

A cleaned WEBUILD interpretation could look like:

``` text
Restriction
│
├── Action
│   └── authoritative specialization hierarchy
│
├── Object / SubjectMatter
│   └── authoritative specialization hierarchy
│
├── Region
│   └── authoritative containment hierarchy
│
├── NACE
│   └── authoritative classification hierarchy
│
├── Organisation
│   └── authoritative registry / identity set
│
├── Context                     [optional]
│   └── governed contextual hierarchy
│
├── Amount
│   └── operator + value + unit
│
├── Time
│   └── operator + interval/value
│
├── NumberOfUses
│   └── operator + value
│
└── extensible managed dimensions
```

Named legal powers can sit above this compositional layer:

``` text
ManagingDirectorRepresentationPower
    entails PowerPattern A
    entails PowerPattern B
    entails PowerPattern C
```

where each entailed Power pattern is itself expressed through ordinary
WEBUILD Restrictions.

------------------------------------------------------------------------

# 17. Core conclusion

RPaM contains useful constraint-related hierarchy ideas, but **there is
no single RPaM hierarchy that should simply be imported as the WEBUILD
authorisation hierarchy**.

The strongest reusable hierarchy is the **Action dimension**, although
the published list is shallow and technically defective. The Event/Scope
hierarchy is mainly a contextual/service classification and should be
treated as questionable for authorisation. The proposed Object dimension
is conceptually useful but not actually realised in the inspected Powers
TTL. RPaM's CPV example is strong evidence for the same-dimension
containment principle WEBUILD is adopting. Its financial, temporal and
usage constraints are also useful requirements, but WEBUILD's generic
operator/value/unit model expresses them more elegantly.

The recommended reuse principle is therefore:

> **Reuse RPaM concepts only after assigning each concept to a single
> WEBUILD Restriction dimension and confirming that its hierarchy
> relation denotes genuine set containment within that dimension.**

Then all reusable material can participate in the same rule:

``` text
required ⊆ granted
```

without introducing RPaM's hybrid Powers Taxonomy into the core WEBUILD
model.
