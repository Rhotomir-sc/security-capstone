# Python Helper

## Purpose

In this section, I created a small Python script to summarize the SSH authentication records in `auth_sample.log`.

My goal was to count successful and failed login attempts and make the main log pattern easier to review.

---

## Script Details

| Item | Information |
|------|-------------|
| Script | `scripts/log_summary.py` |
| Input | `sample-logs/auth_sample.log` |
| Language | Python |
| Output | Login counts and a short review note |

---

## Observations

- The script reads the same log file used in the Log Review section.
- It found five authentication events in total.
- Two login attempts were successful.
- Three login attempts failed.
- The `guest01` account had three failed attempts followed by one successful login.

---

## Finding

The script made it easier to see the repeated failed attempts connected to the `guest01` account.

I still reviewed the original log records because the script provides a summary and does not replace manual analysis.

---

## Recommendations

- Use the script together with the original log records.
- Review repeated failed login attempts carefully.
- Confirm whether unusual successful logins were expected.
- Improve the script gradually as more log examples are added.

---

## Evidence

- [Python Script](scripts/log_summary.py)
- [Python Helper Screenshot](evidence/screenshots/06-python-helper.png)
