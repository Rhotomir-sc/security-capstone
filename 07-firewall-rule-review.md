# 07 - Firewall Rule Review

## Purpose

This section reviews simple firewall rule examples in the fictional lab environment.

The goal is to check whether some access rules are too broad or unnecessary.

## Sample Firewall Rules

| Rule | Source | Destination | Port | Action | Note |
|---|---|---|---|---|---|
| FW-01 | Student network | Lab server | 80 | Allow | Looks acceptable |
| FW-02 | Student network | Lab server | 22 | Allow | Too broad |
| FW-03 | Admin workstation | Lab server | 22 | Allow | More appropriate |
| FW-04 | Guest user | Lab server | Any | Allow | Risky |

## Findings

| Finding | Risk | Suggested Action |
|---|---|---|
| SSH access is allowed from the full student network | Too many users may reach an admin service | Allow SSH only from the admin workstation |
| Guest user has broad access to the lab server | Guest access may expose internal resources | Deny or strongly restrict guest access |

## Notes

Firewall rules should be simple, clear, and limited to what is needed.

A rule should answer:

- who needs access
- which service is needed
- whether the access is too broad

## Learning Connection

This section helped me practice firewall rule review, least privilege, and basic network access control.
