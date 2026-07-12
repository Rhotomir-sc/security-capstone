# 09 - Risk Register

## Purpose

This section lists the main findings from the fictional lab review.

The goal is to organize each finding with a simple risk level and suggested action.

## Risk Register

| ID | Finding | Risk Level | Suggested Action | Status |
|---|---|---|---|---|
| R-01 | Unclear admin account | Medium | Review the account owner and remove admin access if not needed | Open |
| R-02 | Guest account may be unused | Low | Disable or remove the account if it is not required | Open |
| R-03 | Repeated failed login attempts | Medium | Review the login activity and confirm if it is expected | Open |
| R-04 | SSH access is too broad | Medium | Limit SSH access to the admin workstation | Open |
| R-05 | Guest access to lab server is too open | High | Deny or strongly restrict guest access | Open |
| R-06 | Phishing email asks for credentials | High | Report the email and block or review the sender | Open |

## Risk Level Notes

| Level | Meaning |
|---|---|
| Low | Should be reviewed |
| Medium | Should be fixed |
| High | Should be prioritized |

## Short Note

This risk register helped me collect the main findings in one place.

It also made the review easier to understand because each issue has a risk level and a suggested action.

## Learning Connection

This section helped me practice basic risk documentation, prioritization, and clear security reporting.
