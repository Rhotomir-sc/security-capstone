# Firewall Review

## Purpose

In this section, I reviewed the basic firewall rules used in the fictional learning environment.

My goal was to check whether access to the `lab-server` was limited to the devices that actually needed it.

---

## Firewall Rules

| Rule | Source | Destination | Port | Action | Purpose |
|------|--------|-------------|------|--------|---------|
| 01 | 192.168.10.0/24 | 192.168.10.10 | 22 / SSH | Allow | Remote server management |
| 02 | 192.168.10.0/24 | 192.168.10.10 | 80 / HTTP | Allow | Access to learning content |
| 03 | Any | 192.168.10.10 | Any | Deny | Block other incoming traffic |

---

## Observations

- HTTP access is available to devices on the learning network.
- SSH access is also allowed from the entire `192.168.10.0/24` network.
- This rule allows both the `instructor-pc` and `student-pc` to reach the SSH service.
- The `student-pc` does not need remote management access to the server.

---

## Finding

The main issue was that the SSH rule allowed access from the entire learning network.

This access is broader than necessary because only the instructor or administrator device should be able to manage the server remotely.

---

## Recommendations

- Limit SSH access to `192.168.10.20`, which belongs to the `instructor-pc`.
- Keep HTTP access available for the learning network.
- Keep the default deny rule for other incoming traffic.
- Review firewall rules regularly and remove rules that are no longer needed.

---

## Evidence

- [Firewall Review Screenshot](evidence/screenshots/05-firewall-review.png)
