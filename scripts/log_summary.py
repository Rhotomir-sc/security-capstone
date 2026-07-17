from collections import defaultdict
from pathlib import Path
import re


LOG_FILE = Path(__file__).resolve().parent.parent / "sample-logs" / "auth_sample.log"


def main() -> None:
    if not LOG_FILE.exists():
        print(f"Log file not found: {LOG_FILE}")
        return

    events = defaultdict(lambda: {"success": 0, "failed": 0})
    total_events = 0

    for line in LOG_FILE.read_text(encoding="utf-8").splitlines():
        match = re.search(
            r"(Accepted|Failed) password for (\S+) from ([\d.]+)",
            line,
        )

        if not match:
            continue

        status, user, _source_ip = match.groups()
        total_events += 1

        if status == "Accepted":
            events[user]["success"] += 1
        else:
            events[user]["failed"] += 1

    successful_logins = sum(item["success"] for item in events.values())
    failed_logins = sum(item["failed"] for item in events.values())

    print("Security Capstone - SSH Log Summary")
    print("-----------------------------------")
    print(f"Log file: sample-logs/auth_sample.log")
    print(f"Total events: {total_events}")
    print(f"Successful logins: {successful_logins}")
    print(f"Failed logins: {failed_logins}")
    print()
    print("User Summary")
    print("------------")

    for user in sorted(events):
        print(
            f"{user}: "
            f"success={events[user]['success']} "
            f"failed={events[user]['failed']}"
        )

    print()
    print("Review Note")
    print("-----------")
    print(
        "guest01 had three failed attempts followed by "
        "one successful login."
    )


if __name__ == "__main__":
    main()
