# 05 - Log Analysis

## Purpose

This section reviews sample authentication logs from the fictional learning environment.

## What I Looked For

- failed login attempts
- successful login events
- repeated failures from the same user
- login attempts against test or admin accounts
- basic signs of suspicious authentication behavior

## Example Log Review

| Log Pattern | Meaning | Risk Level | Note |
|---|---|---|---|
| Multiple failed logins for testadmin | Possible guessing attempt | Medium | Review whether the account is needed |
| Successful student login | Normal activity | Low | No action needed |
| Failed guest login | Guest account may be targeted | Medium | Disable guest account if unused |

## Student Note

This section focuses on reading and interpreting simple authentication logs.

The goal is not to build an advanced SOC or SIEM workflow. It is a basic log review exercise using fictional sample data.

## Outcome

Authentication logs can reveal account misuse, weak account hygiene, or suspicious login behavior.
