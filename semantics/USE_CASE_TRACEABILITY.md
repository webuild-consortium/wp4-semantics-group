# Use-case traceability register

This register records why classes and properties in the jointly developed model are needed and which WEBUILD use cases they support. Maintain these links in repository documentation, outside the ontology. The register follows the [Protégé and GitHub working guide](PROTEGE_GITHUB.md).

## Use cases and source requirements

Use the project's existing use-case identifiers and names. Link to the authoritative requirement or source passage where available. Do not invent project identifiers or treat an implementation choice as an agreed requirement.

| Use-case ID | Use-case name | Requirement ID or source passage | Source link |
| --- | --- | --- | --- |

No use cases have been entered yet.

## Class and property mappings

Record one row per term and use-case requirement. Use the full term IRI so that labels and local names do not cause ambiguity. If a term supports several use cases, record each relevant link. Explain the modelling need and distinguish proposed mappings from mappings agreed by both modellers.

| Term IRI | Kind (class or property) | Use-case ID | Requirement ID or source passage | Reason the term is needed | Review status |
| --- | --- | --- | --- | --- | --- |

No domain-term mappings have been entered yet. The draft ontology currently contains only its ontology declaration and supporting annotation properties.

For supporting annotation properties, record their documentation role when relevant; do not invent a domain use-case requirement for them. A term with an unresolved source or use-case link remains an explicit gap until the modellers resolve it.

## Maintenance and review

Update this register in the same branch and pull request as the relevant model change. When a term IRI changes, update its register entries. Removing or replacing a term requires review of the use-case requirements linked to it.

Review coverage in both directions: every modelled domain class or property needs a documented rationale, and every registered requirement needs an agreed mapping or an explicit modelling gap. A mapping records intended support; it does not by itself prove that an application profile or implementation meets the requirement.

The existing automated ontology checks do not validate this register. Include its links, mapping accuracy, outstanding gaps, and coverage in the human review before synchronising with GitHub. The separate register introduces no use-case annotations or relations into `model/webuild.ttl`.
