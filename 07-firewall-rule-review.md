# 07 - Firewall Rule Review

## Purpose

This section reviews basic firewall rule risks in the fictional learning environment.

## Review Questions

- Is the rule too broad?
- Does the rule allow unnecessary access?
- Is the source limited?
- Is the destination clear?
- Is the port or service necessary?
- Is there a clear reason for the rule?

## Example Rule Review

| Rule | Observation | Risk Level | Recommendation |
|---|---|---|---|
| Allow any to SSH | Too broad | High | Restrict source IPs |
| Allow internal web access | Expected rule | Low | Keep monitored |
| Old test rule | No clear purpose | Medium | Remove if unused |

## Student Note

The goal is to understand basic firewall rule hygiene.

This is not an enterprise firewall policy design. It is a simple student-level review of fictional firewall examples.

## Outcome

Firewall rules should be limited, documented, and reviewed regularly.
