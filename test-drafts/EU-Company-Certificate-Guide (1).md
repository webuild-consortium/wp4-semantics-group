# EU Company Certificate — Human-Readable Guide
> **Goal:** Prove that a company is legally incorporated in an EU Member State and provide reliable, harmonised information about its identity, registration, legal form, status, and representation.

This guide follows the same content structure as your *Power of Representation* guide and is derived from the uploaded **EU Company Certificate application profile**. The **examples** use the JSON Schema version of the model.

---

## 1. Classes and Properties (from the SHACL profile)
*(Enumerated accurately from the uploaded profile; referenced-but-undefined shapes are marked as such.)*

### LegalEntity
- `legalName` *(string, 1..1)*
- `hasLegalForm` → **LegalForm** *(1..1, referenced; shape not defined in the JSON extract)*
- `hasLegalIdentifier` → **Identifier** *(1..1)*
- `hasIdentifier` → **Identifier[] (0..n)* — includes EUID and other IDs (apart from the registration number)
- `registeredAddress` → **Address** *(1..1)*
- `postalAddress` → **Address[] (1..n)*
- `registrationDate` *(string/date, 1..1)*
- `hasShareCapital` → **ShareCapital** *(1..1)*
- `hasLegalStatus` → **LegalStatus** *(1..1)*
- `hasActivity` → **Activity** *(1..1, referenced; shape not defined in the JSON extract)*
- `hasContactPoint` → **ContactPoint[] (0..n)*
- `hasRepresentationRule` → **RepresentationRule[] (0..n)*

### Identifier
- `schemaAgency` *(string, 1..1)* — issuing register/authority
- `notation` *(string, 1..1)* — the identifier value
- `schemeName` *(string[] , 0..n)* — scheme label(s) (e.g., EUID, LEI)

### Address
*(Generic address structure; all properties optional unless noted)*
- `fullAddress` *(string[])*
- `postCode` *(string[])*
- `postName` *(object[])*
- `adminUnitLevel1` *(object[])*
- `adminUnitLevel2` *(object[])*
- `thoroughfare` *(string[])*
- `locatorName` *(object[])*
- `locatorDesignator` *(object[])*
- `postOfficeBox` *(object[])*
- `careOf` *(object[])*

### ShareCapital
- `capitalType` *(string, 1..1)*
- `totalCapitalAmount` → **MonetaryAmount[] (0..n)*

### MonetaryAmount
- `currency` *(string, 1..1)*
- `value` *(number, 1..1)*

### LegalStatus
- `hasCode` → **CodeClass** *(1..1)*
- `date` *(string/date, 1..1)*

### CodeClass
- `name` *(string, 1..1)*

### ContactPoint
- `contactPage` *(string, 0..1)*
- `email` *(string, 0..1)*

### RepresentationRule
- `description` *(string, 0..1)*
- `membershipBasedRule` → **MembershipBasedRepresentationRule[] (1..n)*
- `roleBasedRule` → **RoleBasedRepresentationRule[] (1..n)*

### MembershipBasedRepresentationRule
- `definesValidMembership` → **Membership[] (1..n)*
- `minimumNumberOfMembers` *(object[])*
- `memberQuantifier` *(referenced type; not defined in the JSON extract)*

### RoleBasedRepresentationRule
- `definesValidRole` → **Role[] (1..n)*
- `minimumNumberOfRoleHolders` *(number[])*
- `roleHolderQuantifier` *(referenced type; not defined in the JSON extract)*

### Membership
- `member` → **Person[] (1..n)*
- `hasRole` → **Role[] (1..n)*

### Role
- `name` *(string, 1..1)*
- `codeValue` *(string, 1..1)*

### Person
- `fullName` *(string, 1..1)*
- `dateOfBirth` *(string/date, 1..1)*

> **Notes:**  
> • The profile distinguishes between the **registration number & Member State** (`hasLegalIdentifier`) and **other identifiers** (like **EUID**, **LEI**) in `hasIdentifier`.  
> • `hasActivity` and `hasLegalForm` are referenced but their detailed shapes are not included in the JSON extract; implementations typically use code lists (e.g., **NACE** for activities).

