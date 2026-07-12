# 08 - Python Log Helper

## Purpose

This section explains the small Python helper script used in this project.

The script was added to show how Python can support a simple log review task.

## Script Location

```text
scripts/log_summary.py
```

## Sample Log File

```text
sample-logs/auth_sample.log
```

## What the Script Does

The script reads the sample authentication log and summarizes:

- successful logins
- failed login attempts
- users with failed attempts

## Example Output

```text
Authentication Log Summary
--------------------------
Successful logins: 3
Failed logins: 4

Users with failed attempts:
- testadmin: 2
- guest: 1
- student01: 1
```

## Short Note

This is a simple helper script, not an advanced security tool.

It helped me practice basic Python scripting, log reading, and small automation for a security-related task.

## Learning Connection

This section connects Python basics with log analysis and beginner SOC-style review.
