# Phishing Review

## Purpose

In this section, I reviewed a fictional email sent to the `student01` account.

My goal was to check the sender, message content, link, and other signs that could indicate a phishing attempt.

---

## Email Details

| Field | Information |
|-------|-------------|
| From | Learning Platform Support `<support@learn-platform-help.example>` |
| To | `student01` |
| Subject | Password Expires Today |
| Link | `https://learning-platform-login.example/reset` |
| Request | Open the link and confirm account credentials |

---

## Observations

- The email used urgent language to make the user act quickly.
- The sender domain did not match the official learning environment.
- The message asked the user to open an external password reset link.
- The link directed the user to a different domain from the sender address.
- The email requested account credentials through the linked page.

---

## Finding

The main issue was that the email used a password warning to direct the user to an external login page.

I noticed that the sender address and the password reset link used different and unfamiliar domains.

---

## Recommendations

- Do not open the link or enter account credentials.
- Report the email as a possible phishing attempt.
- Confirm password warnings through the official learning platform.
- Check the sender address and destination link before taking action.
- Enable multi-factor authentication where possible.

---

## Evidence

- [Phishing Review Screenshot](evidence/screenshots/04-phishing-review.png)
