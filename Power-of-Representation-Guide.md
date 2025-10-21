
# Power of Representation — Human-Readable Guide

> **Goal:** Prove that a named person is allowed to act on behalf of a specific company, for a specific purpose, from a specific date — in a way that software can verify automatically.

- **Mandate** = the authorization record.
- **Mandator (Legal Entity)** = the company that grants the authorization.
- **Mandatee (Person)** = the person who is authorized.
- **Scope** = what the person is allowed to do (the “powers”).
- **Representation Rule** = *why* the person is authorized (e.g., because they hold a valid membership/position).
- **Membership** = the concrete membership or position that makes the authorization valid (e.g., board member, procuration holder).
- **Identifier** = official IDs for the company (e.g., KVK, VAT, EUID, LEI).

---

## 1. Classes and Properties (from the SHACL profile)

### Mandate
- `dateOfIssue` *(date, 1..1)*
- `hasMandator` → **LegalEntity** *(1..1)*
- `hasScope` → **Scope** *(1..1)*
- `hasRepresentationRule` → **MembershipBasedRepresentationRule** *(1..1)*

### LegalEntity
- `legalName` *(string, 1..1)*
- `hasIdentifier` → **Identifier** *(1..n)*

### Person (Mandatee)
- `fullName` *(string)*
- `dateOfBirth` *(date)*

### Scope
- `power` *(1..n)* — typically a controlled code (e.g., `file-tax-returns`).

### MembershipBasedRepresentationRule
- `definesValidMembership` → **Membership** *(1..n)*

### Membership
- `member` → **Person** *(1..n)*

### Identifier
- `identifierValue` *(string)* — the code/number (e.g., “12345678”)
- `schemeName` *(string)* — the scheme (e.g., “NL:KVK”, “EUID”, “LEI”).

---

## 2. Minimal real-world example (JSON)
Dutch-style authorization (eHerkenning-like pattern):

```json
{
  "Mandate": {
    "dateOfIssue": "2025-10-21",
    "hasMandator": {
      "legalName": "Bouwbedrijf Janssen B.V.",
      "hasIdentifier": [
        {
          "identifierValue": "12345678",
          "schemeName": "NL:KVK"
        },
        {
          "identifierValue": "NL123456789B01",
          "schemeName": "NL:VAT"
        }
      ]
    },
    "hasScope": {
      "power": [
        "file-tax-returns",
        "submit-procurement-tenders"
      ]
    },
    "hasRepresentationRule": {
      "definesValidMembership": {
        "member": {
          "fullName": "Sanne de Vries",
          "dateOfBirth": "1990-04-05"
        }
      }
    }
  }
}
```

**How to read it:** *dateOfIssue* says when it starts; *hasMandator* tells which company; *power* lists what’s allowed; the representation rule points to a membership held by the person.

---

## 3. JSON-LD (using the compact context)

Use this context file in your project:
```
power-of-representation-context.jsonld
```

Example JSON-LD instance:

```json
{
  "@context": "power-of-representation-context.jsonld",
  "Mandate": {
    "@type": "Mandate",
    "dateOfIssue": "2025-10-21",
    "hasMandator": {
      "@type": "LegalEntity",
      "legalName": "Bouwbedrijf Janssen B.V.",
      "hasIdentifier": [
        {
          "@type": "Identifier",
          "identifierValue": "12345678",
          "schemeName": "NL:KVK"
        },
        {
          "@type": "Identifier",
          "identifierValue": "NL123456789B01",
          "schemeName": "NL:VAT"
        }
      ]
    },
    "hasScope": {
      "@type": "Scope",
      "power": ["file-tax-returns", "submit-procurement-tenders"]
    },
    "hasRepresentationRule": {
      "@type": "MembershipBasedRepresentationRule",
      "definesValidMembership": {
        "@type": "Membership",
        "member": {
          "@type": "Person",
          "fullName": "Sanne de Vries",
          "dateOfBirth": "1990-04-05"
        }
      }
    }
  }
}
```

---

## 4. As a W3C Verifiable Credential (VCDM 2.x)

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    "https://www.w3.org/ns/credentials/examples/v2",
    {
      "ncbv": "https://iri.suomi.fi/model/ncbv/0.0.5/",
      "webpor": "https://iri.suomi.fi/model/webpor/"
    }
  ],
  "type": ["VerifiableCredential", "PowerOfRepresentationCredential"],
  "issuer": "did:web:mandates.example.nl",
  "validFrom": "2025-10-21T00:00:00Z",
  "credentialSubject": {
    "id": "did:example:person-sanne",
    "Mandate": {
      "dateOfIssue": "2025-10-21",
      "hasMandator": {
        "legalName": "Bouwbedrijf Janssen B.V.",
        "hasIdentifier": [
          {"identifierValue": "12345678", "schemeName": "NL:KVK"},
          {"identifierValue": "NL123456789B01", "schemeName": "NL:VAT"}
        ]
      },
      "hasScope": {"power": ["file-tax-returns", "submit-procurement-tenders"]},
      "hasRepresentationRule": {
        "definesValidMembership": {
          "member": {
            "id": "did:example:person-sanne",
            "fullName": "Sanne de Vries",
            "dateOfBirth": "1990-04-05"
          }
        }
      }
    }
  },
  "proof": {
    "type": "DataIntegrityProof",
    "cryptosuite": "eddsa-rdfc-2022",
    "created": "2025-10-21T09:00:00Z",
    "verificationMethod": "did:web:mandates.example.nl#keys-1",
    "proofPurpose": "assertionMethod",
    "proofValue": "eyJ...signature-bytes..."
  }
}
```

**Implementation tips**
- Re-use the person’s DID in `credentialSubject.id` *and* in `Membership.member`.
- Use a controlled code list for `power` to enable automation across portals.
- Add `validUntil` or a status list if your deployment needs expiry/revocation.

---

## 5. Validation checklist
- `Mandate.dateOfIssue` present, type date.
- `Mandate.hasMandator` → LegalEntity with `legalName` and ≥1 `Identifier`.
- `Mandate.hasScope.power` has ≥1 value.
- `Mandate.hasRepresentationRule.definesValidMembership.member` points to the authorized **Person** (with `fullName`, `dateOfBirth`).

---

**Files**
- **Compact JSON-LD context:** `power-of-representation-context.jsonld`
- **This guide (Markdown):** `Power-of-Representation-Guide.md`
