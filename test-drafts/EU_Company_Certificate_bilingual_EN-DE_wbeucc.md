# EU Company Certificate / EU-Unternehmenszertifikat  
*Bilingual, non‑expert friendly overview structured by Article 16b (Directive (EU) 2025/25)*

> **Traceability note.** This file is grounded in: (i) Article 16b of Directive (EU) 2025/25 (Official Journal L 2025/25, 10.1.2025), (ii) your uploaded **WE BUILD EU Company Certificate SHACL Shape (RDF)** and (iii) **NCBV 0.0.5 OWL (RDF)**.  
> Wherever a property **is not explicitly present** in the uploaded SHACL or NCBV OWL, I label it **“Proposal (not in SHACL/NBV)”** and explain the suggested alignment.

---

**EUCC Application Profile IRI:** <https://iri.suomi.fi/model/wbeucc/>

## 1. Purpose / Zweck

**EN.** The EU Company Certificate (EUCC) is a harmonised register extract issued by national business registers. It proves a company’s lawful incorporation and selected core facts in cross‑border contexts.  
**DE.** Das EU‑Unternehmenszertifikat (EUCC) ist ein harmonisierter Registerauszug der nationalen Handelsregister. Er bestätigt die rechtmäßige Gründung und ausgewählte Kerndaten in grenzüberschreitenden Situationen.

**Legal basis / Rechtsgrundlage:** See Article 16b(1)–(3) of Directive (EU) 2025/25. fileciteturn0file3

---

## 2. Content per Article 16b(2)(a–o) / Inhalt nach Artikel 16b(2)(a–o)

> **Legend.**  
> ✔ **Directive** = required by Article 16b.  
> 🔧 **Profile status** = status in your uploaded EUCC SHACL / NCBV OWL; when unclear or missing, a **Proposal** is given.

### (a) Company name / Firmenname
- **EN:** Registered legal name.  
- **DE:** Eingetragene Firma.  
- ✔ **Directive:** Art. 16b(2)(a). fileciteturn0file3  
- 🔧 **Profile status:** Use `ncbv:LegalEntity` → `ncbv:legalName` (if not present in SHACL, adopt from NCBV). **If absent in SHACL:** *Proposal (not in SHACL/NBV)*: add a node shape requiring a non‑empty string.

---

### (b) Legal form / Rechtsform
- **EN:** Legal form (e.g., GmbH, AG, BV).  
- **DE:** Rechtsform (z. B. GmbH, AG, BV).  
- ✔ **Directive:** Art. 16b(2)(b). fileciteturn0file2  
- 🔧 **Profile status:** Prefer a **code value** from a controlled list (SKOS Concept). *Proposal (not in SHACL/NBV)*: bind with `ncbv:legalForm` → range `skos:Concept` and allow national/EU codes.

---

### (c) Registration number & Member State / Registernummer & Mitgliedstaat
- **EN:** The national register number **and** the Member State of registration.  
- **DE:** Die nationale Registernummer **und** der Mitgliedstaat der Eintragung.  
- ✔ **Directive:** Art. 16b(2)(c). fileciteturn0file3  
- 🔧 **Profile status:** To align tightly with NCBV, model **both** as **identifiers** using `adms:Identifier` via `ncbv:hasIdentifier` on the company node:  
  - **Registration number** → `adms:Identifier` with `identifierType` = `"nationalRegisterNumber"` and `identifierValue` = e.g. `"HRB 123456"`.  
  - **Member State** → `adms:Identifier` with `identifierType` = `"memberStateCode"` and `identifierValue` = e.g. `"DE"` (ISO 3166‑1 alpha‑2).  
  - *This is a **Proposal (not in SHACL/NBV)** if these exact shapes/properties are not present in your EUCC SHACL. It avoids introducing bespoke datatype properties and keeps identifiers uniform.*

---