---

## 2. Real‑world Example (JSON) — Article 16b a–o mapped
A Dutch-style EU Company Certificate reflecting points **(a–o)** from Article 16b. (Fields not present in the JSON profile are included only where the profile provides a slot.)

```json
{
  "@type": "wbeucc:EUCompanyCertificate",
  "LegalEntity": {
    "legalName": "Innovative Timber Structures B.V.",
    "hasLegalForm": { "name": "Besloten Vennootschap (Private Limited Liability Company)" },
    "hasLegalIdentifier": {
      "schemaAgency": "NL-BR",
      "schemeName": ["Dutch Business Register"],
      "notation": "80234567"
    },
    "hasIdentifier": [
      { "schemaAgency": "EU", "schemeName": ["EUID"], "notation": "NL.BR.80234567" },
      { "schemaAgency": "LEI", "schemeName": ["Legal Entity Identifier"], "notation": "724500N3BN3F4W9Z8L61" }
    ],
    "registeredAddress": {
      "fullAddress": ["Keizersgracht 221, 1016 DV Amsterdam, Netherlands"]
    },
    "postalAddress": [
      { "fullAddress": ["Postbus 123, 1000 AA Amsterdam, Netherlands"] }
    ],
    "registrationDate": "2018-04-06",
    "hasShareCapital": {
      "capitalType": "subscribed",
      "totalCapitalAmount": [{ "currency": "EUR", "value": 100000 }]
    },
    "hasLegalStatus": {
      "hasCode": { "name": "Active" },
      "date": "2025-09-12"
    },
    "hasActivity": {
      "naceCode": "C16.23",
      "naceDescription": "Manufacture of other builders' carpentry and joinery"
    },
    "hasContactPoint": [
      { "contactPage": "https://www.innovativetimber.eu", "email": "info@innovativetimber.eu" }
    ],
    "hasRepresentationRule": [
      {
        "description": "The company is represented by the managing director acting alone.",
        "membershipBasedRule": [
          {
            "definesValidMembership": [
              {
                "member": [
                  { "fullName": "Anna de Vries", "dateOfBirth": "1981-07-04" }
                ],
                "hasRole": [
                  { "name": "Managing Director", "codeValue": "MD" }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
}
```

**Mapping to Article 16b:**  
(a) `legalName` • (b) `hasLegalForm.name` • (c) `hasLegalIdentifier.schemaAgency` (Member State) + `hasLegalIdentifier.notation` (registration number) • (d) `hasIdentifier[?schemeName="EUID"].notation` (EUID) • (e) `registeredAddress.fullAddress[]` • (f) correspondence → `postalAddress[]` and/or `hasContactPoint.email` • (g) `registrationDate` • (h) `hasShareCapital.totalCapitalAmount[]` • (i) `hasLegalStatus.hasCode.name` + `hasLegalStatus.date` • (j) `hasRepresentationRule[].membershipBasedRule[].definesValidMembership[].member[]` + `hasRole[]` (+ free-text `description` for joint/sole rules) • (k) if representatives are **legal persons**, model their **name/legal form/EUID/registration number** in a `member` entry shaped as a LegalEntity (not shown in this natural person example) • (l) `hasActivity.*` • (m) *duration*: not available as a field in the JSON extract • (n) `hasContactPoint.contactPage` • (o) *certificate date of issue*: not present as a field in the JSON extract.

---

## 3. JSON‑LD (using the compact context)
Use this context file in your project:
```
eu-company-certificate-context.jsonld
```

