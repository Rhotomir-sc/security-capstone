# Risk Register

## Purpose

In this section, I brought together the main security issues identified during the previous reviews.

My goal was to list each risk clearly and connect it with a practical improvement.

---

## Identified Risks

| ID | Risk | Likelihood | Impact | Level | Recommended Action | Status |
|----|------|------------|--------|-------|--------------------|--------|
| R-01 | The `guest01` account has more access than required | Medium | Medium | Medium | Reduce guest permissions and keep access temporary | Open |
| R-02 | SSH access is allowed from the entire `192.168.10.0/24` network | High | High | High | Limit SSH access to `192.168.10.20` | Open |
| R-03 | Three failed logins were followed by a successful `guest01` login | Medium | High | High | Confirm the login, monitor the account, and reset the password if needed | Review Needed |
| R-04 | A phishing email requested credentials through an external link | High | High | High | Report the email and verify account warnings through the official platform | Review Needed |

---

## Observations

- The risks are connected to identity, network access, authentication logs, and phishing.
- The SSH rule and unusual login pattern need the most attention.
- The risks can be reduced with basic access control, monitoring, and user awareness.
- None of the findings alone prove a real attack because this project uses a fictional learning environment.

---

## Finding

The main issue was that several small weaknesses could affect the same environment at the same time.

I noticed that limiting permissions, restricting SSH access, and reviewing unusual login activity would reduce most of the identified risks.

---

## Recommendations

- Review the high-level risks first.
- Assign only the access each user needs.
- Restrict remote management access.
- Monitor repeated failed login attempts.
- Report suspicious emails and verify requests through official channels.
- Update the risk register when a risk is reduced or closed.

---

## Evidence

- [Risk Register Screenshot](evidence/screenshots/07-risk-register.png)