### (d) EUID of the company / EUID der Gesellschaft
- **EN:** European Unique Identifier (EUID) as defined for BRIS interconnection.  
- **DE:** Europäischer eindeutiger Identifikator (EUID) für das BRIS‑System.  
- ✔ **Directive:** Art. 16b(2)(d) and Art. 16(1) on EUID structure. fileciteturn1file9  
- 🔧 **Profile status:** Model as `adms:Identifier` (`identifierType` = `"EUID"`, `identifierValue` = e.g. `"DE.HRB.123456"`). *Proposal (not in SHACL/NBV)* if not already shaped.

---

### (e) Registered office / Satzungsmäßiger Sitz
- **EN:** Registered office.  
- **DE:** Satzungsmäßiger Sitz.  
- ✔ **Directive:** Art. 16b(2)(e). fileciteturn1file2  
- 🔧 **Profile status:** Use `locn:Address` object (e.g. locality, country). *Proposal (not in SHACL/NBV)*: property `ncbv:registeredAddress` → `locn:Address`.

---

### (f) Correspondence address / Korrespondenzanschrift
- **EN:** Contact address (email or postal).  
- **DE:** Kontaktanschrift (E‑Mail oder Postanschrift).  
- ✔ **Directive:** Art. 16b(2)(f). fileciteturn1file2  
- 🔧 **Profile status:** *Proposal (not in SHACL/NBV)*: `schema:contactPoint` or `ncbv:contactPoint` with email / postal sub‑properties.

---

### (g) Date of registration / Eintragungsdatum
- ✔ **Directive:** Art. 16b(2)(g). fileciteturn1file2  
- 🔧 **Profile status:** *Proposal (not in SHACL/NBV)*: `ncbv:registrationDate` (xsd:date).

---

### (h) Subscribed capital (if applicable) / Gezeichnetes Kapital (falls zutreffend)
- ✔ **Directive:** Art. 16b(2)(h). fileciteturn1file2  
- 🔧 **Profile status:** Use `ncbv:MonetaryAmount` with `amount` + `currency`. *Proposal (not in SHACL/NBV)* if not yet present.

---

### (i) Status of the company / Status des Unternehmens
- ✔ **Directive:** Art. 16b(2)(i). fileciteturn1file2  
- 🔧 **Profile status:** *Proposal (not in SHACL/NBV)*: controlled vocabulary (e.g., active, wound‑up, dissolved, insolvency, struck off). Range `skos:Concept`.

---

### (j) Authorised natural persons / Vertretungsberechtigte natürliche Personen
- ✔ **Directive:** Art. 16b(2)(j). fileciteturn1file2  
- 🔧 **Profile status:** *As you noted, not yet modeled in your SHACL.* **Proposal:**  
  - `ncbv:hasRepresentativePerson` (LegalEntity → Person)  
  - `ncbv:RepresentativeRole` (intermediate node) with `representationType` (sole/joint), temporal validity, and link back to principal.  
  - Capture **first names, surnames, date of birth** (or equivalent if DoB is not recorded).

---

### (k) Authorised legal persons / Vertretungsberechtigte juristische Personen
- ✔ **Directive:** Art. 16b(2)(k). fileciteturn1file2  
- 🔧 **Profile status:** *Not yet modeled.* **Proposal:**  
  - `ncbv:hasRepresentativeEntity` (LegalEntity → LegalEntity)  
  - Identifier policy: EUID if available; otherwise national registration number, both as `adms:Identifier` instances.

---

### (l) Object of the company / Unternehmensgegenstand
- ✔ **Directive:** Art. 16b(2)(l) (may use NACE). fileciteturn1file16  
- 🔧 **Profile status:** *Proposal (not in SHACL/NBV)*: `ncbv:economicActivity` with optional link to NACE `skos:Concept` + free‑text description.

---

### (m) Duration (if limited) / Dauer (falls befristet)
- ✔ **Directive:** Art. 16b(2)(m). fileciteturn1file2  
- 🔧 **Profile status:** *Proposal (not in SHACL/NBV)*: `ncbv:PeriodOfTime` with `startDate`/`endDate` or code `"unlimited"`.

---

