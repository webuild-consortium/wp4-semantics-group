# EU Company Certificate — Human-Readable Guide

> **Goal:** Prove that a company is legally incorporated in a Member State of the EU and provide reliable, harmonised information about its identity, registration, legal form, and representation.

- **Legal Entity** = the company registered in a Member State.
- **Identifier** = official ID such as national register number, EUID, or LEI.
- **Legal Form** = company type (e.g., Limited Liability Company, B.V., Oy, S.A.).
- **Registered Address** = official address where the company is domiciled.
- **Legal Status** = whether the company is active, dissolved, or under liquidation.
- **Activity** = main business object or NACE-coded activity.
- **Representation Rule** = how and by whom the company can act or sign.

---

## 1. Classes and Properties (from the SHACL profile)

### LegalEntity
- `legalName` *(string, 1..1)* — company name  
- `hasLegalForm` → **LegalForm** *(1..1)*  
- `hasLegalIdentifier` → **Identifier** *(1..1)*  
- `hasIdentifier` → **Identifier** *(0..n)*  
- `registeredAddress` → **Address** *(1..1)*  
- `registrationDate` *(date, 1..1)*  
- `hasLegalStatus` → **LegalStatus** *(1..1)*  
- `hasActivity` → **Activity** *(1..1)*  
- `hasShareCapital` → **ShareCapital** *(0..1)*  
- `hasContactPoint` → **ContactPoint** *(0..n)*  
- `hasRepresentationRule` → **RepresentationRule** *(0..n)*

### Identifier
- `schemaAgency` *(string)* — issuing register or authority  
- `schemeName` *(string)* — name of the identification scheme (e.g., EUID)  
- `notation` *(string)* — actual ID value  

### Address
- `fullAddress` *(string)*  
- `postCode`, `postName`, `adminUnitLevel1`, `adminUnitLevel2` *(optional)*  

### LegalStatus
- `hasCode` *(string)* — e.g., Active, Dissolved  
- `date` *(date)* — status date  

### RepresentationRule
- `description` *(string)* — free-text explanation  
- `membershipBasedRule` → **MembershipBasedRepresentationRule** *(0..1)*  

### MembershipBasedRepresentationRule
- `definesValidMembership` → **Membership** *(1..n)*  

### Membership
- `member` → **Person** *(1..n)*  
- `hasRole` → **Role** *(1..n)*  

### Person
- `fullName` *(string)*  
- `dateOfBirth` *(date)*  

### Role
- `name` *(string)*  
- `codeValue` *(string)* — e.g., Managing Director  

---

## 2. Real-world Example (JSON)
Dutch-style EU Company Certificate reflecting Article 16b points (a–j):

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
    "registrationDate": "2018-04-06",
    "hasLegalStatus": {
      "hasCode": { "name": "Active" },
      "date": "2025-09-12"
    },
    "hasActivity": {
      "naceCode": "C16.23",
      "naceDescription": "Manufacture of other builders' carpentry and joinery"
    },
    "hasShareCapital": {
      "capitalType": "subscribed",
      "totalCapitalAmount": [{ "currency": "EUR", "value": 100000 }]
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

**How to read it:**
- `legalName` → Article 16b(a)
- `hasLegalForm` → Article 16b(b)
- `registeredAddress` → Article 16b(c)
- `hasLegalIdentifier` → Articles 16b(d–f)
- `registrationDate` → Article 16b(g)
- `hasLegalStatus` → Article 16b(h)
- `hasActivity` → Article 16b(i)
- `hasRepresentationRule` → Article 16b(j)

---

## 3. JSON-LD (using the compact context)

Use this context file in your project:
```
eu-company-certificate-context.jsonld
```

Example JSON-LD instance:

```json
{
  "@context": "eu-company-certificate-context.jsonld",
  "@type": "wbeucc:EUCompanyCertificate",
  "LegalEntity": {
    "legalName": "Innovative Timber Structures B.V.",
    "hasLegalForm": { "name": "Besloten Vennootschap (Private Limited Liability Company)" },
    "hasLegalIdentifier": {
      "schemaAgency": "NL-BR",
      "notation": "80234567",
      "schemeName": ["Dutch Business Register"]
    },
    "registeredAddress": {
      "fullAddress": ["Keizersgracht 221, 1016 DV Amsterdam, Netherlands"]
    },
    "registrationDate": "2018-04-06",
    "hasLegalStatus": {
      "hasCode": { "name": "Active" },
      "date": "2025-09-12"
    },
    "hasActivity": {
      "naceCode": "C16.23",
      "naceDescription": "Manufacture of other builders' carpentry and joinery"
    },
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

## 4. As a W3C Verifiable Credential (VCDM 2.x)

```json
{
  "@context": [
    "https://www.w3.org/ns/credentials/v2",
    {
      "wbeucc": "https://iri.suomi.fi/model/wbeucc/"
    }
  ],
  "type": ["VerifiableCredential", "EUCompanyCertificateCredential"],
  "issuer": "did:web:register.example.nl",
  "validFrom": "2025-09-12T00:00:00Z",
  "credentialSubject": {
    "id": "did:example:company-innovativetimber",
    "EUCompanyCertificate": {
      "legalName": "Innovative Timber Structures B.V.",
      "hasLegalIdentifier": {
        "schemaAgency": "NL-BR",
        "notation": "80234567"
      },
      "hasIdentifier": [
        { "schemaAgency": "EU", "notation": "NL.BR.80234567" }
      ],
      "registrationDate": "2018-04-06",
      "hasLegalStatus": { "hasCode": { "name": "Active" } },
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
- `LegalEntity.legalName` present (a)
- `LegalEntity.hasLegalForm` present (b)
- `LegalEntity.registeredAddress` present (c)
- `LegalEntity.hasLegalIdentifier` and `hasIdentifier` (d–f)
- `LegalEntity.registrationDate` (g)
- `LegalEntity.hasLegalStatus` (h)
- `LegalEntity.hasActivity` (i)
- `LegalEntity.hasRepresentationRule` (j)

---

**Files**
- **Compact JSON-LD context:** `eu-company-certificate-context.jsonld`  
- **This guide (Markdown):** `EU-Company-Certificate-Guide.md`
