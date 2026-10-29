# Security Capstone

## Start here

1. [Scenario and evidence boundaries](scenario.md)
2. [Reproduce the analysis](REPRODUCE.md)
3. [Risk register](07-risk-register.md)
4. [Remediation verification — planned](remediation-verification.md)

The current project is a fictional assessment with runnable analysis. Live remediation is a planned extension.


## About the Project

This repository contains a fictional small-scale security review created for learning and portfolio purposes.

The project brings together the basic cybersecurity knowledge I gained through the Google Cybersecurity Certificate, TryHackMe labs, and university coursework into a single defensive security scenario.

Throughout the project, I review fundamental topics such as identity and access, networking, log analysis, phishing, firewall rules, Python, and risk assessment.

---

## Technical focus and evidence status

The executable part of this capstone examines a **synthetic SSH authentication log** and identifies a time-bounded failed-login-then-success sequence. The Python script and unit tests are reproducible using the [run guide](REPRODUCE.md).

The identity, firewall, phishing, and network sections are **scenario assessments and proposed controls**. Remediation changes and allow/deny network verification remain **planned**, as recorded in the [verification plan](remediation-verification.md). Screenshots of earlier reports are not proof of live deployment.

This differs from the [Google integrated case](https://github.com/Rhotomir-sc/google-cybersecurity-portfolio-pack/tree/main/integrated-security-case), which uses fictional cloud sign-in events, web logs, and SQL. The projects exercise related analysis methods on distinct datasets.

---

## Repository Structure

| File | Description |
|------|-------------|
| 01-identity-review.md | Review of users, roles, and basic access permissions |
| 02-network-review.md | Basic network observations and service review |
| 03-log-review.md | Analysis of sample log records and security events |
| 04-phishing-review.md | Review of a sample phishing email |
| 05-firewall-review.md | Review of basic firewall rules |
| 06-python-helper.md | Small Python helper used in the project |
| 07-risk-register.md | Identified risks and suggested improvements |
| 08-summary.md | Overall project summary and learning outcomes |

---

## Evidence

Project screenshots are explained in the [evidence index](evidence/README.md), while the SSH input fixture and runnable Python analysis are linked in the [reproduction guide](REPRODUCE.md).

---

## Disclaimer

This project is based on a fictional learning environment.

No real organization, production environment, or sensitive data is included.

The project was created for learning and portfolio purposes only.
