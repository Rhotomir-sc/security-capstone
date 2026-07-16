# Network Review

## Purpose

In this section, I reviewed the main devices, network connections, and services in the fictional learning environment.

My goal was to understand the role of each system on the network and check whether any access was left more open than necessary.

---

## Network Structure

| System | IP Address | Role |
|--------|------------|------|
| router-firewall | 192.168.10.1 | Gateway and basic traffic control |
| lab-server | 192.168.10.10 | Learning content and management tasks |
| instructor-pc | 192.168.10.20 | Instructor workstation |
| student-pc | 192.168.10.30 | Student workstation |

---

## Observed Services

| System | Port | Service | Purpose |
|--------|------|---------|---------|
| lab-server | 22 | SSH | Remote management |
| lab-server | 80 | HTTP | Access to learning content |

---

## Observations

- The `lab-server` uses the HTTP service to provide learning content.
- The SSH service is open for remote server management.
- The `instructor-pc` and `student-pc` are connected to the same small learning network.
- It would be safer to limit SSH access to devices that need management access.

---

## Finding

The main issue was that SSH access was open to all devices on the network.

The `student-pc` does not need to connect to the server through SSH, so limiting this access would be safer.

---

## Recommendations

- Limit SSH access to the required administrator or instructor devices.
- Keep unused services closed.
- Review open ports on the server regularly.
- Keep an updated list of network devices and services.

---

## Evidence

- [Network Review Screenshot](evidence/screenshots/02-network-review.png)
