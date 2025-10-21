# EU Company Certificate — Human-Readable Guide

> **Goal:** Prove that a company is legally incorporated in an EU Member State and provide reliable, harmonised information about its identity, registration, legal form, status, and representation.

This guide explains the **EU Company Certificate (EUCC)** as modelled in the *WE BUILD Application Profile* based on Article 16b of Directive (EU) 2025/25.  
Each class and property from the SHACL profile is listed together with its **real‑world meaning** in the context of the certificate.  
References to **Article 16b letters (a–o)** are shown in **bold** where applicable.

---

## 1. Classes and Properties (from the SHACL profile)

### LegalEntity
| Property | Real‑world meaning |
|:--|:--|
| `legalName` | **(a)** Official name of the company as registered in the national business register. |
| `hasLegalForm` | **(b)** Type of company according to national law (e.g., B.V., Oy, S.A., GmbH). |
| `hasLegalIdentifier` | **(c)** The national registration number and the Member State where the company is registered. |
| `hasIdentifier` | **(d)** Other identifiers such as the **EUID**, **LEI**, or tax ID used for cross‑border recognition. |
| `registeredAddress` | **(e)** The official address of the registered office of the company. |
| `postalAddress` | **(f)** Postal or correspondence address if different from the registered office. |
| `registrationDate` | **(g)** Date when the company was entered in the business register. |
| `hasShareCapital` | **(h)** Information on the company’s share capital – type (subscribed/issued) and amount. |
| `hasLegalStatus` | **(i)** Current legal situation – active, dissolved, in liquidation, etc. |
| `hasActivity` | **(l)** Main business activity or object of the company (often expressed with a NACE code). |
| `hasContactPoint` | **(n)** Company contact information such as website or email. |
| `hasRepresentationRule` | **(j)** Rules on who represents the company and whether they act alone or jointly. |

---

### Identifier
| Property | Real‑world meaning |
|:--|:--|
| `schemaAgency` | Authority or register responsible for issuing the identifier (e.g., Dutch BR, GLEIF). |
| `notation` | The identifier value itself – e.g., “80234567” or “NL.BR.80234567”. |
| `schemeName` | Name of the identifier scheme – e.g., “Dutch Business Register”, “EUID”, “LEI”. |

---

### Address
| Property | Real‑world meaning |
|:--|:--|
| `fullAddress` | The complete textual form of the address used for human‑readable display. |
| `postCode` | Postal code (ZIP code) identifying the delivery area. |
| `postName` | City / municipality of the address. |
| `adminUnitLevel1` | First‑level administrative region (e.g., province, state). |
| `adminUnitLevel2` | Second‑level administrative region (e.g., municipality, district). |
| `thoroughfare` | Street name and number. |
| `locatorName` | Name of building or estate (if applicable). |
| `locatorDesignator` | Additional location designator (e.g., apartment number). |
| `postOfficeBox` | Post office box number. |
| `careOf` | “c/o” line identifying recipient or attention name. |

---

### ShareCapital
| Property | Real‑world meaning |
|:--|:--|
| `capitalType` | Specifies whether the capital is subscribed, issued, or paid‑up. |
| `totalCapitalAmount` | Monetary amount representing the declared capital. |

---

### MonetaryAmount
| Property | Real‑world meaning |
|:--|:--|
| `currency` | ISO currency code (e.g., EUR). |
| `value` | Numerical amount of money. |

---

### LegalStatus
| Property | Real‑world meaning |
|:--|:--|
| `hasCode` | **(i)** Code or label describing the company’s legal status (Active, Dissolved, etc.). |
| `date` | Date from which the current legal status applies. |

---

### CodeClass
| Property | Real‑world meaning |
|:--|:--|
| `name` | Human‑readable code name used in the EUCC (e.g., “Active”, “Suspended”). |

---

### ContactPoint
| Property | Real‑world meaning |
|:--|:--|
| `contactPage` | **(n)** Official website URL of the company or business register entry. |
| `email` | **(f)** Email address for contact or correspondence. |

---

### RepresentationRule
| Property | Real‑world meaning |
|:--|:--|
| `description` | **(j)** Narrative description of how the company may be represented. |
| `membershipBasedRule` | **(j)** Rule listing the actual persons who may represent the company. |
| `roleBasedRule` | **(j)** Rule stating which roles (e.g., Managing Director, Board Member) can represent it. |

---

### MembershipBasedRepresentationRule
| Property | Real‑world meaning |
|:--|:--|
| `definesValidMembership` | The specific persons and roles who have representation rights. |
| `minimumNumberOfMembers` | Minimum number of persons required to represent jointly. |
| `memberQuantifier` | Constraint specifying how members combine to form valid representation (e.g., jointly). |

---

### RoleBasedRepresentationRule
| Property | Real‑world meaning |
|:--|:--|
| `definesValidRole` | Defines which roles (e.g., Managing Director) are entitled to represent the company. |
| `minimumNumberOfRoleHolders` | Minimum number of role holders needed for joint representation. |
| `roleHolderQuantifier` | Specifies the quantifier for the role (e.g., one acting alone or jointly). |

---

### Membership
| Property | Real‑world meaning |
|:--|:--|
| `member` | The individual person or legal entity who is a member (e.g., director, board member). |
| `hasRole` | The official function or capacity in which the member acts. |

---

### Role
| Property | Real‑world meaning |
|:--|:--|
| `name` | Title of the role (e.g., Managing Director, Board Member). |
| `codeValue` | Code used to identify the role within the register (e.g., “MD”). |

---

### Person
| Property | Real‑world meaning |
|:--|:--|
| `fullName` | Full legal name of the natural person authorised to act. |
| `dateOfBirth` | Birth date of that person (proves uniqueness in the register). |

---

## 2. Real‑world Example (JSON)

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

---

## 3. JSON‑LD (using the compact context)

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

## 4. As a W3C Verifiable Credential (VCDM 2.x)

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
- `LegalEntity.legalName` present **(a)**
- `LegalEntity.hasLegalForm` present **(b)**
- `LegalEntity.hasLegalIdentifier` **(c)** and `LegalEntity.hasIdentifier` includes **EUID (d)**
- `LegalEntity.registeredAddress` **(e)** and `LegalEntity.postalAddress` / `hasContactPoint.email` **(f)**
- `LegalEntity.registrationDate` **(g)**
- `LegalEntity.hasShareCapital` **(h)**
- `LegalEntity.hasLegalStatus` **(i)**
- `LegalEntity.hasRepresentationRule` **(j)**
- If legal‑person representative: model via Role/Membership link **(k)**
- `LegalEntity.hasActivity` **(l)**
- *(m)* Duration — not present in the JSON extract
- `hasContactPoint.contactPage` **(n)**
- Certificate date of issue — not present in the JSON extract **(o)**

---

**Files**
- **Compact JSON‑LD context:** `eu-company-certificate-context.jsonld`  
- **This guide (Markdown):** `EU-Company-Certificate-Guide.md`
