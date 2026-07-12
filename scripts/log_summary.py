from pathlib import Path
import re


def main():
    log_path = Path(__file__).resolve().parent.parent / "sample-logs" / "auth_sample.log"

    if not log_path.exists():
        print("Log file not found.")
        return

    lines = [
        line.strip()
        for line in log_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    successful_logins = 0
    failed_logins = 0
    users = set()

    for line in lines:
        if "login_success" in line:
            successful_logins += 1

        if "login_failed" in line:
            failed_logins += 1

        user_match = re.search(r"user=([a-zA-Z0-9_.-]+)", line)
        if user_match:
            users.add(user_match.group(1))

    print("Log Summary")
    print("-----------")
    print(f"Total lines reviewed: {len(lines)}")
    print(f"Successful logins: {successful_logins}")
    print(f"Failed login attempts: {failed_logins}")
    print(f"Users found: {', '.join(sorted(users))}")

    if failed_logins >= 3:
        print("Note: Repeated failed logins should be reviewed.")


if __name__ == "__main__":
    main()
