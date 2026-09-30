"""Run the complete automated ontology quality suite before synchronising."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def main():
    commands = (
        [sys.executable, '-B', '-m', 'unittest', 'discover',
         '-s', 'semantics/quality', '-p', 'test_*.py'],
        [sys.executable, '-B', 'semantics/quality/check.py'],
    )
    failed = False
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, check=False)
        failed = failed or result.returncode != 0
    print('FAIL: resolve errors before synchronising.' if failed else
          'PASS: automated suite complete; complete the documented human review before synchronising.',
          flush=True)
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
