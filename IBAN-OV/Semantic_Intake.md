# Use Case Overview of IBAN OV

Purpose: Capture the story and high-level purpose of the use case of the IBAN Ownership Verification attestation.

## Storyline

What is the scenario being solved?

## Business Context / Motivation

Why is this attestation needed?

## Stakeholders

## Expected Outcome

What should happen when the attestation is used?

# Information Model from the intake

Purpose: Capture the entities, attributes, and relationships.

**Entity: Hello**
|Name|Description/Definition|
|--|--|
| Hello | Represents the  _Hello_  part of  _Hello World_. It symbolizes the entity initiating a greeting. |

|Attribute| Description | mandatory | private | datatype | 
|--|--|--|--|--|
| greetingText | An example of a mandatory attribute that holds the text of the greeting. | yes | no | string |
| definition | An example of an optional, private attribute describing the greeting or its context. | no | yes | string |

| Relation | Description | Left Entity | Right Entity | Left Role | Right Role | Cardinality | Optional |
|--|--|--|--|--|--|--|--|
| greets | Expresses the relation between Hello (the greeter) and World (the greeted). | Hello | World | greeter | greeted | 1 1..n | no |

> Questions to ask per relation:
> Check whether the direction (Hello ? World) reflects the dominant
> flow of meaning.
> If both sides can have multiple relations (n?n), consider
> refactoring the relationship into a separate class (e.g.,
> GreetingEvent)

# Workflow of the Attestation

Purpose: Map the flow of actions, data, and interactions between entities.

Trigger Event: What initiates the workflow? a request from the holder’s wallet to obtain the “Hello World” attestation from the Hello Authority.

Post-condition: What is the result of the workflow? The holder’s wallet contains an active, verifiable Hello World attestation bound to the ID attestation.

Notable Interactions / Dependencies: Are there cross-border or cross-domain steps?

# Life Cycle of the Attestation

Purpose: Capture how the attestation evolves over time.

| Stage | Description |
|--|--|

# Requirements and Constraints

Purpose: Capture explicit and implicit technical or policy requirements.

## Information requirements

| No. | Requirement | Source | Verification method |
|--|--|--|--|
| I001 |  |  | inspect |

## Legal and Regulatory requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| L001 |  |  | review |

## Functional requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| F001 | |  | test |

## Technical requirements – e.g. security, privacy, performance, usability.
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| T001 | |  | test |

## Operational requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| O001 |  |  | test |

## Governance and trust restrictions
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| G001 | |  | review |

## Open Questions / Gaps – For follow-up or design iterations.
| No. | Question | Why |
|--|--|--|
| Q001 | |  |

