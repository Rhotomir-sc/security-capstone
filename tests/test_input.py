import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from log_summary import load_events, LOG_FILE
from auth_patterns import detect_sequences

class InputTests(unittest.TestCase):
    def test_real_fixture(self):
        events, skipped = load_events(LOG_FILE, 2026)
        self.assertEqual((len(events), skipped), (5, 0))
        findings = detect_sequences(events)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]['user'], 'guest01')
        self.assertEqual(findings[0]['failed_count'], 3)
    def test_nonmatching_lines_are_counted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'input.log'
            path.write_text('not a supported record\n\n')
            self.assertEqual(load_events(path, 2026), ([], 1))
    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(OSError):
                load_events(Path(directory) / 'missing.log', 2026)
