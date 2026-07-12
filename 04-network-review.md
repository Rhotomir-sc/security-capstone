# 04 - Network Observation

## Purpose

This section documents basic network observations in the fictional lab environment.

The goal is not to perform an advanced network assessment. The goal is to understand which systems exist and which access points may need review.

## Sample Network Notes

| Asset | Example |
|---|---|
| Lab network | `192.168.10.0/24` |
| Gateway | `192.168.10.1` |
| Student workstation | `192.168.10.20` |
| Admin workstation | `192.168.10.10` |
| Lab server | `192.168.10.50` |

## Observations

| Observation | Note |
|---|---|
| Student and admin systems are in the same small network | Acceptable for a lab, but should be reviewed in real environments |
| The lab server is reachable inside the lab network | Access should be limited to users or systems that need it |
| No separate guest network is shown in this scenario | Guest access should be controlled more carefully |

## Suggested Actions

- Review which systems need access to the lab server.
- Limit admin-related access where possible.
- Avoid giving guest users broad internal access.

## Learning Connection

This section helped me practice basic network observation, asset awareness, and access control thinking.
