# 08 - Python Log Helper

## Purpose

This section explains a small Python helper script used to summarize sample authentication logs.

## Related Files

- `scripts/log_summary.py`
- `sample-logs/auth_sample.log`

## What the Script Does

The script reads a fictional sample log file and counts:

- successful login events
- failed login events
- users with repeated failed attempts

## Example Command

```bash
python scripts/log_summary.py
