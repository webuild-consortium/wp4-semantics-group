# Use Case Overview of EU Company Registration

Purpose: It is to capture the story and high-level purpose of the use case “presenting proof of registration of the company” as an input for the information model. The information model is the basis for the declaration of Attestation details: Application Model. The mapping will take care of the translation/casting of the Information Model to the Application Model...

This iteration is based on:

 - Rulebook Company Registration Attestation v1.2.pdf

Other sources are yet to be incorporated.

<img width="330" height="330" alt="funnel" src="../img/Funnel01_EUCR.jpg" />

Input: Company law and EUCC Data Rulebook.

> **Important:** This template is on a "need" basis. If there is nothing to mention in the workflow part of the use case, for instance, just omit the paragraph. Only use what you need to. Keep it simple and clean.

## Storyline

**What is the scenario being solved?**

- The attestation proves the registration of the company in the business register of the Member State and provides basic information on the company such as the status of the company, the type of the company, the type of activity of the company and company contact and location details.
- The CR attestation encompasses the company key attributes as stated in the Implementing Regulation 2013/138 on high-value datasets regarding the open data regulation 2019/1024.

## Business Context / Motivation

Why is this attestation needed?


## Stakeholders

When mentioning organisation, every registered Economic Operator is meant.

 - the organisation stated in the EUCR
 - the registry
 - the organisation asking for the EUCR

## Expected Outcome

**What should happen when the attestation is used?**

The EU Company Registration shall be accepted in all Member States as sufficient evidence, at the time of its issuance, of the incorporation of the company, which is held by the register in which the company is registered.

# Information Model or Knowledge Graph

Purpose: Capture the entities, attributes, and relationships.

**Entity: EOCR**
| Name | Description/Definition | vocabulary | required by |
|--|--|--|--|


**Attributes of Entity: EOCR**
|--|--|--|--|--|--|


| Relation | Description | vocabulary | Left Entity | Right Entity | Cardinality | required by |
|--|--|--|--|--|--|--|

> Questions to ask per relation:
> 

# Workflow of the Attestation

Purpose: Map the flow of actions, data, and interactions between entities.

| Actor | Role | Description |
|--|--|--|
Trigger Event: What initiates the workflow?

Post-condition: What is the result of the workflow?

Notable Interactions / Dependencies: 

# Life Cycle of the Attestation

Purpose: Capture how the attestation evolves over time.

| Stage | Description |
|--|--|
| | |

# Requirements and Constraints

Purpose: Capture explicit and implicit technical or policy requirements.


## Legal and Regulatory requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|

## Information requirements
| No. | Requirement | mandatory/optional |Source | Verification method |
|--|--|--|--|--|
| <a id="requirement-I001"></a>I001 | Entity for the register in which the organisation is registered | M | [L001](#requirement-L001) | check |

Check for a list of standard legal forms in the EU.

## Functional requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|
|  |  |  |  |

## Technical requirements – e.g. security, privacy, performance, usability.
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| <a id="requirement-T001"></a>T001 | paper issuance | [L025](#requirement-L025) |  |

## Rulebook or Operational requirements
| No. | Requirement | Source | MOC | Verification method |
|--|--|--|--|--|
| <a id="requirement-O001"></a>O001 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O002"></a>O002 | Legal entity attribute: company_type Type of the company based on ISO 20275. |  | M | ? |
| <a id="requirement-O003"></a>O003 | Legal entity attribute: company_status . This is the primary name of the company. |  | M | ? |
| <a id="requirement-O004"></a>O004 | Legal entity attribute: company_activity . This is the primary name of the company. |  | M | ? |
| <a id="requirement-O005"></a>O005 | Legal entity attribute: registration_date . This is the primary name of the company. |  | M | ? |
| <a id="requirement-O006"></a>O006 | Legal entity attribute: company_end_date . This is the primary name of the company. |  | O | ? |
| <a id="requirement-O007"></a>O007 | Legal entity attribute: company_EUID. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O008"></a>O008 | Legal entity attribute: vat_number . This is the primary name of the company. |  | O | ? |
| <a id="requirement-O009"></a>O009 | Legal entity attribute: company_contact_data . This is the primary name of the company. |  | O | ? |
| <a id="requirement-O010"></a>O010 | Legal entity attribute: registered_address . This is the primary name of the company. |  | M | ? |
| <a id="requirement-O011"></a>O011 | Legal entity attribute: postal_address . This is the primary name of the company. |  | O | ? |
| <a id="requirement-O012"></a>O012 | Legal entity attribute: branch. This is the primary name of the company. |  | O | ? |
| <a id="requirement-O013"></a>O013 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O014"></a>O014 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O015"></a>O015 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O016"></a>O016 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O017"></a>O017 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O018"></a>O018 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O019"></a>O019 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O020"></a>O020 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O021"></a>O021 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O022"></a>O022 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O023"></a>O023 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O024"></a>O024 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O025"></a>O025 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O026"></a>O026 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O027"></a>O027 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O028"></a>O028 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O029"></a>O029 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O030"></a>O030 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O031"></a>O031 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O032"></a>O032 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O033"></a>O033 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O034"></a>O034 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O035"></a>O035 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O036"></a>O036 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O037"></a>O037 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |
| <a id="requirement-O038"></a>O038 | Legal entity attribute: company_name. This is the primary name of the company. |  | M | ? |



































## Governance and trust restrictions
| No. | Requirement | Source | Verification method |
|--|--|--|--|
|  | |  |  |

## Open Questions / Gaps – For follow-up or design iterations.
| No. | Question | Why |
|--|--|--|
|  |  |  |
