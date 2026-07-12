# 03 - Identity and Access Review

## Purpose

This section reviews sample user accounts and access levels in the fictional lab environment.

The goal is to check whether each account has a clear purpose and whether the access level looks reasonable.

## Sample Accounts

| Account | Role | Access Level | Note |
|---|---|---|---|
| `student01` | Student user | Standard | Looks normal |
| `student02` | Student user | Standard | Looks normal |
| `labadmin` | Lab admin | Admin | Expected admin account |
| `testadmin` | Test account | Admin | Purpose is unclear |
| `guest01` | Guest user | Standard | Should be reviewed |

## Findings

| Finding | Risk | Suggested Action |
|---|---|---|
| `testadmin` has admin access, but its purpose is unclear | Unnecessary privileged access | Review the account and remove admin access if not needed |
| `guest01` may no longer be needed | Unused account risk | Disable or remove the account if it is not required |

## Notes

The main focus in this section is least privilege.

Accounts should have only the access they need. Admin accounts should be limited and easy to explain.

## Learning Connection

This section helped me practice basic identity review, access control, account ownership, and least privilege thinking.
