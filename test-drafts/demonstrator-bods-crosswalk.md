<!--
  Demonstrator crosswalk — worked example.
  Input: the non-normative sample payload in rulebooks/rb-ownership README §3.2.3
         (webuild-attestation-rulebooks-catalog), Apache-2.0.
  Output: the same facts expressed as BODS v0.4 statements.
  Intended as a concrete exhibit for issue #58 / PR #59 and the semantics-group discussion.
  Prefixes: bods: = https://vocab.openownership.org/terms#  ·  codes: = https://standard.openownership.org/codelists#  ·  ebwv: = https://w3id.org/ebwv#
-->

# Demonstrator: an Ownership attestation expressed in BODS

This takes the rulebook's own non-normative example (`rb-ownership` §3.2.3) and renders the identical facts as a set of **BODS v0.4 statements**. The point is to make concrete what the current flat model cannot express — in particular an *indirect ownership chain* — and to show field-by-field how the empty **Semantic Reference** column would be filled.

The BODS layer is the *payload* semantics only. The SD-JWT VC envelope (`vct`, selective disclosure, status list, trust anchor, holder binding) is unchanged and sits around it exactly as today.

## The scenario

`rb-ownership` §3.2.3 describes the ownership of one company by two owners:

| Owner | Direct | Indirect | Total | Category |
|---|---|---|---|---|
| John Doe (natural person) | 25% | 10% | 35% | Direct shareholder |
| Acme Holdings Inc. (legal person) | 50% | 0% | 50% | Direct shareholder |

The sample records John Doe's indirect 10% via an opaque list — `legal_person_id: ["DE12.HRB1212", "12345678901234567890"]` — with no way to say *how* the 10% arises. We make it concrete and arithmetically consistent: John Doe holds **40% of an intermediate holding company**, which in turn holds **25% of the subject** → 40% × 25% = **10% indirect**, giving **35% total**. Subject company: *Acme Manufacturing GmbH*. Intermediate: *Doe Holding BV*.

## A. Before — the rulebook representation (trimmed)

From `rb-ownership` §3.2.3, the natural-person owner:

```json
{
  "vct": "eu.we-build.ownership.1",
  "ownership": [
    {
      "natural_person": {
        "family_name": "Doe",
        "given_name": "John",
        "birth_date": "1980-01-15",
        "natural_person_identifier": { "document_type": "Passport", "document_number": "P12345678", "issuing_country": "USA" },
        "residence_address": { "address": "123 Main St", "locality": "Anytown", "postal_code": "12345", "region": "CA", "country": "USA" },
        "stake": {
          "direct_ownership": 25.00,
          "indirect_ownership": 10.00,
          "total_ownership": 35.00,
          "legal_person_id": ["DE12.HRB1212", "12345678901234567890"],
          "ownership_category": "Direct shareholder"
        }
      }
    }
  ]
}
```

What this representation cannot say:

- **How the 10% indirect arises.** `legal_person_id` lists two identifiers with no structure — no percentages on the intermediate links, no direction of flow, no way to distinguish "the chain runs through these" from "these are co-owned."
- **Direct vs indirect as a property of the interest.** It is baked into `total_ownership` arithmetic rather than typed.
- **A range instead of a point.** `stake` is a single decimal; banded disclosures (common in registers) can't be represented.
- **Provenance per fact, and history.** No per-fact source; no append-only change model.

## B. After — the same facts as BODS v0.4

Eight statements: three entity statements, one person statement, four relationship statements. Concatenated, they form one BODS dataset (a JSON array, or JSON Lines). IDs here are readable slugs for legibility; in production these are globally unique (UUID/ULID or content-hashed). Optional statement-grouping fields (`declaration`, `declarationSubject`) are omitted for readability.

**Entity statements**

```json
{
  "statementId": "stmt-entity-acme-mfg-0001",
  "recordId": "acme-manufacturing-gmbh",
  "recordStatus": "new",
  "statementDate": "2024-01-15",
  "recordDetails": {
    "entityType": { "type": "registeredEntity" },
    "name": "Acme Manufacturing GmbH",
    "incorporatedInJurisdiction": { "name": "Germany", "code": "DE" },
    "identifiers": [
      { "id": "529900T8BM49AURSDO55", "scheme": "XI-LEI", "schemeName": "Global Legal Entity Identifier Index" },
      { "id": "DEK1101R.HRB12345", "schemeName": "EUID" }
    ],
    "foundingDate": "2010-03-01",
    "addresses": [ { "type": "registered", "address": "Hauptstrasse 5, 10115 Berlin", "country": "DE" } ]
  },
  "source": { "type": ["selfDeclaration"] }
}
```

