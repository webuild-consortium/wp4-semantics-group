# Use Case Overview of LPID

Purpose: Capture the story and high-level purpose of the use case “LPID” & "PID".

## Storyline

What is the scenario being solved?
 + to define and create a PID and LPID
 + initialising a (buisiness) wallet
   

## Business Context / Motivation

Why is this attestation needed?
PID and LPID To be able to bind a person or buisiness to the wallet an do economic oprations.

We need to provide an ID for EVERY organisation or business or even economic operator, not only legal persons. We suggest to rename LPID to organisation ID, business ID or Economic Operator ID. This will also make it possible to incorporate, Shipping company, persons partnership, commercial partnership, Limited partnership and sole traders.

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
 + 

# Data Model or Knowledge Graph

Purpose: Capture the entities, attributes, and relationships.


## Entity: LPID
|Name|Description/Definition|
|--|--|
| LPID | Represents the Economic operator. So the name LPID is misleading. We propose EOID. Economic operator means any natural or legal person or public entity or group of such persons and/or entities, including any temporary association of undertakings, which offers the execution of works and/or a work, the supply of products or the provision of services on the market. |

|Attribute| Description | mandatory | private | datatype | 
|--|--|--|--|--|
| EUID | The EUID is defined as in BORIS. However a EOID can be a better name, because it is natural and also covers natural persons. | yes | no | string |
| regitered name | As stated in the registry as the statutairy name. | no | yes | string |

| Relation | Description | Left Entity | Right Entity | Left Role | Right Role | Cardinality | Optional |
|--|--|--|--|--|--|--|--|
|  |  | Hello | World | greeter | greeted | 1 1..n | no |

> **Questions to ask per relation:**


## Entity: PID
|Name|Description/Definition|
|--|--|
| PID | Represents the Economic operator. Economic operator means any natural or legal person or public entity or group of such persons and/or entities, including any temporary association of undertakings, which offers the execution of works and/or a work, the supply of products or the provision of services on the market. |

|Attribute| Description | mandatory | private | datatype | 
|--|--|--|--|--|
| - | We need harmonised attributes for the PID. People should be able to use their NP wallet as a business wallet so they can act as an Economic Operator. | yes | no | string |

| Relation | Description | Left Entity | Right Entity | Left Role | Right Role | Cardinality | Optional |
|--|--|--|--|--|--|--|--|
| (none) | The World entity has no outgoing relations in this example. | - | - | - | - | - | - |

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
| I001 | The  _Hello World_  attestation shall serve as an illustrative reference implementation to clarify the intended use of this template and to demonstrate practical dilemmas and opportunities arising at the intersection of semantics, trust, lifecycle management, and real-world usage. While not intended as a production-grade attestation, it should support analysis and discussion of how these dimensions interact within the broader EU wallet ecosystem. | Bart Bink | inspect |

## Legal and Regulatory requirements

From the directive: <link>

| No. | Requirement | Source | Verification method |
|--|--|--|--|
| L001 | The Hello World attestation is currently outside the scope of eIDAS2 compliance requirements. However, its design should not preclude future alignment with eIDAS2 trust frameworks, credential formats, or conformity assessment procedures. | eIDAS2 | review |

## Functional requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| F001 | The Hello World attestation shall be capable of being issued to any compliant digital wallet, irrespective of the wallet provider or implementation, provided that the wallet supports at least one of the supported attestation formats (JSON-LD, SD-JWT, or mDoc). The attestation should not rely on wallet-specific extensions or proprietary interfaces that would limit its interoperability. | Bart Bink | test |

## Technical requirements – e.g. security, privacy, performance, usability.
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| T001 | The issuer MUST issue the Hello World attestation as a JSON-LD-based attestation. If the recipient wallet does not support JSON-LD, the issuer MUST fall back to an SD-JWT-based attestation. If the recipient wallet does not support SD-JWT, the issuer MUST issue the attestation as an mDoc. | WEBUILD Semantic Modeling interoperability requirement. | test |

## Operational requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| O001 | The LPID should be stable over time. | WEBUILD Semantic Modeling interoperability requirement. | test |

## Governance and trust restrictions
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| G001 | The  _Hello World_  attestation shall be cryptographically bound to both the holder’s eWallet and the holder’s verified identity attestation to ensure authenticity and non-transferability.| General trust mechanism. | review |

## Open Questions / Gaps – For follow-up or design iterations.
| No. | Question | Why |
|--|--|--|
| Q001 | Can we change the name LPID to something else? LPID excliudes all organisations except legal persons.||
| Q002 | how is the LPID issued to sole traders not mentioned in the business registries? ||
| Q003 | are there any othe attributes that need to be considdered? |  |
| Q004 | how to cope with organisations/businesses not registered at any registry? ||
| Q005 | how to harmonise attributes per memberstate for sole traders for instance? | |
| Q005 | Do we need all the attributes defined for the PID? The PID will be unstable and make the wallet unactive. | |
