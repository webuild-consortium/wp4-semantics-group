# Semantic intake template

# Use Case Overview of EBWOID

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

The stakeholders are mentioned with their roles:
 - authority or government providing the authentic source.
 - a QTSP as issuer
 - an EO or PSB as owner

## Prerequisites
 - The Wallet owner already has a wallet and needs a EBWOID to activate it.

## Expected Outcome

What should happen when the attestation is used?
 + initialised (business) wallet for an EO or PSB from any member state, so the wallet can receive other attestations for the economic operator.

# Informaion Model from the intake

Purpose: Capture the entities, attributes, and relationships.

Owner Attestation - Source and Scope of Information

The Owner Attestation shall contain two attributes: (1) the official organisational identifier as registered in the competent business registry, and (2) the official registered name of the organisation. These attributes constitute an authoritative excerpt of the organisation’s registered data as held by the official registration authority. The attestation does not encompass the full set of information maintained in the business registry; rather, it provides a verifiable subset issued directly by, or obtained in a trusted manner from, the competent registry office. The information included in the Owner Attestation MUST be derived solely from the official records of the registration authority to ensure accuracy, authenticity, and trustworthiness.

![](https://img.plantuml.biz/plantuml/png/NP1FImD13CNl-HIXUb9MH4zkBrNQGq4H117j7nXsihkXivcIYIYM_Uu6fI2UajyBURnaLYoelGy9Z2qHBgNDEWJEWWyvKi9Myu3M4x9Os150aq8fkBXxULpEyG1ujdZsfaQE9COjaxgcr74nKeeeOI0V5rEM3aO0oKPeUO-vFThKEFbnsGVp9N7UhcwhjytXQlojr-DwVO6hK7qvNbOtctFdltWw-PViv9wxtbuffVmnJInKpuFkdYXEZJxj202zvyQ6jKb-suma-Y--0G00)

## Entity: EBWOID
|Name|Description/Definition|
|--|--|
| EBWOID | Represents the Economic operator or Public Sector Body. So the name LPID is misleading. We proposed EOID. The EU proposes EBWOID. owner ID works for any natural or legal person or public entity or group of such persons and/or entities, including any temporary association of undertakings, which offers the execution of works and/or a work, the supply of products or the provision of services on the market.|

|Attribute| Description | mandatory | private | datatype | 
|--|--|--|--|--|
| EUID | Here the EUID covers the EUID and the ID issued by, or on behalf of, the commission. In case of the EUID, it is defined as in BORIS. The ID provided by the commission has not yet been fromalised. The EUID follows the patern: ^[A-Z]{2}[A-Z]{3}\\. [a-zA-Z0-9]+\\.[a-zA-Z0-9]+$ | yes | no | string |
| registered name | As stated in the registry often stated as the statutairy name. | no | yes | string |

# Workflow of the Attestation

Purpose: Map the flow of actions, data, and interactions between entities.

| Actor | Role | Description |
|--|--|--|
|  |  |  |

Trigger Event: What initiates the workflow?

Post-condition: What is the result of the workflow?

See Figure 2 for a simplified overview.

Notable Interactions / Dependencies: 

# Life Cycle of the Attestation

Purpose: Capture how the attestation evolves over time.

| Stage | Description |
|--|--|
|  |  |

# Requirements and Constraints

Purpose: Capture explicit and implicit technical or policy requirements.

## Information requirements

| No. | Requirement | Source | Verification method |
|--|--|--|--|
| I001 | There will be an Entity EBWOID | L000, L003, L004 | check |
| I002 | The EBWOID shall have two attributes, an EUID or equivalent and the registered name. | L003, L004, L005 | check |
| I003 | The EUID or equivalent shall be unique for all memberstates. | L000, L005  | check |

## Legal and Regulatory requirements

From the directive:
 - [1. COM(2025) 838 - Proposal for a Regulation on the establishment of European Business Wallets](https://ec.europa.eu/newsroom/dae/redirection/document/121736)
 - [2. COM(2025) 838 - Annex to the Proposal](https://ec.europa.eu/newsroom/dae/redirection/document/121735)
 - [3. SWD(2025) 837 - Staff Working Document accompanying the Proposal](https://ec.europa.eu/newsroom/dae/redirection/document/121737)

| No. | Requirement | Source | Verification method |
|--|--|--|--|
| L000 | EBWOID is necessary to establish the owner's identity, trust and traceability. | Article 3.1, 5, 114(37) | review |
| L001 | Providers of EBWOID (qualified trust service providers, public sector bodies, or the Commission) shall issue it to European Business Wallet owners. | Aticle 8 1, 2. | review |
| L002 | Where EBW owners are Union entities, the Commission shall issue the EBWOID. | Aticle 8 1, 2. | review |
| L003 | The EBWOID shall contain at least the official name of the economic operator or public sector body, as recorded in the relevant register or official record. | Aticle 8 5, 6. | review |
| L004 | The EBWOID shall contain at least the relevant unique identifier attributed in accordance with Article 9. | Aticle 8 5, 6. | review |
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
| O001 | The European Business Wallet Owner Identification Data (EBWOID) must be stable in time primarily to ensure legal certainty, trust, and the reliable functioning of cross-border systems | following multiple legal requirements and stated in large scale project EWC | test |

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
