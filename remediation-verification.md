# Remediation and verification plan

Status: **planned lab extension — not yet executed**.

| Finding | Basis | Proposed change | Evidence to collect | Status |
|---|---|---|---|---|
| R-01 Guest access | [Identity review](01-identity-review.md) | Restrict resources and duration | Before/after permissions and allowed/denied access tests | Pending |
| R-02 Broad SSH | [Firewall review](05-firewall-review.md) | Permit management from instructor-pc only | SSH succeeds from .20 and fails from .30; HTTP still works | Pending |
| R-03 Authentication | [Log](sample-logs/auth_sample.log) | Verify activity and investigate unexpected sessions | Timeline, scenario owner verification, follow-up logs | Analysis reproducible; remediation pending |
| R-04 Phishing | [Phishing review](04-phishing-review.md) | Document reporting and independent verification | Simulated triage record with rationale | Pending |

Before lab firewall changes, retain console access and save the original configuration. Record exact commands, rule order, active firewall, timestamp, and rollback. Compare a failed connection with service availability and an allowed-source test.

## Verification record
- Finding ID and lab date:
- Original configuration and evidence:
- Exact change:
- Expected allowed and denied behavior:
- Actual results and evidence:
- Rollback:
- Remaining limitations:
- Status: pending / verified / failed

Add results only after performing the lab. Recommendations and verified remediation remain separate.
