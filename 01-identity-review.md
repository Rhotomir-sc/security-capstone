# Identity Review

## Purpose

In this section, I reviewed the user accounts and their access levels in the fictional learning environment.

My goal was to check whether each user had permissions that matched their role.

---

## Users and Roles

| User | Role | Expected Access |
|------|------|-----------------|
| admin01 | Administrator | System management |
| instructor01 | Instructor | Learning content and related user areas |
| student01 | Student | Personal learning area |
| guest01 | Guest | Limited and temporary access |

---

## Observations

- The `admin01` account is used for system management tasks.
- The `instructor01` account can access learning content and related user areas.
- The `student01` account is limited to its own learning area.
- I noticed that the `guest01` account had broader access than expected.

---

## Finding

The main issue was that the `guest01` account had more permissions than it needed.

It would be safer for the guest account to access only the required areas and only for a limited period.

---

## Recommendations

- Reduce the permissions of the `guest01` account.
- Do not use the administrator account for daily user tasks.
- Give users only the access they need.
- Review user accounts and permissions regularly.

---

## Evidence

- [Identity Review Screenshot](evidence/screenshots/01-identity-review.png)
