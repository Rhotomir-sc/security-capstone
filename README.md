# Security Capstone

## Fictional Small Learning Environment Security Review

This repository is a small capstone project that I prepared as part of my cybersecurity learning process.

Instead of using real systems, this project uses a fictional lab scenario created with sample data. The focus of this work is to perform a basic security review through user accounts, access levels, sample login logs, a phishing scenario, firewall rules, a Python log summary, and a risk register.

---

## Scenario

This project is based on a small fictional learning/lab environment.

The environment includes sample user accounts, basic login logs, simple network notes, a phishing email example, and firewall rule examples.

I reviewed this environment from a basic security perspective and tried to write the main points in a short and organized way.

---

## Reviewed Areas

In this project, I worked on the following areas:

- user accounts and access levels
- unnecessary or unclear permissions
- basic network observations
- login logs and failed login attempts
- suspicious points in a phishing email
- overly open access in firewall rules
- sample log summary with Python
- risk register and final summary

---

## File Guide

| File | Short description |
|---|---|
| [01-project-overview.md](01-project-overview.md) | Scenario and scope |
| [02-learning-map.md](02-learning-map.md) | Connection with my learning path |
| [03-identity-access-review.md](03-identity-access-review.md) | User and access review |
| [04-network-review.md](04-network-review.md) | Basic network observations |
| [05-log-review.md](05-log-review.md) | Sample login log review |
| [06-phishing-triage.md](06-phishing-triage.md) | Phishing email review |
| [07-firewall-rule-review.md](07-firewall-rule-review.md) | Firewall rule review |
| [08-python-log-helper.md](08-python-log-helper.md) | Python log helper explanation |
| [09-risk-register.md](09-risk-register.md) | Risk table |
| [10-summary.md](10-summary.md) | Short closing summary |

---

## Python Section

In this project, I used a small Python script:

```text
scripts/log_summary.py
```

The script reads the sample log file and summarizes successful logins, failed login attempts, and users found in the log.

Sample log file:

```text
sample-logs/auth_sample.log
```

This section was added to show how Python can help with simple log review tasks.

---

## Evidence

Screenshots are stored in this folder:

```text
evidence/screenshots/
```

This folder includes screenshots of the repository structure, sample log file, Python output, risk register, and final summary section.

---

## Status

Status: `In progress`

This project is one of the small but organized capstone works in my cybersecurity portfolio.

In this repository, I combined the basic topics I learned into a small scenario and tried to write my review in an organized way.
