# Use Case Overview of BWOID

Purpose: Capture the story and high-level purpose of the use case of the European Business Wallet Owner ID.

## Storyline

What is the scenario being solved?

The “LPID” & "PID" were the candidates for the attestations to initialise the wallet. At least for the LPID and the business wallet the LPID was too restricted. The LP in LPID stand for Legal Person. And because not all business wallet owners will be legal persons, we need a new term. The [Proposal for a Regulation on the establishment of European Business Wallets](https://digital-strategy.ec.europa.eu/en/library/proposal-regulation-establishment-european-business-wallets) solves this issue by introducing the European Business Wallet Owner ID.

## Business Context / Motivation

Why is this attestation needed?
The EBWOID is the attestation that wil be bouwned to the wallet so the Economis Operator (EO) or Public Sector Body (PSB) is the owner of the wallet. The owner organisation is one of three kinds:
 - Economic Operators (EO): This is a broad category encompassing various entities acting in a commercial or professional capacity
 - Public Sector Bodies (PSB): This group includes national, state, regional, or local authorities, bodies governed by public law, or associations formed by these entities. It also includes private entities mandated by one or more of these bodies to provide public services, when acting under that mandate.
 - Union Entities: These are a specific type of Public Sector Body (PSB). They are defined as Union institutions, bodies, offices and agencies set up by or pursuant to the Treaty on European Union, the Treaty on the Functioning of European Union, or the Treaty establishing the European Atomic Energy Community.

The EBWOID will have two attributes, an ID and the registered name of the organisation. For organisations registered at a business registry the organisation is attributed a European Unique Identifier (EUID) in accordance with Directive (EU) 2017/1132 (or Directive (EU) 2015/849).
If a European Unique Identifier (EUID) has not been attributed to an economic operator or public sector body, a unique identifier must be created according to a specific process defined through implementing acts. The "how" of this creation process relies on two key aspects: the designation of authentic national data sources and the detailed technical instructions provided by the European Commission. The implementing acts will establish the structure and technical specifications of this identifier, with the goal of ensuring Union-wide uniqueness and interoperability.

If the public sector body is a Union entity (a Union institution, body, office, or agency), the Commission shall create and attribute a unique identifier to that Union entity in accordance with the implementing acts.

## Stakeholders

authority or government
issuer,
holder,
verifier,
relying party,
etc.

## Expected Outcome

What should happen when the attestation is used?
 + initialised (business) wallet for any member state, so the wallet can receive other attestations for the economic operator.

# Data Model or Knowledge Graph

Purpose: Capture the entities, attributes, and relationships.

Owner Attestation – Source and Scope of Information

The Owner Attestation shall contain two attributes: (1) the official organisational identifier as registered in the competent business registry, and (2) the official registered name of the organisation. These attributes constitute an authoritative excerpt of the organisation’s registered data as held by the official registration authority. The attestation does not encompass the full set of information maintained in the business registry; rather, it provides a verifiable subset issued directly by, or obtained in a trusted manner from, the competent registry office. The information included in the Owner Attestation MUST be derived solely from the official records of the registration authority to ensure accuracy, authenticity, and trustworthiness.


## Entity: EBWOID
|Name|Description/Definition|
|--|--|
| EBWOID | Represents the Economic operator or Public Sector Body. (So the name LPID is misleading. We proposed EOID. The EU proposes EBWOID. owner ID works for any natural or legal person or public entity or group of such persons and/or entities, including any temporary association of undertakings, which offers the execution of works and/or a work, the supply of products or the provision of services on the market.|

|Attribute| Description | mandatory | private | datatype | 
|--|--|--|--|--|
| EUID | Here the EUID covers the EUID and the ID issued by, or on behalf of, the commission. In case of the EUID, it is defined as in BORIS. The ID provided by the commission has not yet been fromalised. It would be obvious to follow the same format of the EUID. | yes | no | string |
| registered name | As stated in the registry as the statutairy name. | no | yes | string |

| Relation | Description | Left Entity | Right Entity | Left Role | Right Role | Cardinality | Optional |
|--|--|--|--|--|--|--|--|
|  |  |  |  |  |  |  |  |

> **Questions to ask per relation:**
> Check whether the direction reflects the dominant flow of meaning.
> If both sides can have multiple relations (n?n), consider refactoring the relationship into a separate class.

# Workflow of the Attestation

Purpose: Map the flow of actions, data, and interactions between entities.

| Actor | Role | Description |
|--|--|--|
| Hello Authority | issuer | The trusted party that creates and issues the Hello World attestation. It defines the semantics, attributes, and relation (“greets”) between the entities Hello and World. It also manages issuance, signing, and potential revocation. |
| Wallet Owner | holder | The user (or test persona) who receives the Hello World attestation in their EU Digital Identity Wallet. The holder stores, manages, and can present the attestation when needed. |
| EU business Wallet | Wallet | The technical component used by the holder to receive, store, and present the attestation. It handles workflow and format negotiation (JSON-LD, SD-JWT, mDoc) and enforces binding with the holder’s ID attestation. |
| Verifier | relying party | The entity that requests and verifies the Hello World attestation to confirm the claim “Hello greets World” is valid and trustworthy. It validates the signature, the wallet binding, and the issuer’s trust status. |
| Trust Registry | governance authority | Maintains the trust list or framework under which the Hello World issuer (Hello Authority) is recognized as trustworthy. It ensures that the attestation can be verified across systems and jurisdictions. |
| Attestation Registry | registry | Stores or indexes attestations for verification (if used in your architecture). |
| Revocation Service | revocation service | Manages lifecycle events, such as the deactivation of the Hello World attestation. |

Trigger Event: What initiates the workflow? a request from the holder’s wallet to obtain the “Hello World” attestation from the Hello Authority.

Post-condition: What is the result of the workflow? The holder’s wallet contains an active, verifiable Hello World attestation bound to the ID attestation.

See Figure 2 for a simplified overview.

![Swimlane 1](https://www.plantuml.com/plantuml/png/ZLJDaXet4BxhAReuh6SgIt6VpO-niIjR5SSkMDkLAYvQgHaKX3HfQMP2Ggho3dd3F4ca4R0C2snEZAJkhx_kxsjUEy_9rslDlF8QOV0ZQctXgoKjOUmzXdUlh85___u7tXavz7OOVcB0Qg5jEs3i5RorsX98N2YZOh23H-vGGaZRs9f0QEuSICLBucl6t4gPYeTFuCAhHlaD_Ca0tbYII0bhmcarHHbktrlZJ-_USB4goTP6ffUVLBdqlqJYBVlh2DvOZm7wQiB_Bzo3TgrQQsxm2lE7ED2hbLD8B7GsDy5Uvi29RDiHE8q9cdns-3JUEFfZrWwo0E6JM3aqYiDsBBobBJngArOk07HdLy0Crznu9U23bQYHRY5PP5pxfQM8djqxLoFbuSLg6ICcgbIUQ_ZAjKP_2r-Gr4B5bmUgdOSfbifvsepU1rRO1Y_TXhl6YkIr6LAZ1Dxs3BZFWSnMyOBhdB5jgWYZNIdus1gaBUjSpOe7KcM9L8Jat-g0D3V7_Xu0VyA_2s1zsbjMl5sYM46Re6_cvdu23TTAXgxlc5f0zYMUViZ1Bz50zgs8EXGx7RxVeCiPQeVFNepDMJ55W-tSF252e6qhXaQgHNXEb7VJBWdHkyGxKhsaGI3TSU8UWHB27Ii-4GQziTzlCLEbERwQcnjmw24UQmVVGOVPbNikJYXq7xSz5Fi3zoc4mfASc-m0COuMn3nYd1Cpe7pSgQatGDqjKe_dzMOdg0C-WUgelYZep5l2qwYzEo6RejueKy8dJduJuVSYL8GEpNvCcLt0uBakW_oyYQo9kV0D24BkiGUMn8d7cDkhVoob2rA5YHB23OGB3kkuZ36blr0mWiDATVITrGscwH3u67j9pcJslP9P4cuK8rSeHtFpxlTAKVYQrHMIGuaoFqFvi1Gm_dcoK__gVW0KOo6myZrLBgyDGEZgLnGdyMbfs2iO3eTmr5x5_H8opQEhi47ZynXnrLAfvJxy-Obzhf8uUxFlXdNM1LCKg9f3i5XoK-BTt7m8lKLZI3HncU3Uy6veBnXpLZ-ww4tZGKJT72ouqj1q6MB7ElsVl4OZwxN-3m00)
Figure 2 The swim lane diagram Hello World issuance and revocation.

Notable Interactions / Dependencies: Are there cross-border or cross-domain steps?

# Life Cycle of the Attestation

Purpose: Capture how the attestation evolves over time.

| Stage | Description |
|--|--|
| Creation / Issuance | Who issues it and under what conditions? The Hello Authority (trusted issuing entity). Preconditions: The holder’s wallet is activated and bound to a valid ID. |
| Usage / Presentation | How and where it’s presented? The attestation may be presented to any Verifier who requests proof that the Hello Authority issued a valid greeting (symbolically representing any verifiable claim). The wallet creates a verifiable presentation (potentially with selective disclosure). |
| Update / Renewal | Can it change or expire? The Hello World attestation is static by design - it has no mutable attributes. However, if either the schema changes or the Hello Authority updates its signing keys or trust policy, then a new version of the attestation must be issued. Optionally, an expiry date can be set to force periodic renewal for testing lifecycle behavior. |
| Revocation / Expiry | How is it invalidated or replaced? The Hello World attestation can be revoked by the issuer or automatically expire after a predefined validity period. |
| Archiving / End-of-life Handling | What happens after expiry or revocation? The wallet may retain a cryptographic proof of the attestation (hash or record) for audit or traceability purposes, while marking it as expired or revoked. The issuer may archive metadata (e.g., issuance date, revocation timestamp, format used) for audit trails, compliance testing, or statistical reporting complying to privacy rules. In demonstrative settings, archived attestations can serve as test material for verifying lifecycle management and revocation interoperability. |

# Requirements and Constraints

Purpose: Capture explicit and implicit technical or policy requirements.

## Information requirements

| No. | Requirement | Source | Verification method |
|--|--|--|--|


## Legal and Regulatory requirements

From the directive: COM_2025_838_1_EN_ACT_part1

| No. | Requirement | Source | Verification method |
|--|--|--|--|
| L001 | Providers of EBWOID (qualified trust service providers, public sector bodies, or the Commission) shall issue it to European Business Wallet owners. | Aticle 8 1, 2. | review |
| L002 | Where EBW owners are Union entities, the Commission shall issue the EBWOID. | Aticle 8 1, 2. | review |
| L003 | It shall contain at least the official name of the economic operator or public sector body, as recorded in the relevant register or official record. | Aticle 8 5, 6. | review |
| L004 | It shall contain at least the relevant unique identifier attributed in accordance with Article 9. | Aticle 8 5, 6. | review |
| L005 | If the economic operator has been attributed a European Unique Identifier (EUID), that identifier shall be used as the unique identifier for EBWOID. | Aticle 9 2, 3, 4. | review |
| L006 | EUROPEAN BUSINESS WALLETS UNIT AUTHENTICATION Access to the European Business Wallets Unit shall be granted only after the European Business Wallets user has been successfully authenticated by means of either: (1) a notified electronic identification (eID) means in accordance with Article 6 of Regulation (EU) No 910/2014, fulfilling at least the requirements for a substantial level of assurance as defined in Article 8 of that Regulation and further specified in Commission Implementing Regulation (EU) 2015/1502; or (2) an alternative authentication mechanism recognised as equivalent and fulfilling at least the requirements for a substantial level of assurance as defined in Article 8 of Regulation (EU) No 910/2014 and further specified in Commission Implementing Regulation (EU) 2015/1502. Until such authentication has been completed, no functionality of the European Business Wallets Unit or of any other functionalities shall be made accessible to the Wallets user. | ANNEX | review |
| L007 | The EBWOID shall be issued in a format compliant with one of the standards listed in Annex II of Commission Implementing Regulation (EU) 2024/2979. | Aticle 8 3. | review |
| L008 | The EBWOID issued by the Commission shall have the same legal effect as QEAA and EAA issued by, or on behalf of, a public sector body responsible for an authentic source. | | review |
| L009 | The EBWOID issued to Business Wallets units must comply with the technical specifications set out in the implementing acts. | 16 | review |
| L010 | When issued to economic operators established outside the Union, identity proofing and verification must fulfil one or a combination of the methods set out in Article 24(1a) of Regulation (EU) No 910/2014. | Article 8 4, 5, 6 | review |

## Functional requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| F001 |  | |  |

## Technical requirements – e.g. security, privacy, performance, usability.
| No. | Requirement | Source | Verification method |
|--|--|--|--|


## Operational requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| O001 | The European Business Wallet Owner Identification Data (EBWOID) must be stable in time primarily to ensure legal certainty, trust, and the reliable functioning of cross-border systems | following multiple legal requirements. | test |

## Governance and trust restrictions
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| G001 | | | review |

## Open Questions / Gaps – For follow-up or design iterations.
| No. | Question | How is it resolved? |
|--|--|--|
| Q001 | Can we change the name LPID to something else? LPID excliudes all organisations except legal persons.| Yes, resolved by Proposal for a Regulation on the establishment of European Business Wallets. |
| Q002 | how is the LPID issued to sole traders not mentioned in the business registries? | Resolved by Proposal for a Regulation on the establishment of European Business Wallets.|
| Q003 | are there any othe attributes that need to be considdered? | No, resolved by Proposal for a Regulation on the establishment of European Business Wallets. |
| Q004 | how to cope with organisations/businesses not registered at any registry? | Resolved by Proposal for a Regulation on the establishment of European Business Wallets. |
| Q005 | how to harmonise attributes per memberstate for sole traders for instance? | Resolved by Proposal for a Regulation on the establishment of European Business Wallets.|
| Q005 | Do we need all the attributes defined for the PID? The PID will be unstable and make the wallet unactive. | |
