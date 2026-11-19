# Quality exceptions for the jointly developed model

## Merge and publication rules

Changes to the central ontology or its application profiles must be approved by both modellers and free of logical conflicts before merging into `main`. Resolve inconsistencies and unsatisfiable named classes reported by HermiT before merging. See the [scope of the merge requirements](PROTEGE_GITHUB.md#quality-checks-before-every-github-synchronisation).

A version with a known conflict may be published only as a separate publication from outside `main`. Both modellers must explicitly approve the exception for the documented revision and the proposed warning before publication. Keep the original diagnostics and show the warning prominently with the affected version.

## Exception records

No quality exceptions are currently registered or approved.

Before separately publishing a version with a known conflict, add a record below using this template. Fill the applicable fields and link to the actual approvals. Distinguish a proposal from an approved exception.

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

The [ontology pull request template](../.github/PULL_REQUEST_TEMPLATE/ontology.md) prompts authors and reviewers to record the quality checks, any unresolved findings, and the approval evidence for a proposed separate publication.

The quality suite runs HermiT and reports inconsistencies and unsatisfiable named classes as failures. An approved record leaves that result in place and authorises the separate publication within the recorded scope. Automated enforcement of the merge requirements on GitHub remains to be configured.
