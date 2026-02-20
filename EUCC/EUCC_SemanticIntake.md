# Use Case Overview of EU Organisation Certificate (former EUCC)

Purpose: Capture the story and high-level purpose of the use case “issuing and using the EUCC”.

This iteration is based on:
 - [Publication amending existing EU company-law directives (Directives 2009/102/EC and 2017/1132) to expand and improve the use of digital tools and digital processes in company law](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32025L0025&qid=1762615804836). In article 16b it describes the EU Company Certificate. Suggested to rename to EU Organisation Certificate, EUOC.
 - The [EU Company Certificate Data Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/0434604ad07d42e946bc062ea72f86b1cafecc19/rulebooks/rb002_eu_company_certificate.md)

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

**Entity: EUCC**
| Name | Description/Definition |
|--|--|
|  |  |

| Attribute | Description | mandatory | private | datatype | 
|--|--|--|--|--|
|  |  |  |  |  |
|  |  |  |  |  |

| Relation | Description | Left Entity | Right Entity | Left Role | Right Role | Cardinality | Optional |
|--|--|--|--|--|--|--|--|
|  |  |  |  |  |  |  |  |

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
| L001 | Member States shall ensure that the registers issue the EU Company Certificates regarding the companies listed in Annexes II and IIB. The EU Company Certificate shall be accepted in all Member States as sufficient evidence, at the time of its issuance, of the incorporation of the company and of the information listed in paragraphs 2 and 3 of this Article, respectively, which is held by the register in which the company is registered. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
|  | **Remark:** *The annexes II and IIb do not seem to be complete or may be unclear. For NL it is missing legal forms. Therefor the requirements will apply to all registered organisations, unless explicitly mentioned otherwise.* |  |  |
| L002 | the EU Company Certificate for the limited liability companies listed in Annex II shall include the following information: | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L003 | for limited liability companies: the **name or names of the company**  | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L004 | for limited liability companies: the **legal form** of the company | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L005 | for limited liability companies: the **registration number** of the company **and the Member State where the company is registered** | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L006 | for limited liability companies: the **EUID** of the company | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L007 | for limited liability companies: the **registered office** of the company | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
|  | **Remark:** *The registered office is the address recorded in the commercial register that determines: under which Member State’s company law the company is incorporated; where official communications and legal documents must be served; and, in most cases, where the company is considered to have its  legal domicile (even if it operates elsewhere). It’s the company’s  formal legal seat, not necessarily its operational headquarters or main place of business.* |  |  |
| L008 | for limited liability companies: the **correspondence address** of the company, such as its electronic mail or postal address  | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L009 | for limited liability companies: the **date of registration** of the company  | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L010 | for limited liability companies: the **amount of the subscribed capital** of the company, if applicable. (an amount and currency) | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L011 | for limited liability companies: the **status** of the company, such as when it is closed, struck off the register, wound up, dissolved, undergoing insolvency proceedings, economically active or inactive as defined in national law and where it is recorded in the national register; (ENUM: active, inactive, ...) | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L012 | for limited liability companies: the first names, surnames and date of birth, or equivalent information when that date is not recorded in the national register, of **any persons who** either as a body or as members of any such body **are authorised by the company to represent it** in dealings with third parties and in legal proceedings, and whether those persons may do so alone or are required to act jointly.  | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L013 | for limited liability companies: where the persons referred to in point (j) are legal persons, the name, the legal form, the EUID or, where the EUID is not applicable, the registration number. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
|  | **Remark:** *(we should talk about this. How deep do we follow the PoA chain? We don't! In the text it clearly states are authorised by the company, that is directly, so it means the shareholders. Also we should have a harmonised list of titles of each country.)* |  |  |
| L014 | for limited liability companies: the **object of the company**, describing its main activity or activities, which can be expressed using the relevant Statistical Classification of Economic Activities in the European Community (NACE) code, where such code is used for the purposes of the register pursuant to applicable national law, and where the object is recorded in the national register. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
|  | **Remark:** *because some countries don't use the NACE code, one should be able to enter another code or string. NACE (SBI in NL, different codes in BE, WZ in DE)* |  |  |
| L015 | for limited liability companies: the **duration** of the company, where its duration is limited. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L016 | for limited liability companies: details of the company’s **website** where such details are recorded in the national register. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L017 | for limited liability companies: the **date of issue of the** company’s **EU Company Certificate**. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L018 | The EU Company Certificate for partnerships listed in Annex IIB shall include the information referred to in paragraph 2 of this Article, with the exception of points (e), (h) (j) and (k). The following information shall also be included: | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L019 | for partnerships: the **registered office, or equivalent**, of the partnership. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L020 | for partnerships: the amount of **maximum liability or of the contribution of each limited partner**, where that information is recorded in the national register. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L021 | for partnerships: the first names, surnames and date of birth, or equivalent information when that date is not recorded in the national register, of **the partners, directors or other statutory representatives, who are authorised to represent the partnership** in dealings with third parties and in legal proceedings, or, if not applicable, information about the nature and scope of the authorisation of the partners, directors or other representatives to represent the partnership and their particulars. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L022 | for partnerships: where the persons referred to in point (c) (this is L018) are legal persons, the name, the legal form, the EUID or, where the EUID is not applicable, the registration number. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L023 | for partnerships: where different from points (c) (this is L018 and (d) (this is L019), the first names, surnames and date of birth, or equivalent information when that date is not recorded in the national register, of the general partners, and, in the case of limited partnerships, particulars of the limited partners, where particulars of the latter are made publicly available in the national register. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L024 | for partnerships: where the persons referred to in point (e) are legal persons, the name, the legal form, the EUID or, where the EUID is not applicable, the registration number. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L025 | Member States shall ensure that the EU Company Certificate can be obtained from the register upon an application submitted to the register by electronic or by paper means.<br>Member States shall ensure that the electronic version of the EU Company Certificate can also be obtained through the system of interconnection of registers. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L026 | Member States shall ensure that each company listed in Annex II or Annex IIB can obtain its EU Company Certificate in electronic format free of charge unless it causes serious prejudice to the financing of the national registers. In any case, each company shall be able to obtain its EU Company Certificate free of charge at least once per calendar year.<br>Where a price is charged for obtaining the EU Company Certificate, whether by electronic or by paper means, it shall not exceed the administrative costs thereof, including the costs of development and maintenance of registers. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L027 | Member States shall ensure that the EU Company Certificate provided by the register in electronic form is authenticated by means of trust services as referred to in Regulation (EU) No 910/2014 in order to guarantee that it has been provided by the register and that its content is a true copy of the information held by the register or that it is consistent with the information contained therein. The EU Company Certificate shall also be compatible with the European Digital Identity Wallet, as provided for in Regulation (EU) 2024/1183. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L028 | Member States shall ensure that the EU Company Certificate provided by the register in paper form includes the date of issuance, as well as the seal or stamp of the register, or equivalent means of authentication, in order to certify that its content is a true copy of the information held by the register or that it is consistent with the information contained therein, and bears a unique protocol or identification number or similar feature that allows the electronic verification of the origin and authenticity of the document. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |
| L029 | The Commission shall publish the multilingual template for the EU Company Certificate on the European e-Justice portal (“the portal”) in all official languages of the Union. | [Article 16b](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025L0025) | review |


|  | **Remark:**  |  |  |

Why are some attributes only applicable for limited liability 

## Information requirements




| No. | Requirement | mandatory/optional |Source | Verification method |
|--|--|--|--|--|
| I001 | Entity for the register in which the organisation is registered | M | L001 | check |
| I002 | Entity for the organisation | M | L001 | check |
| I003 | Entity for the organisation's legal type | M | L001 | check |
| I004 | Details of the company’s **website** | M | L015 | check |
| I005 | The **LPID name** | M | L001 | check |
| I006 | The **LPID ID**, or EUID | M | L001 | check |
| I007 | the **legal form** of the company | M | L003 | check |
| I008 | the **Member State where the company is registered** | M | L004| check |
| I009 | the object of the company, **NACE code** or member state code | M | L013 | check |
| I010 | for limited liability companies: the **duration** of the company | M | L014 | check |
| I011 | The Commission shall publish the multilingual template for the EU Company Certificate on the European e-Justice portal (“the portal”) in all official languages of the Union. | M | L028 | check |
| I012 | EUCC attribute: **legal_person** Information regarding the legal entity, including name, ID, legal form, etc. | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#4-eucc-attributes) | check |
| I013 | EUCC attribute: **legal_person_name** Official current legal entity name as registered in the business register. | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#4-eucc-attributes) | check |
| I014 | EUCC attribute: **legal_person_id** Unique ID for the legal entity in the EUID structure. | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#4-eucc-attributes) | check |
| I015 | EUCC attribute: legal_form_type 	Legal form of the company. | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#4-eucc-attributes) | check |
| I016 | EUCC attribute: **registration_member_state** The member state where the company is registered (Alpha-2 country code according to ISO 3166-1). | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#4-eucc-attributes) | check |
| I017 | EUCC attribute: **registered_address** The official address of the company. | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#4-eucc-attributes) | check |
| I018 | EUCC attribute: **care_of** Used when the address is at the address of another person or legal entity. | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#4-eucc-attributes) | check |
| I019 | EUCC attribute: **full_address** Complete address of the company, written as a string, separated by semicolons. | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#4-eucc-attributes) | check |
| I020 | EUCC attribute: **registration_date** Date of company registration. | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) | check |
| I021 | EUCC attribute: **share_capital** Amount of the subscribed capital with currency. | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) | check |
| I022 | EUCC attribute: **legal_entity_status** Status of the company as defined in national law and recorded in the national register. | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) | check |
| I023 | EUCC attribute: **legal_entity_activity** Main activity or activities of the company, expressed using the NACE (Statistical Classification of Economic Activities). | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) | check |
| I024 | EUCC attribute: **legal_entity_duration** Duration of the company, if limited. | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) | check |
| I025 | EUCC attribute: **contact_point** Correspondence address of the company, such as email or postal address (full or partial). | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) | check |
| I026 | EUCC attribute: **contact_email** Details of the company email address. | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) | check |
| I027 | EUCC attribute: **contact_page** Details of the company website. | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) | check |
| I028 | EUCC attribute: **legal_representative** Information about the person(s) authorized to represent the company, either individually or jointly. | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) | check |
| I029 | EUCC attribute: **legal_representative.natural_person** Details about the natural person representing the company. | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) | check |
| I030 | EUCC attribute: **legal_representative.legal_person** Details about the legal person representing the company. | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md) | check |
| I031 | Registered address attribute: **full_address** | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#41-regitered-address-related-attributes) | check |
| I032 | Registered address attribute: **care_of** | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#41-regitered-address-related-attributes) | check |
| I033 | Registered address attribute: **thorough_fare** | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#41-regitered-address-related-attributes) | check |
| I034 | Registered address attribute: **locator_designator** | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#41-regitered-address-related-attributes) | check |
| I035 | Registered address attribute: **post_code** | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#41-regitered-address-related-attributes) | check |
| I036 | Registered address attribute: **post_name** | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#41-regitered-address-related-attributes) | check |
| I037 | Registered address attribute: **post_office_box** | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#41-regitered-address-related-attributes) | check |
| I038 | Registered address attribute: **locator_name** | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#41-regitered-address-related-attributes) | check |
| I039 | Registered address attribute: **admin_unit_level_1** | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#41-regitered-address-related-attributes) | check |
| I040 | Registered address attribute: **admin_unit_level_2** | O | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#41-regitered-address-related-attributes) | check |
| I041 | Legal representative attribute: **full_name** | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#42-legal-representative-related-attributes) | check |
| I042 | Legal representative attribute: **date_of_birth** | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#42-legal-representative-related-attributes) | check |
| I043 | Legal representative attribute: **nationality** | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#42-legal-representative-related-attributes) | check |
| I044 | Legal representative attribute: **signatory_rule** | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#42-legal-representative-related-attributes) | check |
| I045 | Legal person attribute: **legal_person_name** | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#42-legal-representative-related-attributes) | check |
| I046 | Legal person attribute: **legal_person_id** | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#42-legal-representative-related-attributes) | check |
| I047 | Legal person attribute: **legal_form_type** | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#42-legal-representative-related-attributes) | check |
| I048 | Legal person attribute: **signatory_rule** | M | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#42-legal-representative-related-attributes) | check |

