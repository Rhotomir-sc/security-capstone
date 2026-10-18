# Scenario and evidence boundaries

This is a fictional teaching environment. Roles and proposed controls describe the scenario, not a production system.

```text
router-firewall 192.168.10.1
        |
        +-- lab-server    192.168.10.10  (SSH 22, HTTP 80)
        +-- instructor-pc 192.168.10.20  (intended management source)
        +-- student-pc    192.168.10.30  (learning-content access)
```

| Material | Meaning |
|---|---|
| [Authentication log](sample-logs/auth_sample.log) | Fictional input that can be analyzed |
| [Identity review](01-identity-review.md) | Scenario roles and a proposed permission correction |
| [Firewall review](05-firewall-review.md) | Scenario rules and recommended restriction |
| [Reproduction guide](REPRODUCE.md) | Executable analysis and expected findings |
| [Verification plan](remediation-verification.md) | Proposed changes; live verification pending |

A screenshot of a report documents that report; it does not independently prove deployment. No new system changes or live connection tests are claimed by this maintenance update.