```json
{
  "statementId": "stmt-entity-doe-holding-0001",
  "recordId": "doe-holding-bv",
  "recordStatus": "new",
  "statementDate": "2024-01-15",
  "recordDetails": {
    "entityType": { "type": "registeredEntity" },
    "name": "Doe Holding BV",
    "incorporatedInJurisdiction": { "name": "Netherlands", "code": "NL" },
    "identifiers": [
      { "id": "7245001BLPDQU2UTPS66", "scheme": "XI-LEI", "schemeName": "Global Legal Entity Identifier Index" },
      { "id": "NLNAR.812345678", "schemeName": "EUID" }
    ],
    "addresses": [ { "type": "registered", "address": "Keizersgracht 1, 1015 Amsterdam", "country": "NL" } ]
  },
  "source": { "type": ["selfDeclaration"] }
}
```

```json
{
  "statementId": "stmt-entity-acme-holdings-0001",
  "recordId": "acme-holdings-inc",
  "recordStatus": "new",
  "statementDate": "2024-01-15",
  "recordDetails": {
    "entityType": { "type": "registeredEntity" },
    "name": "Acme Holdings Inc.",
    "incorporatedInJurisdiction": { "name": "United States", "code": "US" },
    "identifiers": [
      { "id": "5493001KJTIIGC8Y1R12", "scheme": "XI-LEI", "schemeName": "Global Legal Entity Identifier Index" }
    ],
    "addresses": [ { "type": "registered", "address": "789 Corporate Blvd, Dover, DE 19901", "country": "US" } ]
  },
  "source": { "type": ["selfDeclaration"] }
}
```

**Person statement**

```json
{
  "statementId": "stmt-person-john-doe-0001",
  "recordId": "person-john-doe",
  "recordStatus": "new",
  "statementDate": "2024-01-15",
  "recordDetails": {
    "personType": "knownPerson",
    "names": [ { "type": "individual", "fullName": "John Doe" } ],
    "birthDate": "1980-01-15",
    "nationalities": [ { "code": "US", "name": "United States" } ],
    "addresses": [ { "type": "residence", "address": "123 Main St, Anytown, CA 12345", "country": "US" } ],
    "identifiers": [ { "id": "P12345678", "scheme": "US-PASSPORT", "schemeName": "Passport" } ]
  },
  "source": { "type": ["selfDeclaration"] }
}
```

**Relationship statements**

```json
{
  "statementId": "stmt-rel-doe-acme-direct-0001",
  "recordId": "rel-doe-acme-direct",
  "recordStatus": "new",
  "statementDate": "2024-01-15",
  "recordDetails": {
    "subject": { "describedByEntityStatement": "stmt-entity-acme-mfg-0001" },
    "interestedParty": { "describedByPersonStatement": "stmt-person-john-doe-0001" },
    "interests": [
      { "type": "shareholding", "directOrIndirect": "direct", "beneficialOwnershipOrControl": true, "share": { "exact": 25 }, "startDate": "2019-06-01" }
    ]
  },
  "source": { "type": ["selfDeclaration"] }
}
```

```json
{
  "statementId": "stmt-rel-doe-holding-0001",
  "recordId": "rel-doe-doeholding",
  "recordStatus": "new",
  "statementDate": "2024-01-15",
  "recordDetails": {
    "subject": { "describedByEntityStatement": "stmt-entity-doe-holding-0001" },
    "interestedParty": { "describedByPersonStatement": "stmt-person-john-doe-0001" },
    "interests": [
      { "type": "shareholding", "directOrIndirect": "direct", "beneficialOwnershipOrControl": true, "share": { "exact": 40 } }
    ]
  },
  "source": { "type": ["selfDeclaration"] }
}
```

```json
{
  "statementId": "stmt-rel-holding-acme-0001",
  "recordId": "rel-doeholding-acme",
  "recordStatus": "new",
  "statementDate": "2024-01-15",
  "recordDetails": {
    "subject": { "describedByEntityStatement": "stmt-entity-acme-mfg-0001" },
    "interestedParty": { "describedByEntityStatement": "stmt-entity-doe-holding-0001" },
    "interests": [
      { "type": "shareholding", "directOrIndirect": "direct", "beneficialOwnershipOrControl": true, "share": { "exact": 25 } }
    ]
  },
  "source": { "type": ["selfDeclaration"] }
}
```

```json
{
  "statementId": "stmt-rel-acmeholdings-acme-0001",
  "recordId": "rel-acmeholdings-acme",
  "recordStatus": "new",
  "statementDate": "2024-01-15",
  "recordDetails": {
    "subject": { "describedByEntityStatement": "stmt-entity-acme-mfg-0001" },
    "interestedParty": { "describedByEntityStatement": "stmt-entity-acme-holdings-0001" },
    "interests": [
      { "type": "shareholding", "directOrIndirect": "direct", "beneficialOwnershipOrControl": true, "share": { "exact": 50 } }
    ]
  },
  "source": { "type": ["selfDeclaration"] }
}
```

