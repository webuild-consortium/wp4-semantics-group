# Quality exceptions for the jointly developed model

## Default rule

Changes merged into `main` must be approved by both modellers and free of unresolved logical conflicts. An inconsistent ontology or an unintentionally unsatisfiable class blocks merging by default.

A justified exception is possible only when both modellers explicitly approve its scope and disclosure. Approval of the modelling change alone does not imply approval of a conflict. Do not conceal a diagnostic, disable a check for the entire model, or report a waived finding as an unqualified pass.

## Exception records

No quality exceptions are currently registered or approved.

Before merging or publishing a change with a known conflict, add a record below using this template. Fill every field; link to the actual approvals rather than pre-filling them. Distinguish a proposal from an approved exception.

```text
Exception ID:
Status (proposed / approved / resolved):
Affected model revision and intended publication or release:
Affected term IRIs, axioms, and use cases:
Check and exact reported finding (with report link):
Reason for retaining or publishing the conflict:
Consequences for users, reasoning, and validation:
Scope of the exception (specific findings covered):
Resolution plan and responsible person:
Review trigger or expiry:
Bart's explicit exception approval (link):
Modelling colleague's explicit exception approval (link):
Pull request:
Publication warning text and where it appears:
Resolution evidence (when resolved):
```

Keep resolved records for traceability. Changes to the affected axioms, a new conflict, or a publication outside the approved scope require renewed review. An exception covers only its listed findings; all other quality checks still apply.

## Publication disclosure

The pull request, release notes, and documentation accompanying the affected published model must prominently identify the exception, the affected revision, the known conflict, its consequences, and the resolution plan. Link to the full record. The disclosure must travel with the publication, rather than being accessible only through an old pull request. An affected release must be visibly marked as containing approved quality exceptions; approval must not be described as proof of consistency.

## Enforcement status

The [ontology pull request template](../.github/PULL_REQUEST_TEMPLATE/ontology.md) prompts authors and reviewers to record the normal checks or an explicit exception. This is a procedural safeguard.

The reasoner, logical-check implementation, exception-aware checks, and GitHub protection of `main` still need to be configured. The present automated suite checks structural/editorial rules; it does not yet enforce logical consistency or this exception process. No automated waiver has been enabled by creating this register. A later implementation must preserve the original findings, reject unapproved or out-of-scope exceptions, and distinguish an approved exception from a clean result.
