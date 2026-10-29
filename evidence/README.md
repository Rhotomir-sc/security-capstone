# Capstone evidence and limitations

The screenshots in `screenshots/` were created during earlier portfolio documentation. **An image of a written report is not proof that a control was deployed or a vulnerability exploited.** The actual executable evidence in this repo is the [synthetic SSH log](../sample-logs/auth_sample.log), [Python script](../scripts/log_summary.py), and [automated tests](../tests/test_input.py).

## Screenshot-to-section index

| File | Related section | Interpretation |
|---|---|---|
| [01-identity-review.png](screenshots/01-identity-review.png) | [Identity review](../01-identity-review.md) | Scenario analysis; access change not independently verified |
| [02-network-review.png](screenshots/02-network-review.png) | [Network review](../02-network-review.md) | Documentation context; not a verified network deployment |
| [03-log-review.png](screenshots/03-log-review.png) | [Log review](../03-log-review.md) | Report illustration; use the committed SSH log and script for reproducible evidence |
| [04-phishing-review.png](screenshots/04-phishing-review.png) | [Phishing review](../04-phishing-review.md) | Educational example; not an actual enterprise phishing incident |
| [05-firewall-review.png](screenshots/05-firewall-review.png) | [Firewall review](../05-firewall-review.md) | Scenario rules; live allow/deny tests pending |
| [06-python-helper.png](screenshots/06-python-helper.png) | [Python helper](../06-python-helper.md) | Historical output; current output may differ |
| [07-risk-register.png](screenshots/07-risk-register.png) | [Risk register](../07-risk-register.md) | Written risk assessment; no production risk acceptance implied |
| [08-summary.png](screenshots/08-summary.png) | [Summary](../08-summary.md) | Earlier report illustration; not additional technical execution |

## Reproduce the current technical work

From the repository root, with Python 3.10+:

```sh
python scripts/log_summary.py
python -m unittest discover -s tests -v
```

See [REPRODUCE.md](../REPRODUCE.md) for the expected result, assumptions about the year of the syslog fixture, and validation limitations.

## Planned verification

The [remediation verification plan](../remediation-verification.md) describes missing before/after permission tests, firewall connection tests, and follow-up checks. These are **pending**, not completed work. Keep future evidence separate from historical screenshots, label its execution date and environment, and do not commit personal or production data.

[Back to capstone](../README.md)
