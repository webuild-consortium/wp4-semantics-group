# Authorised Signatories application profile

Status: draft for joint review. Profile ID: `authorised-signatories`. Shape namespace: `https://w3id.org/ebwv/profile/authorised-signatories#`.

[shapes.ttl](shapes.ttl) validates the structure shown in the [Authorised Signatories PlantUML diagram](AuthorisedSignatories.PlantUML), which describes an attestation for one legal entity and one or more authorised persons. The initial README identified an attestation Turtle file, the diagram and a possible SHACL mapping as deliverables. This draft checks RDF data against the profile. A transformation from an external attestation format requires a separate mapping.

## Source and model alignment

The diagram is the source for the fields, links and multiplicities below. Its `*` marker is treated as required and `+` as optional. An attribute marker alone gives no explicit maximum. Use-case rules stay in this profile. The [joint central ontology](../../model/webuild.ttl) currently declares supporting annotations. The table distinguishes mappings to terms in the [existing generated EBWV vocabulary](../../../docs/ebwv/vocabulary.ttl) from candidate IRIs for the future central model. All domain term IRIs below use `https://w3id.org/ebwv#`. Joint review is needed before adopting the candidates or using the profile for interoperability.

| Diagram evidence | Constraints in the draft | Existing EBWV terms selected for reuse | Candidate EBWV terms for review |
| --- | --- | --- | --- |
| [Attestation and outgoing links](AuthorisedSignatories.PlantUML#L90-L91) | Exactly one represented legal entity and at least one authorised person. The attestation is the validation entry point. | `LegalEntity` | `AuthorizedSignatories`, `AuthorizedPerson`, `hasLegalEntity`, `hasAuthorizedPerson` |
| [Legal entity, legal person and identifier](AuthorisedSignatories.PlantUML#L7-L30), [links](AuthorisedSignatories.PlantUML#L97-L98) | Exactly one legal person and one legal entity identifier record per represented legal entity. The legal name, legal form and EUID are required. LEI and tax identifier are optional. | `LegalPerson`, `LegalEntityIdentifier`, `legalName`, `legalForm`, `lei` | `hasLegalPerson`, `hasLegalEntityIdentifier`, `euid`, `taxIdentifier` |
| [Authorised person and personal details](AuthorisedSignatories.PlantUML#L13-L19), [natural person](AuthorisedSignatories.PlantUML#L39-L43), [links](AuthorisedSignatories.PlantUML#L92-L96) | Each authorised person record links to one natural person, one role, one birthplace and one citizenship code entry. Given name, family name and date of birth are required. The date uses `xsd:date`. An identifying document is optional and singular in the draft. | `NaturalPerson`, `givenName`, `familyName`, `dateOfBirth` | `hasNaturalPerson`, `hasSignatoryRole`, `hasBirthPlace`, `hasCitizenshipCountry`, `hasIdentifyingDocument` |
| [Role and representation](AuthorisedSignatories.PlantUML#L45-L48), [codes](AuthorisedSignatories.PlantUML#L62-L65), [link](AuthorisedSignatories.PlantUML#L99) | A role name is optional. Each role has one representation code entry. Its code is `SOLE` or `JOINT`. | | `SignatoryRole`, `roleName`, `representationType` |
| [Birthplace and code lists](AuthorisedSignatories.PlantUML#L50-L54), [code entries](AuthorisedSignatories.PlantUML#L67-L77), [links](AuthorisedSignatories.PlantUML#L100-L101) | A birthplace has a required locality and one country code entry. A region code entry is optional and singular in the draft. | | `Place`, `locality`, `hasCountry`, `hasRegion` |
| [Identifying document](AuthorisedSignatories.PlantUML#L32-L37), [document type codes](AuthorisedSignatories.PlantUML#L79-L83), [links](AuthorisedSignatories.PlantUML#L102-L103) | When a document is provided, it has a document number, one document type code entry, one issuing country code entry and an expiry date of type `xsd:date`. | | `IdentifyingDocument`, `documentNumber`, `documentType`, `issuingCountry`, `expiryDate` |

Code entries are RDF resources. The draft uses `skos:notation` for one string code and `skos:prefLabel` for the name. Citizenship, birthplace country and issuing country use the diagram's three-letter format. The existing EBWV `citizenship` property instead expects a literal and uses an alpha-2-based datatype. The proposed `hasCitizenshipCountry` preserves the diagram's link to a code entry. Country and LEI checks cover lexical format. Checking country code membership, LEI check digits or registry status would require separate rules and reference data. [ISO 3166 glossary](https://www.iso.org/glossary-for-iso-3166.html) · [GLEIF LEI data dictionary](https://www.gleif.org/en/lei-data/access-and-use-lei-data/gleif-data-dictionary)

## Open decisions

- **Identifying document and region.** The attribute lists mark both links optional. The lines show a target multiplicity of one. The draft uses zero or one, pending review.
- **Signatory list.** The draft reads the list directly from the attestation, based on the explicit `1..n` link. The legal entity also lists a required `hasAuthorisedPersons` field without a separate association. Confirm whether the two paths are intended to coexist and how they would relate. Reverse multiplicities are outside the forward validation of an attestation and its linked data.
- **Legal entity and legal form.** Confirm the diagram's separate legal entity and legal person records and the use of the existing EBWV concepts for both. The diagram leaves the legal form value type open. The draft uses the string representation from the selected EBWV term.
- **Code lists and joint representation.** The diagram leaves the accepted region and document type lists open. The draft checks that these entries contain a code and a name. It checks `SOLE` or `JOINT` on each role. It leaves open how a signing group is identified and how the required combination of signers is determined.
- **Rulebook and use-case ID.** The diagram refers to a rulebook without a version or clause reference. Confirm the authoritative rulebook and project use-case ID before treating this as a normative profile.

## Example validation

Supply an attestation node typed `ebwv:AuthorizedSignatories` and the linked records in the RDF graph. pySHACL starts from that class and follows the declared links. A graph without a target can conform without evaluating an attestation. The fixtures use synthetic data and provide the required types directly so validation works without additional inference.

| File | Expected result |
| --- | --- |
| [minimum.ttl](examples/valid/minimum.ttl) | Conforms with one signatory, a `SOLE` representation code and the optional fields omitted. |
| [joint-with-document.ttl](examples/valid/joint-with-document.ttl) | Conforms with two signatories and a `JOINT` representation code. One signatory supplies an identifying document and a birthplace region. |
| [missing-authorized-person.ttl](examples/invalid/missing-authorized-person.ttl) | Fails because the attestation has no authorised person. |
| [invalid-representation-code.ttl](examples/invalid/invalid-representation-code.ttl) | Fails because `SHARED` falls outside the allowed representation codes. |
| [invalid-country-code.ttl](examples/invalid/invalid-country-code.ttl) | Fails because the citizenship code has two letters. |
| [document-without-expiry-date.ttl](examples/invalid/document-without-expiry-date.ttl) | Fails because a supplied identifying document lacks its expiry date. |

The project quality suite validates these examples. See the [application profile instructions](../README.md#validation-and-review).