Example JSON‑LD instance:
```json
{
  "@context": "eu-company-certificate-context.jsonld",
  "@type": "wbeucc:EUCompanyCertificate",
  "LegalEntity": {
    "legalName": "Innovative Timber Structures B.V.",
    "hasLegalForm": { "name": "Besloten Vennootschap (Private Limited Liability Company)" },
    "hasLegalIdentifier": { "schemaAgency": "NL-BR", "notation": "80234567", "schemeName": ["Dutch Business Register"] },
    "hasIdentifier": [{ "schemaAgency": "EU", "notation": "NL.BR.80234567", "schemeName": ["EUID"] }],
    "registeredAddress": { "fullAddress": ["Keizersgracht 221, 1016 DV Amsterdam, Netherlands"] },
    "registrationDate": "2018-04-06",
    "hasLegalStatus": { "hasCode": { "name": "Active" }, "date": "2025-09-12" },
    "hasActivity": { "naceCode": "C16.23", "naceDescription": "Manufacture of other builders' carpentry and joinery" },
    "hasContactPoint": [{ "contactPage": "https://www.innovativetimber.eu", "email": "info@innovativetimber.eu" }],
    "hasRepresentationRule": [{
      "description": "The company is represented by the managing director acting alone.",
      "membershipBasedRule": [{
        "definesValidMembership": [{
          "member": [{ "fullName": "Anna de Vries", "dateOfBirth": "1981-07-04" }],
          "hasRole": [{ "name": "Managing Director", "codeValue": "MD" }]
        }]
      }]
    }]
  }
}
```

---

## 4. As a W3C Verifiable Credential (VCDM 2.x)
```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    { "wbeucc": "https://iri.suomi.fi/model/wbeucc/" }
  ],
  "type": ["VerifiableCredential", "EUCompanyCertificateCredential"],
  "issuer": "did:web:register.example.nl",
  "validFrom": "2025-09-12T00:00:00Z",
  "credentialSubject": {
    "id": "did:example:company-innovativetimber",
    "EUCompanyCertificate": {
      "legalName": "Innovative Timber Structures B.V.",
      "hasLegalIdentifier": { "schemaAgency": "NL-BR", "notation": "80234567" },
      "hasIdentifier": [{ "schemaAgency": "EU", "notation": "NL.BR.80234567" }],
      "registrationDate": "2018-04-06",
      "hasLegalStatus": { "hasCode": { "name": "Active" } },
      "hasRepresentationRule": [{
        "description": "The company is represented by the managing director acting alone.",
        "membershipBasedRule": [{
          "definesValidMembership": [{
            "member": [{ "fullName": "Anna de Vries", "dateOfBirth": "1981-07-04" }],
            "hasRole": [{ "name": "Managing Director", "codeValue": "MD" }]
          }]
        }]
      }]
    }
  },
  "proof": {
    "type": "DataIntegrityProof",
    "cryptosuite": "eddsa-rdfc-2022",
    "created": "2025-09-12T10:00:00Z",
    "verificationMethod": "did:web:register.example.nl#keys-1",
    "proofPurpose": "assertionMethod",
    "proofValue": "eyJ...signature-bytes..."
  }
}
```

---

## 5. Validation Checklist
- `LegalEntity.legalName` present *(a)*
- `LegalEntity.hasLegalForm` present *(b)*
- `LegalEntity.hasLegalIdentifier` *(c)* and `LegalEntity.hasIdentifier` includes **EUID** *(d)*
- `LegalEntity.registeredAddress` *(e)* and `LegalEntity.postalAddress` / `hasContactPoint.email` *(f)*
- `LegalEntity.registrationDate` *(g)*
- `LegalEntity.hasShareCapital` *(h)*
- `LegalEntity.hasLegalStatus` *(i)*
- `LegalEntity.hasRepresentationRule` *(j)*
- **If legal-person representative**: model via Role/Member linkage *(k)*
- `LegalEntity.hasActivity` *(l)*
- *(m)* Duration — not present in the JSON extract
- `hasContactPoint.contactPage` *(n)*
- Certificate **date of issue** — not present in the JSON extract *(o)*

---

**Files**
- **Compact JSON‑LD context:** `eu-company-certificate-context.jsonld`  
- **This guide (Markdown):** `EU-Company-Certificate-Guide.md`
