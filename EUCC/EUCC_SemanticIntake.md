# Use Case Overview of EU Organisation Certificate (former EUCC)

Purpose: Capture the story and high-level purpose of the use case “issuing and using the EUCC”.

This iteration is based on:
 - [Publication amending existing EU company-law directives (Directives 2009/102/EC and 2017/1132) to expand and improve the use of digital tools and digital processes in company law](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32025L0025&qid=1762615804836). In article 16b it describes the EU Company Certificate. Suggested to rename to EU Organisation Certificate, EUOC.
 - The [EU Company Certificate Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md)

Other sources are yet to be incorporated.

<img width="330" height="330" alt="funnel" src="https://raw.githubusercontent.com/webuild-consortium/wp4-semantics-group/ac925c6c1333c1c9fe05b56383b82a986c9c037a/img/Funnel_02.jpg" />

Input: Company law and EUCC Data Rulebook.


> Note: The acronym EUCC is already [taken](https://certification.enisa.europa.eu/certification-library/eucc-certification-scheme_en) and may cause misunderstandings if used here as well. So some proposals:
> Replacing the word Company with:
> Business, Enterprise, Firm, Organisation, Entity, Legal Person, Commercial, Registration
>
> Replacing the word Certificate with:
> Attestation, Excerpt, Act, Warrant, Deed, Record, Register, Instrument, Grant, Certificate.
>
> Some candidates:
> - EU Business Excerpt
> - EU Business Warrant
> - EU Organisation Excerpt
> - EU Organisation Warrant

## Storyline

**What is the scenario being solved?**

- Member States shall ensure that the registers issue the EU Company Certificates regarding the companies listed in Annexes II and IIB.


## Business Context / Motivation

**Why is this attestation needed?**

- The goal of the EUCC attestation is to have a common standard for European legal entities to exchange. The EUCC attestation will be used by companies in the EWC pilots. This attestation allows companies to share, with a high level of security, information about their companies. This is also a way for relying parties to ensure that they only verify one standard attestation, which allows machine automation and simplifies human comprehension.

## Stakeholders

When mentioning organisation, every registered Economic Operator is meant.

 - the organisation stated in the EUCC
 - the registry
 - the organisation asking for the EUCC

## Expected Outcome

**What should happen when the attestation is used?**

The EU Company Certificate shall be accepted in all Member States as sufficient evidence, at the time of its issuance, of the incorporation of the company and of the information listed in paragraphs 2 and 3 of this Article, respectively, which is held by the register in which the company is registered.

# Data Model or Knowledge Graph

Purpose: Capture the entities, attributes, and relationships.

**Entity: EOCC**
| Name | Description/Definition | vocabulary | required by |
|--|--|--|--|
| EOCC | A standardised, machine-verifiable proof of a company’s incorporation and registered company information, to be presented by a Wallet User to an RP in cross-border and domestic contexts. | - | [O039](#requirement-O039) |
| Address | an identification of the fixed location of a geographic place | [Address](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#Address) | [L008](#requirement-L008), [O013](#requirement-O013) |
| NaturalPerson | the designation of a Person in a legal and business context | [Address](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#NaturalPerson) | [O003](#requirement-O003) |
| LegalPerson |  | [Address](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#LegalPerson) | [O004](#requirement-O004) |
| LegalEntity |  | [Address](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#LegalEntity) | [O005](#requirement-O005) |
| LegalRepresentative |  | [Address](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#LegalRepresentative) | [O006](#requirement-O006) |
| SignatoryRights |  | [Address](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#SignatoryRights) | [O007](#requirement-O007) |

| Attribute | Description | vocabulary | MOC | private |required by | 
|--|--|--|--|--|--|
| fullAddress | the complete address written as a string. | [fullAddress](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#fullAddress) | M | No | [O029](#requirement-O029) |
| attestationLegalCategory | One of EAA, Pub-EAA or QEAA | [attestationLegalCategory](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#attestationLegalCategory) | M | No | [O009](#requirement-O009) |
| legalName | the name under which the legal entity is legally registered | [legalName](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#legalName) | M | No | [O009](#requirement-O009) |
| legalIdentifier | Unique ID for the legal person in the EUID structure. | [legalIdentifier](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#legalIdentifier) | M | No | [O010](#requirement-O010) |
| legalFormType | Legal form of the company. | [legalFormType](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#legalFormType) | M | No | [O011](#requirement-O011) |
| registrationMemberState | The member state where the company is registered (Alpha-2 country code). | [registrationMemberState](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#registrationMemberState) | M | No | [O012](#requirement-O012) |
| dateOfRegistration | the date on which the legal entity has registered in some jurisdiction for regulatory and / or for tax purposes | [dateOfRegistration](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#dateOfRegistration) | M | No | [O014](#requirement-O014) |
| pick up from here |  | |  |  |  |
| legalPersonStatus | Status of the company as defined in national law. #TODO: Can we limit this to the BRIS accepted groups for a better international representative approach? | [legalPersonStatus](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#legalPersonStatus) | M | No | [O015](#requirement-O015) |
| legalPersonActivity | Main activity of the company (NACE). | [legalPersonActivity](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#legalPersonActivity) | M | No | [O016](#requirement-O016) |
| legalRepresentative | Information about the natural or legal person(s) authorized to represent the company. See section 2.4. At least one is required. | [legalRepresentative](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#legalRepresentative) | M | No | [O017](#requirement-O017) |
| shareCapital | Amount of the subscribed capital with currency. Currency code used of the capital subscribed, as defined in ISO 4217:2015. | [shareCapital](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#shareCapital) | O | No | [O018](#requirement-O018) |
| legalPersonDuration | Endpoint of the legal duration of the company, if it is of a limited timespan. Given as date following ISO 8601. | [legalPersonDuration](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#legalPersonDuration) | O | No | [O019](#requirement-O019) |
| digitalContactPoint | Correspondence address of the company, such as electronic mail and/or website. | [digitalContactPoint](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#digitalContactPoint) | O | No | [O020](#requirement-O020) |
| fullName | Full name of the natural person representing the company. | [fullName](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#fullName) | C | No | [O021](#requirement-O021) |
| dateOfBirth | Date of birth of the natural person representing the company. | [dateOfBirth](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#dateOfBirth) | C | No | [O022](#requirement-O022) |
| nationality | OPTIONAL: Nationality of the natural person representing the company. | [nationality](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#nationality) | C | No | [O023](#requirement-O023) |
| signatoryRule | Information on whether the representative can engage the company alone or jointly. | [signatoryRule](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#signatoryRule) | C | No | [O024](#requirement-O024) |
| name | Details about the legal person representing the company. | [name](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#name) | C | No | [O025](#requirement-O025) |
| id | Unique ID for the legal person in the EUID structure. | [id](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#id) | C | No | [O026](#requirement-O026) |
| legalFormType | Legal form of the legal person representing the company. | [legalFormType](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#legalFormType) | C | No | [O027](#requirement-O027) |
| signatoryRule | Information on whether the representative can engage the company alone or jointly. | [signatoryRule](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#signatoryRule) | C | No | [O028](#requirement-O028) |
| fullAddress | Complete address of the company, written as a string, separated by semicolons. | [fullAddress](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#fullAddress) | M | No | [O029](#requirement-O029) |
| careOf | Used when the address is at the address of another person or legal person. | [careOf](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#careOf) | O | No | [O030](#requirement-O030) |
| thoroughFare | The name of a passage or way through from one location to another. | [thoroughFare](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#thoroughFare) | O | No | [O031](#requirement-O031) |
| locatorDesignator | A number or sequence that uniquely identifies the locator. | [locatorDesignator](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#locatorDesignator) | O | No | [O032](#requirement-O032) |
| postCode | The code created and maintained for postal purposes. | [postCode](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#postCode) | O | No | [O033](#requirement-O033) |
| postName | A name identifying a subdivision of addresses (e.g., city). | [postName](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#postName) | O | No | [O034](#requirement-O034) |
| postOfficeBox | A location designator for a postal delivery point at a post office. | [postOfficeBox](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#postOfficeBox) | O | No | [O035](#requirement-O035) |
| locatorName | Proper noun(s) applied to the real-world entity. | [locatorName](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#locatorName) | O | No | [O036](#requirement-O036) |
| adminUnitLevel1 | The uppermost administrative unit (typically country). | [adminUnitLevel1](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#adminUnitLevel1) | O | No | [O037](#requirement-O037) |
| adminUnitLevel2 | Secondary level/region (typically county or state). | [adminUnitLevel2](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#adminUnitLevel2) | O | No | [O038](#requirement-O038) |



| Relation | Description | vocabulary | Left Entity | Right Entity | Cardinality | required by |
|--|--|--|--|--|--|--|
| registeredAddress | the address at which the legal entity is legally registered | [registeredAddress](https://ebw-vocabulary.spherity.dev/ebw/v0.1/vocabulary#registeredAddress) | Company  | Address | 1..1 | [O013](#requirement-O013) |


> Questions to ask per relation:
> Check whether the direction (Hello ? World) reflects the dominant
> flow of meaning.
> If both sides can have multiple relations (n?n), consider
> refactoring the relationship into a separate class (e.g.,
> GreetingEvent)

# Workflow of the Attestation

Purpose: Map the flow of actions, data, and interactions between entities.

| Actor | Role | Description |
|--|--|--|
|  |  |  |

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

From the [publication](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_2025000250)

| No. | Requirement | Source | Verification method |
|--|--|--|--|
| <a id="requirement-L001"></a>L001 | Member States shall ensure that the registers issue the EU Company Certificates regarding the companies listed in Annexes II and IIB. The EU Company Certificate shall be accepted in all Member States as sufficient evidence, at the time of its issuance, of the incorporation of the company and of the information listed in paragraphs 2 and 3 of this Article, respectively, which is held by the register in which the company is registered. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
|  | **Remark:** *The annexes II and IIb do not seem to be complete or may be unclear. For NL it is missing legal forms. Therefor the requirements will apply to all registered organisations, unless explicitly mentioned otherwise.* |  |  |
| <a id="requirement-L002"></a>L002 | the EU Company Certificate for the limited liability companies listed in Annex II shall include the following information: | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L003"></a>L003 | for limited liability companies: the **name or names of the company** | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L004"></a>L004 | for limited liability companies: the **legal form** of the company | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L005"></a>L005 | for limited liability companies: the **registration number** of the company **and the Member State where the company is registered** | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L006"></a>L006 | for limited liability companies: the **EUID** of the company | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L007"></a>L007 | for limited liability companies: the **registered office** of the company | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
|  | **Remark:** *The registered office is the address recorded in the commercial register that determines...* |  |  |
| <a id="requirement-L008"></a>L008 | for limited liability companies: the **correspondence address** of the company, such as its electronic mail or postal address | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L009"></a>L009 | for limited liability companies: the **date of registration** of the company | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L010"></a>L010 | for limited liability companies: the **amount of the subscribed capital** of the company, if applicable. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L011"></a>L011 | for limited liability companies: the **status** of the company... | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L012"></a>L012 | for limited liability companies: first names, surnames and date of birth of **any persons authorised to represent it** | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L013"></a>L013 | for limited liability companies: where the persons referred to are legal persons, the name, legal form, EUID or registration number. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
|  | **Remark:** *(we should talk about this...)* |  |  |
| <a id="requirement-L014"></a>L014 | for limited liability companies: the **object of the company** (NACE code where used). | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
|  | **Remark:** *because some countries don't use the NACE code...* |  |  |
| <a id="requirement-L015"></a>L015 | for limited liability companies: the **duration** of the company. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L016"></a>L016 | for limited liability companies: details of the company’s **website**. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L017"></a>L017 | for limited liability companies: the **date of issue** of the EU Company Certificate. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L018"></a>L018 | The EU Company Certificate for partnerships listed in Annex IIB shall include the information referred to... | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L019"></a>L019 | for partnerships: the **registered office** of the partnership. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L020"></a>L020 | for partnerships: **maximum liability or contribution of each limited partner**. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L021"></a>L021 | for partnerships: details of **partners/directors authorised to represent** the partnership. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L022"></a>L022 | for partnerships: where persons are legal persons, include name, legal form, EUID or registration number. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L023"></a>L023 | for partnerships: details of general and limited partners. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L024"></a>L024 | for partnerships: where persons referred to are legal persons, include name, legal form, EUID or registration number. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L025"></a>L025 | Member States shall ensure that the EU Company Certificate can be obtained from the register electronically or by paper means. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L026"></a>L026 | Member States shall ensure that each company can obtain its EU Company Certificate in electronic format free of charge (at least once per year). | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L027"></a>L027 | Electronic EU Company Certificate must be authenticated using trust services and compatible with the European Digital Identity Wallet. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L028"></a>L028 | Paper EU Company Certificate must include date of issuance, seal/stamp and unique protocol or identification number. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| <a id="requirement-L029"></a>L029 | The Commission shall publish the multilingual template for the EU Company Certificate on the European e-Justice portal. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |


|  | **Remark:**  |  |  |

Why are some attributes only applicable for limited liability 

## Information requirements




| No. | Requirement | mandatory/optional |Source | Verification method |
|--|--|--|--|--|
| <a id="requirement-I001"></a>I001 | Entity for the register in which the organisation is registered | M | [L001](#requirement-L001) | check |
| <a id="requirement-I002"></a>I002 | Entity for the organisation | M | [L001](#requirement-L001) | check |
| <a id="requirement-I003"></a>I003 | Entity for the organisation's legal type | M | [L001](#requirement-L001) | check |
| <a id="requirement-I004"></a>I004 | Details of the company’s **website** | M | [L015](#requirement-L015) | check |
| <a id="requirement-I005"></a>I005 | The **LPID name** | M | [L001](#requirement-L001) | check |
| <a id="requirement-I006"></a>I006 | The **LPID ID**, or EUID | M | [L001](#requirement-L001) | check |
| <a id="requirement-I007"></a>I007 | the **legal form** of the company | M | [L003](#requirement-L003) | check |
| <a id="requirement-I008"></a>I008 | the **Member State where the company is registered** | M | [L004](#requirement-L004) | check |
| <a id="requirement-I009"></a>I009 | the object of the company, **NACE code** or member state code | M | [L013](#requirement-L013) | check |
| <a id="requirement-I010"></a>I010 | for limited liability companies: the **duration** of the company | M | [L014](#requirement-L014) | check |
| <a id="requirement-I011"></a>I011 | The Commission shall publish the multilingual template for the EU Company Certificate on the European e-Justice portal (“the portal”) in all official languages of the Union. | M | [L028](#requirement-L028) | check |

Check for a list of standard legal forma in the EU.

## Functional requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|
|  |  |  |  |

## Technical requirements – e.g. security, privacy, performance, usability.
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| <a id="requirement-T001"></a>T001 | paper issuance | [L025](#requirement-L025) |  |
| <a id="requirement-T002"></a>T002 | The EUCC SHALL follow the SD-JWT format. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#32-sd-jwt-vc-based-encoding) | check |
| <a id="requirement-T003"></a>T003 | The EUCC SHALL be in a format that can scale to additional/new legal forms. |  |  |
| T004 |  |  |  |
|  |  |  |  |

## Rulebook or Operational requirements
| No. | Requirement | Source | MOC | Verification method |
|--|--|--|--|--|
| <a id="requirement-O001"></a>O001 | Each company listed in Annex II or Annex IIB can obtain its EU Company Certificate in electronic format free of charge unless it causes serious prejudice to the financing of the national registers. | [L025](#requirement-L025), [L026](#requirement-L026) | O | ? |
| <a id="requirement-O002"></a>O002 | The Commission shall publish the multilingual template for the EU Company Certificate on the European e-Justice portal (“the portal”) in all official languages of the Union. (see countries below). | [L028](#requirement-L028) | M | ? |
| <a id="requirement-O003"></a>O003 | **Natural person:** an individual human being who has legal rights and obligations. Unlike a legal person (which refers to an organization or entity), a natural person is a human with the capacity to engage in legal relationships, enter into contracts, own property, and be subject to legal actions. Natural persons are distinct from artificial entities (like corporations or governments). In legal terms, a natural person is someone who exists as a human being, as opposed to a corporate or fictional entity. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#14-terminology) | M | check |
| <a id="requirement-O004"></a>O004 | **Legal person:** an entity that has legal rights and obligations, similar to a natural person (an individual). It is an organization or group recognized by law as having the capacity to enter into contracts, sue, and be sued, and own property. Legal persons are distinct from the individuals who may own, manage, or be part of them. Examples of legal persons include Corporations, Government agencies, public entities (that are granted legal recognition to act on behalf of the state), Nonprofit organizations A legal person exists as a separate legal entity, meaning it can perform legal actions in its own name, distinct from the actions of its members. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#14-terminology) | M | check |
| <a id="requirement-O005"></a>O005 | **Legal entity:** an organization or structure that is recognized by law as having legal rights and responsibilities distinct from those of its members or owners. A legal entity can enter into contracts, own property, incur debts, and be held liable for legal actions in its own name. Legal entities include various forms of organizations such as Corporations, Limited liability companies (LLCs), Nonprofit organizations, Partnerships The key characteristic of a legal entity is that it has its own legal existence, allowing it to perform actions independently of the individuals who are involved with it. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#14-terminology) | M | check |
| <a id="requirement-O006"></a>O006 | **Legal representative:** Natural or legal person authorized to act on behalf of another person or organization in legal matters. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#14-terminology) | M | check |
| <a id="requirement-O007"></a>O007 | **Signatory rights:** the authority or power granted to an individual or entity to legally bind an organization or company by signing contracts, agreements, or other formal documents. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#14-terminology) | M | check |
| <a id="requirement-O008"></a>O008 | **attestation_legal_category** One of EAA, Pub-EAA or QEAA | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#22-mandatory-attributes) | M | check |
| <a id="requirement-O009"></a>O009 | **legal_person_name** Official current legal person name as registered in the business register. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#22-mandatory-attributes) | M | check |
| <a id="requirement-O010"></a>O010 | **legal_person_id** Unique ID for the legal person in the EUID structure. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#22-mandatory-attributes) | M | check |
| <a id="requirement-O011"></a>O011 | **legal_form_type** Legal form of the company. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#22-mandatory-attributes) | M | check |
| <a id="requirement-O012"></a>O012 | **registration_member_state** The member state where the company is registered (Alpha-2 country code). | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#22-mandatory-attributes) | M | check |
| <a id="requirement-O013"></a>O013 | **registered_address** The official address of the company as registered by public authority. See [section 2.5](#25-Address). | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#22-mandatory-attributes) | M | check |
| <a id="requirement-O014"></a>O014 | **registration_date** Date of company registration. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#22-mandatory-attributes) | M | check |
| <a id="requirement-O015"></a>O015 | **legal_person_status** Status of the company as defined in national law. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#22-mandatory-attributes) | M | check |
| <a id="requirement-O016"></a>O016 | **legal_person_activity** Main activity of the company (NACE). | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#22-mandatory-attributes) | M | check |
| <a id="requirement-O017"></a>O017 | **legal_representative** Information about the natural or legal person(s) authorized to represent the company. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#22-mandatory-attributes) | M | check |
| <a id="requirement-O018"></a>O018 | **share_capital** Amount of the subscribed capital with currency. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#23-optional-attributes) | O | check |
| <a id="requirement-O019"></a>O019 | **legal_person_duration** Endpoint of the legal duration of the company. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#23-optional-attributes) | O | check |
| <a id="requirement-O020"></a>O020 | **digital_contact_point** Correspondence address of the company. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#23-optional-attributes) | O | check |
| <a id="requirement-O021"></a>O021 | **full_name** Full name of the natural person representing the company. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#24-conditional-attributes) | C | check |
| <a id="requirement-O022"></a>O022 | **date_of_birth** Date of birth of the natural person representing the company. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#24-conditional-attributes) | C | check |
| <a id="requirement-O023"></a>O023 | **nationality** Nationality of the natural person representing the company. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#24-conditional-attributes) | C | check |
| <a id="requirement-O024"></a>O024 | **signatory_rule** Information on whether the representative can engage the company alone or jointly. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#24-conditional-attributes) | C | check |
| <a id="requirement-O025"></a>O025 | **name** Details about the legal person representing the company. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#24-conditional-attributes) | C | check |
| <a id="requirement-O026"></a>O026 | **id** Unique ID for the legal person in the EUID structure. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#24-conditional-attributes) | C | check |
| <a id="requirement-O027"></a>O027 | **legal_form_type** Legal form of the legal person representing the company. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#24-conditional-attributes) | C | check |
| <a id="requirement-O028"></a>O028 | **signatory_rule** Information on whether the representative can engage the company alone or jointly. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#24-conditional-attributes) | C | check |
| <a id="requirement-O029"></a>O029 | **full_address** Complete address of the company. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#25-address) | M | check |
| <a id="requirement-O030"></a>O030 | **care_of** Used when the address is at the address of another person. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#25-address) | O | check |
| <a id="requirement-O031"></a>O031 | **thorough_fare** The name of a passage or way. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#25-address) | O | check |
| <a id="requirement-O032"></a>O032 | **locator_designator** A number identifying the locator. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#25-address) | O | check |
| <a id="requirement-O033"></a>O033 | **post_code** Postal code. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#25-address) | O | check |
| <a id="requirement-O034"></a>O034 | **post_name** City or subdivision name. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#25-address) | O | check |
| <a id="requirement-O035"></a>O035 | **post_office_box** PO box identifier. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#25-address) | O | check |
| <a id="requirement-O036"></a>O036 | **locator_name** Proper noun(s) applied to the entity. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#25-address) | O | check |
| <a id="requirement-O037"></a>O037 | **admin_unit_level_1** Country-level administrative unit. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#25-address) | O | check |
| <a id="requirement-O038"></a>O038 | **admin_unit_level_2** Secondary administrative unit. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#25-address) | O | check |
| <a id="requirement-O039"></a>O039 | The EUCC is intended to be used as a standardised, machine-verifiable proof of a company’s incorporation and registered company information. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#4-attestation-usage) | check |
| <a id="requirement-O040"></a>O040 | **Cross-border business onboarding (B2B)** description. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#4-attestation-usage) | check |
| <a id="requirement-O041"></a>O041 | **Public administration procedures (G2B)** description. |  | check |
| <a id="requirement-O042"></a>O042 | **Financial and regulated services** description. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#4-attestation-usage) | check |
| <a id="requirement-O043"></a>O043 | **Replacement/supplement of national extracts** description. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#4-attestation-usage) | check |
| <a id="requirement-O044"></a>O044 | The EUCC is intended for **online, remote presentation** using EUDI Wallet-compatible protocols. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#4-attestation-usage) | check |
| <a id="requirement-O045"></a>O045 | Only Business Registries are allowed to be the authentic source of the EUCC attestation. | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#41-issuance-of-the-eucc) | check |
| <a id="requirement-O046"></a>O046 | The EUCC SHALL be issued in a format compatible with the EUDI Wallet ecosystem (e.g., **OpenID4VP** profiles). | [Rulebook](https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog/blob/main/rulebooks/ds004-eucc-rulebook.md#41-issuance-of-the-eucc) | check |

## Governance and trust restrictions
| No. | Requirement | Source | Verification method |
|--|--|--|--|
|  | |  |  |

## Open Questions / Gaps – For follow-up or design iterations.
| No. | Question | Why |
|--|--|--|
|  |  |  |