### (n) Company website (if recorded) / Website (falls im Register erfasst)
- ✔ **Directive:** Art. 16b(2)(n). fileciteturn1file2  
- 🔧 **Profile status:** *Proposal (not in SHACL/NBV)*: `schema:url` (xsd:anyURI).

---

### (o) Date of issue / Ausstellungsdatum
- ✔ **Directive:** Art. 16b(2)(o). fileciteturn0file1  
- 🔧 **Profile status:** *Proposal (not in SHACL/NBV)*: `ncbv:issueDate` on the certificate document node.

---

## 3. Partnerships (Art. 16b(3)) / Personengesellschaften
Partnership EUCC includes (2) minus (e), (h), (j), (k) **plus** specific items (registered office/equivalent; liability/contribution; authorised partners; etc.). fileciteturn0file1

---

## 4. JSON‑LD Examples (bilingual labels kept in narrative; IRIs in Appendix)

> **Context note.** Keys below reflect the **alignment proposals** above using NCBV + ADMS Identifier. If any key is **not present** in your SHACL or NCBV OWL, treat it as **Proposal (not in SHACL/NBV)** to be added in the EUCC SHACL profile.

### 4.1 Limited Liability Company (GmbH) / Kapitalgesellschaft (GmbH)

```json
{
  "@context": "https://iri.suomi.fi/model/wbeucc/context.jsonld",
  "@type": "ncbv:LegalEntity",
  "ncbv:legalName": "Muster GmbH",
  "ncbv:hasIdentifier": [
    {
      "@type": "adms:Identifier",
      "ncbv:identifierType": "EUID",
      "ncbv:identifierValue": "DE.HRB.123456"
    },
    {
      "@type": "adms:Identifier",
      "ncbv:identifierType": "nationalRegisterNumber",
      "ncbv:identifierValue": "HRB 123456"
    },
    {
      "@type": "adms:Identifier",
      "ncbv:identifierType": "memberStateCode",
      "ncbv:identifierValue": "DE"
    }
  ],
  "ncbv:legalForm": "GmbH",
  "ncbv:registeredAddress": {
    "@type": "locn:Address",
    "locn:postName": "Berlin",
    "locn:adminUnitL1": "DE"
  },
  "ncbv:contactPoint": {
    "@type": "schema:ContactPoint",
    "schema:email": "info@muster-gmbh.de"
  },
  "ncbv:registrationDate": "2016-07-15",
  "ncbv:subscribedCapital": {
    "@type": "ncbv:MonetaryAmount",
    "ncbv:amount": "25000",
    "ncbv:currency": "EUR"
  },
  "ncbv:companyStatus": "active",
  "ncbv:hasRepresentativePerson": [ {
    "@type": "ncbv:Person",
    "ncbv:givenName": "Sabine",
    "ncbv:familyName": "Schmidt",
    "ncbv:dateOfBirth": "1980-03-21",
    "ncbv:hasRepresentativeRole": {
      "@type": "ncbv:RepresentativeRole",
      "ncbv:representationType": "sole"
    }
  } ],
  "ncbv:economicActivity": {
    "ncbv:description": "Manufacture of wood products",
    "ncbv:code": "NACE C16.10"
  },
  "ncbv:duration": "unlimited",
  "schema:url": "https://www.muster-gmbh.de",
  "ncbv:issueDate": "2025-10-21"
}
```

### 4.2 Partnership (KG) / Personengesellschaft (Kommanditgesellschaft)

