# Security Capstone

## Overview

This repository contains a student-level security capstone based on a fictional small learning environment.

The goal of this capstone is to connect several basic cybersecurity topics into one organized review scenario. It brings together identity and access review, basic network observation, authentication log analysis, phishing triage, firewall rule review, simple Python log summarization, and risk documentation.

## Scenario

**Fictional Small Learning Environment Security Review**

In this scenario, I review a small fictional learning/lab environment from a basic security perspective.

The environment includes:

- student user accounts
- possible test or admin accounts
- sample authentication logs
- basic network observations
- a sample phishing scenario
- simple firewall rule examples
- fictional log data for Python-based summarization

## Purpose

The purpose of this capstone is not to perform a real penetration test, professional audit, or production security review.

The purpose is to show that I can:

- follow a clear security review process
- connect different learning areas into one scenario
- document observations in a simple and organized way
- think about basic identity, network, log, phishing, and firewall risks
- convert findings into risk-based notes
- use a small Python script to support log review

## What This Capstone Covers

- Identity and access review
- Basic network observation
- Authentication log analysis
- Phishing triage
- Firewall rule review
- Python log summarization
- Risk register
- Final learning summary

## Repository Structure

| File / Folder | Purpose |
|---|---|
| `01-scenario-and-scope.md` | Defines the fictional scenario, scope, and limits |
| `02-learning-sources-map.md` | Shows which previous learning areas supported this capstone |
| `03-identity-access-review.md` | Reviews basic user account and access risks |
| `04-network-observation.md` | Documents simple network observations |
| `05-log-analysis.md` | Reviews sample authentication log patterns |
| `06-phishing-triage.md` | Reviews a sample suspicious email scenario |
| `07-firewall-rule-review.md` | Checks basic firewall rule hygiene |
| `08-python-log-helper.md` | Explains the small Python log helper script |
| `09-risk-register.md` | Converts observations into a small risk table |
| `10-final-summary.md` | Summarizes the final learning outcome |
| `scripts/` | Contains the Python helper script |
| `sample-logs/` | Contains fictional sample authentication logs |
| `evidence/screenshots/` | Contains a small number of screenshots showing structure, sample data, script output, and final documentation |

## Structure Logic

Although this capstone contains 10 files, the structure follows 3 main parts: an introduction section, a technical review section, and a closing section.

| Section | Files | Purpose |
|---|---|---|
| Introduction | `01-scenario-and-scope.md`, `02-learning-sources-map.md` | Defines the scenario, scope, limits, and learning sources |
| Technical Review | `03-identity-access-review.md` to `08-python-log-helper.md` | Documents the main security review steps |
| Closing | `09-risk-register.md`, `10-final-summary.md` | Converts observations into risks and summarizes the learning outcome |

## Capstone Flow

The capstone follows a simple review flow:

1. Define the scenario and scope
2. Connect the scenario to previous learning
3. Review identity and access risks
4. Observe the network side
5. Analyze sample authentication logs
6. Triage a suspicious email example
7. Review firewall rule risks
8. Use Python to summarize sample logs
9. Convert findings into a risk register
10. Write a final learning summary

## Supporting Files

### Python Helper

The Python helper script is stored in `scripts/log_summary.py`.

It reads a fictional authentication log file and summarizes:

- successful login events
- failed login events
- users with repeated failed attempts

This script is intentionally simple. It is used to practice basic log parsing and Python-supported security review.

### Sample Logs

The sample log file is stored in `sample-logs/auth_sample.log`.

All log data in this repository is fictional and created only for this student-level scenario.

### Evidence

Screenshots are stored in `evidence/screenshots/`.

The screenshots are used only to show:

- repository structure
- sample log file
- Python script output
- risk register
- closing summary

## Important Note

This project does not use real company data, real user data, or real production systems.

It is a controlled student portfolio project built with fictional examples.

This capstone is not presented as:

- a real penetration test
- a professional audit
- an enterprise security assessment
- an advanced SIEM project

## Learning Outcome

This capstone helped me practice connecting separate cybersecurity topics into one small security review process.

The main learning outcome is that security work is not only about identifying issues. It is also about documenting observations clearly, understanding basic risk, and suggesting practical improvements.

## Status

This repository is part of my cybersecurity learning portfolio and supports my long-term direction toward cloud and identity security.
