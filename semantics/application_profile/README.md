# Application profiles for the jointly developed model

The agreed format for new application profiles is SHACL in separate Turtle (`.ttl`) files. The central OWL model remains in [`../model/webuild.ttl`](../model/webuild.ttl). Application profiles express use-case-specific requirements against data, such as mandatory values, permitted datatypes, and minimum or maximum counts.

## Files and term references

Create a directory for each profile under `semantics/application_profile`, with a `shapes.ttl` file and an English README explaining its use case, scope, and source requirements. These are file naming conventions; shape identifiers and their namespace still need to be agreed before creating the first profile.

Reference central classes and properties by their existing IRIs. A profile's requirements must reflect its use case. Requirements valid generally for the meaning of a central concept belong in the central model. Maintain term-to-use-case links in the separate [traceability register](../USE_CASE_TRACEABILITY.md).

Keep the SHACL shapes outside the central ontology and apply the relevant profile separately during data validation. The central OWL model is edited in Protégé; edit SHACL source files as Turtle, preserving their SHACL content. Do not save shapes through the central ontology's Protégé workflow without first verifying that the editor preserves them.

Existing profile diagrams and documentation are source material for review. This decision does not automatically convert or approve them as profiles of the new draft model.

## Validation and review

For each profile, prepare example data that should pass and example data that should fail its requirements. Record the expected result and use these examples to check the profile when its requirements change. Review the targets, property paths, datatypes, cardinalities, and use-case justification together.

The SHACL validation engine, inference settings, and integration into the automated quality suite remain to be agreed and configured. The current ontology checker does not validate application-profile data. No new SHACL profile or example dataset has been authored yet because the draft model has no domain classes or properties.

Reference: [W3C Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/).