Check for a list of standard legal forma in the EU.

## Functional requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|
|  |  |  |  |

## Technical requirements – e.g. security, privacy, performance, usability.
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| T001 | paper issuance | L025 |  |
| T002 | The EUCC SHALL follow the SD-JWT format. | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#51-trust-requirements-on-the-eucc-attestation-from-the-perspective-of-company-registration-offices-as-authentic-sources-for-the-eucc) |  |
| T001 | The EUCC unique identifier SHALL be unique and agreed upon on EU and EES level. | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#51-trust-requirements-on-the-eucc-attestation-from-the-perspective-of-company-registration-offices-as-authentic-sources-for-the-eucc) |  |
| T001 | The EUCC SHALL be in a format that can scale to additional/new legal forms. | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#51-trust-requirements-on-the-eucc-attestation-from-the-perspective-of-company-registration-offices-as-authentic-sources-for-the-eucc) |  |
| T001 | The EUCC SHALL apply for all legal persons. | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#51-trust-requirements-on-the-eucc-attestation-from-the-perspective-of-company-registration-offices-as-authentic-sources-for-the-eucc) |  |
| T001 | paper issuance | L025 |  |
| T001 | paper issuance | L025 |  |
|  |  |  |  |

## Rulebook or Operational requirements
| No. | Requirement | Source | Verification method |
|--|--|--|--|
| O001 | Each company listed in Annex II or Annex IIB can obtain its EU Company Certificate in electronic format free of charge unless it causes serious prejudice to the financing of the national registers. | L025, L026 | ? |
| O002 | The Commission shall publish the multilingual template for the EU Company Certificate on the European e-Justice portal (“the portal”) in all official languages of the Union. (see countries below). | L028 | ? |
| O003| **Natural person:** an individual human being who has legal rights and obligations. Unlike a legal person (which refers to an organization or entity), a natural person is a human with the capacity to engage in legal relationships, enter into contracts, own property, and be subject to legal actions. Natural persons are distinct from artificial entities (like corporations or governments). In legal terms, a natural person is someone who exists as a human being, as opposed to a corporate or fictional entity. | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#15-terminology) | check |
| O004| **Legal person:** an entity that has legal rights and obligations, similar to a natural person (an individual). It is an organization or group recognized by law as having the capacity to enter into contracts, sue, and be sued, and own property. Legal persons are distinct from the individuals who may own, manage, or be part of them. Examples of legal persons include Corporations, Government agencies, public entities (that are granted legal recognition to act on behalf of the state), Nonprofit organizations A legal person exists as a separate legal entity, meaning it can perform legal actions in its own name, distinct from the actions of its members. | [[Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#15-terminology) | check |
| O005| **Legal entity:** an organization or structure that is recognized by law as having legal rights and responsibilities distinct from those of its members or owners. A legal entity can enter into contracts, own property, incur debts, and be held liable for legal actions in its own name. Legal entities include various forms of organizations such as Corporations, Limited liability companies (LLCs), Nonprofit organizations, Partnerships The key characteristic of a legal entity is that it has its own legal existence, allowing it to perform actions independently of the individuals who are involved with it. | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#15-terminology) | check |
| O006| **Legal representative:** Natural or legal person authorized to act on behalf of another person or organization in legal matters. This person has the legal authority to represent the interests of the entity, such as a company, in dealings with other parties, including signing contracts, making decisions, and appearing in legal proceedings. For businesses, a legal representative can be a director, officer, or another person designated by the company’s governing body (like the board of directors) to represent the company in legal matters. In the case of individuals, a legal representative might include a guardian, power of attorney holder, or someone with similar legal authority to act on behalf of the person. | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#15-terminology)| check |
| O007| **Signatory rights:** the authority or power granted to an individual or entity to legally bind an organization or company by signing contracts, agreements, or other formal documents. This authority can be granted to a specific person, such as an executive, director, or authorized representative, and can be either individual (where one person alone can sign) or joint (where multiple individuals are required to sign together). Signatory rights are important because they ensure that any commitments made by the organization are legally valid and enforceable. The terms and scope of signatory rights are usually outlined in the organization's internal governance documents, such as its bylaws, and can vary based on the level of responsibility and the nature of the agreements being signed. | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#2-eucc-issuance-process) | check |
| O008| Only Business Registries are allowed to be the authentic source of the EUCC attestation | [[Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#2-eucc-issuance-process) | check |
| O009| This attestation can only be issued to an EUDI valid organizational wallet. | [Rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb002_eu_company_certificate.md#2-eucc-issuance-process) | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |
| O010|  |  | check |


<img width="513" height="436" alt="image" src="https://github.com/user-attachments/assets/4d248f0d-54b2-4d8d-9b37-ee5b9694caee" />


Do we need to discuss the issuance on paper?

## Governance and trust restrictions
| No. | Requirement | Source | Verification method |
|--|--|--|--|
|  | |  |  |

## Open Questions / Gaps – For follow-up or design iterations.
| No. | Question | Why |
|--|--|--|
|  |  |  |
