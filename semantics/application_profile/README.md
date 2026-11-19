# Application profiles for the jointly developed model

The agreed format for new application profiles is SHACL in separate Turtle (`.ttl`) files. The central OWL model remains in [`../model/webuild.ttl`](../model/webuild.ttl). Application profiles express use-case-specific requirements against data, such as mandatory values, permitted datatypes, and minimum or maximum counts.

## Files and term references

Create a directory for each profile under `semantics/application_profile`, with a `shapes.ttl` file and an English README explaining its use case, scope, and source requirements. These are file naming conventions; shape identifiers and their namespace still need to be agreed before creating the first profile.

Reference central classes and properties by their existing IRIs. A profile's requirements must reflect its use case. Requirements valid generally for the meaning of a central concept belong in the central model. Maintain term-to-use-case links in the separate [traceability register](../USE_CASE_TRACEABILITY.md).

Keep the SHACL shapes outside the central ontology and apply the relevant profile separately during data validation. The central OWL model is edited in Protégé; edit SHACL source files as Turtle, preserving their SHACL content. Do not save shapes through the central ontology's Protégé workflow without first verifying that the editor preserves them.

Existing profile diagrams and documentation are source material for review. This decision does not automatically convert or approve them as profiles of the new draft model.

## Validation and review

The local quality suite and GitHub workflow use pySHACL to check each example against its own profile's `shapes.ttl`. The current suite validates the supplied example graph without additional inference or an extra ontology graph. If a profile needs additional inference, agree and document the intended settings before changing the check. See the [conservative OWL reasoning policy](../PROTEGE_GITHUB.md#conservative-use-of-owl-reasoning).

For each new profile, put at least one conforming Turtle example in `examples/valid/` and at least one non-conforming Turtle example in `examples/invalid/`. Document what each example demonstrates in the profile README. Each example is evaluated independently. A non-conforming example counts as expected only when SHACL returns a validation report. A syntax error, invalid shapes graph, or validator error fails the suite.

Review the profile targets, property paths, datatypes, cardinalities, and use-case justification together. For invalid examples, check that the reported violations match the requirements the examples are intended to test. Folders containing only earlier diagrams or documentation are outside the automated validation scope.

[W3C Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/) · [pySHACL documentation](https://github.com/RDFLib/pySHACL)