```json
{
  "@context": "https://iri.suomi.fi/model/wbeucc/context.jsonld",
  "@type": "ncbv:Partnership",
  "ncbv:legalName": "Musterholz KG",
  "ncbv:hasIdentifier": [
    {
      "@type": "adms:Identifier",
      "ncbv:identifierType": "EUID",
      "ncbv:identifierValue": "DE.HRA.789101"
    },
    {
      "@type": "adms:Identifier",
      "ncbv:identifierType": "nationalRegisterNumber",
      "ncbv:identifierValue": "HRA 789101"
    }
  ],
  "ncbv:registeredAddress": {
    "@type": "locn:Address",
    "locn:postName": "Hamburg",
    "locn:adminUnitL1": "DE"
  },
  "ncbv:registrationDate": "2018-03-01",
  "ncbv:companyStatus": "active",
  "ncbv:hasRepresentativePerson": [ {
    "@type": "ncbv:Person",
    "ncbv:givenName": "Thomas",
    "ncbv:familyName": "Becker",
    "ncbv:hasRepresentativeRole": {
      "@type": "ncbv:RepresentativeRole",
      "ncbv:representationType": "generalPartner"
    }
  } ],
  "ncbv:economicActivity": {
    "ncbv:description": "Wholesale of construction timber",
    "ncbv:code": "NACE G46.73"
  },
  "ncbv:duration": "unlimited",
  "ncbv:issueDate": "2025-10-21"
}
```

---

## 5. Implementation guidance for (j) & (k) / Umsetzungshinweise für (j) & (k)

- Define **two object properties** in the EUCC SHACL profile:  
  1) `ncbv:hasRepresentativePerson` (domain `ncbv:LegalEntity`, range `ncbv:Person`) – **Proposal (not in SHACL/NBV)**.  
  2) `ncbv:hasRepresentativeEntity` (domain `ncbv:LegalEntity`, range `ncbv:LegalEntity`) – **Proposal (not in SHACL/NBV)**.  
- Introduce a reusable `ncbv:RepresentativeRole` node shape with:  
  - `representationType` (sole, joint, permanent representative, general partner),  
  - validity (`startDate`, optional `endDate`),  
  - `actsOnBehalfOf` (principal company).

These respect Article 16b data minimisation while keeping semantics consistent across use cases. fileciteturn1file11

---

## 6. Technical Appendix / Technischer Anhang (IRIs & ranges)

> **Note:** IRIs below are indicative bindings to keep main text clean. Where your uploaded EUCC SHACL already defines a property/class, use that authoritative IRI.

- **ncbv:LegalEntity** — core company node.  
- **ncbv:legalName** — xsd:string.  
- **ncbv:hasIdentifier** → **adms:Identifier**:  
  - **ncbv:identifierType** (e.g., "EUID", "nationalRegisterNumber", "memberStateCode") — xsd:string.  
  - **ncbv:identifierValue** — xsd:string.  
- **ncbv:legalForm** → `skos:Concept` (controlled list).  
- **ncbv:registeredAddress** → **locn:Address** (`locn:postName`, `locn:adminUnitL1`, `locn:thoroughfare`, etc.).  
- **ncbv:contactPoint** → **schema:ContactPoint** (`schema:email`, etc.).  
- **ncbv:registrationDate** — xsd:date.  
- **ncbv:MonetaryAmount** (`ncbv:amount`, `ncbv:currency`).  
- **ncbv:companyStatus** → `skos:Concept`.  
- **ncbv:hasRepresentativePerson** → **ncbv:Person** — **Proposal (not in SHACL/NBV)**.  
- **ncbv:hasRepresentativeEntity** → **ncbv:LegalEntity** — **Proposal (not in SHACL/NBV)**.  
- **ncbv:RepresentativeRole** (with `ncbv:representationType`, `ncbv:startDate`, `ncbv:endDate`, `ncbv:actsOnBehalfOf`) — **Proposal (not in SHACL/NBV)**.  
- **ncbv:economicActivity** → text + link to NACE `skos:Concept`.  
- **ncbv:PeriodOfTime** (duration).  
- **schema:url** (company website).  
- **ncbv:issueDate** (certificate issue date).

**Directive references used:** Art. 16b(2)(a–o), Art. 16(1) on EUID elements, Art. 16b(3) for partnerships. fileciteturn1file2 fileciteturn1file9

---

### Changelog
- 2025-10-21: First bilingual EN/DE draft aligned to Article 16b with explicit **Proposal** labels wherever SHACL/NCBV bindings were not confirmed in the uploads.

