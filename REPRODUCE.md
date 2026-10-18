# Reproduce the SSH analysis

Requires Python 3.10+; standard library only. From the repository root:

```sh
python scripts/log_summary.py
python -m unittest discover -s tests -v
```

Expected: 5 events, 2 successful and 3 failed logins; one sequence for guest01 from 192.168.10.30, ending at 09:15:02.

Options: `--input PATH --year 2026 --threshold 3 --window-minutes 10`.
The year is an explicit assumption because the fixture is yearless syslog. The parser supports this fixture's IPv4 SSH password format and reports skipped lines. All records must use one timezone and year; year rollover is unsupported.

The detector sorts timestamps and groups by user and IP. A success resets the sequence. Equal timestamps do not prove order; duplicate rows count as separate events. A finding is a review lead, not an attack verdict.

Tests cover unsorted input, success before failures, expired failures, different users/IPs, equal timestamps, thresholds, and reset after success. Historical screenshots may differ from current output.
