# Log Review

## Purpose

In this section, I reviewed sample SSH authentication logs generated on the `lab-server`.

My goal was to separate successful and failed login attempts and check whether there was a login pattern that needed attention.

---

## Log Summary

| Status | User | Source IP | Count |
|--------|------|-----------|-------|
| Successful login | admin01 | 192.168.10.20 | 1 |
| Failed login | guest01 | 192.168.10.30 | 3 |
| Successful login | guest01 | 192.168.10.30 | 1 |

---

## Observations

- The `admin01` account successfully logged in once from `192.168.10.20`.
- The `guest01` account had three consecutive failed login attempts from `192.168.10.30`.
- Shortly after the failed attempts, a successful login occurred for the same user and source IP.
- This pattern does not prove an attack, but it should be reviewed.

---

## Finding

The main issue was that a successful login occurred after three consecutive failed attempts for the `guest01` account.

It would be safer to confirm whether this login was made by the expected user.

---

## Recommendations

- Review the login history of the `guest01` account.
- Monitor repeated failed login attempts.
- Reset the guest account password if necessary.
- Limit unnecessary SSH access.

---

## Evidence

- [Authentication Log](sample-logs/auth_sample.log)
- [Log Review Screenshot](evidence/screenshots/03-log-review.png)
