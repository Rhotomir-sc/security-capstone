from pathlib import Path
from collections import Counter


def parse_log_line(line):
    """
    Parses a simple key=value log line.
    Example:
    2026-07-07 10:05:44 user=testadmin action=login status=failed
    """
    parts = line.strip().split()
    data = {}

    for part in parts:
        if "=" in part:
            key, value = part.split("=", 1)
            data[key] = value

    return data


def main():
    log_path = Path(__file__).resolve().parent.parent / "sample-logs" / "auth_sample.log"

    if not log_path.exists():
        print("Log file not found.")
        return

    successful_logins = 0
    failed_logins = 0
    failed_users = Counter()

    with log_path.open("r", encoding="utf-8") as file:
        for line in file:
            data = parse_log_line(line)

            user = data.get("user", "unknown")
            status = data.get("status", "unknown")

            if status == "success":
                successful_logins += 1
            elif status == "failed":
                failed_logins += 1
                failed_users[user] += 1

    print("Authentication Log Summary")
    print("--------------------------")
    print(f"Successful logins: {successful_logins}")
    print(f"Failed logins: {failed_logins}")

    print("\nUsers with failed attempts:")
    for user, count in failed_users.items():
        print(f"- {user}: {count}")


if __name__ == "__main__":
    main()