## The key difference: the UBO figure is derived, not stored

John Doe's effective interest in Acme Manufacturing GmbH — **25% direct + (40% × 25%) = 35%** — is *computed by traversing the graph*, not held in a `total_ownership` field that can silently drift from the underlying holdings. The two intermediate links (Doe → Doe Holding 40%; Doe Holding → Acme 25%) are explicit and individually verifiable. This is exactly the `rb-ubo` model in reverse: the UBO list is a projection over the ownership/control graph, and here the graph is represented natively.

(If a publisher wants to *assert* the aggregate as well, BODS permits an additional relationship statement: John Doe → Acme Manufacturing, `directOrIndirect: "indirect"`, `share: { "exact": 10 }` — the computed indirect portion — alongside the constituent links. Storing it is optional; deriving it is always possible.)

## Field-by-field mapping

| Rulebook field (`rb-ownership`) | BODS location | Note |
|---|---|---|
| `natural_person.given_name` / `family_name` | person `names[].fullName` (type `individual` → `bods:Legal`) | reuse `ebwv:givenName` / `ebwv:familyName` |
| `natural_person.birth_date` | person `birthDate` | reuse `ebwv:dateOfBirth` |
| `natural_person.residence_address` | person `addresses[]` (type `residence` → `bods:Residence`) | reuse `ebwv:domicile` |
| `natural_person_identifier` (passport) | person `identifiers[]` {`id`, `scheme`, `schemeName`} | via PID attestation in practice (`rb-pid`) |
| `legal_person.legal_entity_name` | entity `name` | reuse `ebwv:legalName` |
| `legal_person.legal_form_type` | entity `entityType` (+ free-form) | reuse `ebwv:legalForm` |
| `legal_person.identifier.lei` / `.euid` | entity `identifiers[]` {`scheme: XI-LEI`} / {`schemeName: EUID`} | reuse `ebwv:lei` / `ebwv:legalIdentifier` |
| `legal_person.registered_address` | entity `addresses[]` (type `registered` → `bods:Registered`) | reuse `ebwv:registeredAddress` |
| `stake.ownership_category` | relationship `interests[].type` | → `bods:InterestType` (crosswalk below) |
| `stake.direct_ownership` / `indirect_ownership` | relationship `interests[].directOrIndirect` + `share` | direct/indirect becomes a *typed property*, not arithmetic |
| `stake.total_ownership` | *derived* by graph traversal | not stored — see above |
| `stake.legal_person_id` (chain) | the graph of entity + relationship statements | the opaque list becomes explicit linked statements |
| `evidence[]` | statement `source` {`type`, `url`, `description`} → `bods:SourceType` | per-fact provenance |

## Interest-type crosswalk (values used here)

| `ownership_category` | BODS `interests[].type` (JSON) | RDF class |
|---|---|---|
| Direct shareholder | `shareholding` + `directOrIndirect: direct` | `bods:Shareholding` + `codes:Direct` |
| Indirect shareholder | `shareholding` + `directOrIndirect: indirect` | `bods:Shareholding` + `codes:Indirect` |

(The full mapping for `control_mechanism` and `determination_methodology` is in issue #58.)

## What BODS adds, shown by this example

- **The indirect chain is explicit and verifiable** — three statements (Doe → Doe Holding → Acme) instead of an opaque two-element ID list.
- **Direct/indirect is typed** on the interest (`codes:Direct` / `codes:Indirect`), not inferred from totals.
- **`share` is a range** (`exact` here, but `minimum`/`maximum` available) — matches banded register and Implementing-Act formats.
- **Provenance is per fact** (`source.type` → `bods:OfficialRegister` / `bods:SelfDeclaration` / …) and **history is append-only** (`recordId` + `recordStatus` new/updated/closed).
- **The UBO list becomes a query** over this graph rather than a third, independently-maintained dataset that can drift.

## Round-trip

Because every rulebook field maps to a defined BODS location, an Ownership attestation round-trips to a BODS statement set and back without loss — which is what enables AMLR Art. 60/62 register submission and the `rb-ubo` §4.2.10 cross-check from the same wallet-held data. The credential envelope is untouched; only the payload gains agreed semantics. Existing open-source converters (the `bods-*` family) already perform this class of mapping for other formats.

## Using this exhibit

This is a discussion artefact, not a normative change. It pairs with issue #58 and PR #59. Suggested use: attach to the PR (or place alongside the intake submission under `test-drafts/`) and walk through the before/after at a semantics-group session as the concrete basis for deciding whether to adopt BODS as the reference model for the ownership/control/UBO semantics.

*Illustrative identifiers (LEIs, EUIDs, passport number) are fictional; identifier `scheme` codes follow the org-id.guide list that BODS references and should be validated against it.*
