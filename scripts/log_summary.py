"""Summarize fictional SSH logs and calculate time-bounded review findings."""
import argparse
from collections import Counter
from datetime import datetime
from pathlib import Path
import re
from auth_patterns import detect_sequences

LOG_FILE = Path(__file__).resolve().parent.parent / 'sample-logs' / 'auth_sample.log'
PATTERN = re.compile(r'^([A-Z][a-z]{2}\s+\d{1,2}\s+\d\d:\d\d:\d\d) \S+ sshd\[\d+\]: (Accepted|Failed) password for (\S+) from ([\d.]+) port \d+ ssh2$')


def load_events(path, year):
    events, skipped = [], 0
    for line in path.read_text(encoding='utf-8').splitlines():
        match = PATTERN.match(line)
        if not match:
            if line.strip():
                skipped += 1
            continue
        stamp, status, user, source_ip = match.groups()
        months = {name: i for i, name in enumerate('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(), 1)}
        month, day, clock = stamp.split()
        timestamp = datetime.fromisoformat(f'{year:04d}-{months[month]:02d}-{int(day):02d}T{clock}')
        events.append(dict(timestamp=timestamp, user=user, source_ip=source_ip,
                           status='success' if status == 'Accepted' else 'failed'))
    return events, skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=LOG_FILE)
    parser.add_argument('--year', type=int, default=2026, help='Assumed fixture year; syslog has no year')
    parser.add_argument('--threshold', type=int, default=3)
    parser.add_argument('--window-minutes', type=float, default=10)
    args = parser.parse_args()
    try:
        events, skipped = load_events(args.input, args.year)
        findings = detect_sequences(events, args.threshold, args.window_minutes)
    except (OSError, ValueError, KeyError) as exc:
        parser.exit(2, f'Error: {exc}\n')
    print('Security Capstone - SSH Log Summary')
    print(f'Assumed year: {args.year}; one local timezone; no year rollover support')
    print(f'Total events: {len(events)}')
    print(f"Successful logins: {sum(e['status'] == 'success' for e in events)}")
    print(f"Failed logins: {sum(e['status'] == 'failed' for e in events)}")
    print(f'Skipped nonmatching lines: {skipped}')
    print('\nUser Summary')
    for user in sorted({e['user'] for e in events}):
        counts = Counter(e['status'] for e in events if e['user'] == user)
        print(f"{user}: success={counts['success']} failed={counts['failed']}")
    print(f'\nSequences requiring review: {len(findings)}')
    for f in findings:
        print(f"{f['user']} from {f['source_ip']}: {f['failed_count']} failures "
              f"before success at {f['success_time'].isoformat(sep=' ')} "
              f'(within {args.window_minutes:g} minutes).')
    if not findings:
        print('No sequence met this rule; absence of a match does not prove safety.')


if __name__ == '__main__':
    main()
