"""Run checks and create a clean Lab16 ZIP. Standard library only."""
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

HERE = Path(__file__).resolve().parent
FILES = (
    'asof.py', 'test_asof.py', 'README.md', 'LAB16_REFLECTION.md',
    'SUBMISSION.md', 'validation_output.txt', 'submission_checks.txt',
    'prepare_submission.py', '.gitignore',
)


def main():
    logs = []

    def run(folder, *args):
        result = subprocess.run([sys.executable, *args], cwd=folder,
                                capture_output=True, text=True)
        logs.append(f"COMMAND: python {' '.join(args)}\n"
                    + result.stdout + result.stderr + f'\nEXIT: {result.returncode}\n')
        if result.returncode:
            raise RuntimeError(logs[-1])
        return result.stdout

    source = (HERE / 'asof.py').read_bytes()
    marker = b"DECISION_DATE = '2026-03-31'"
    if source.count(marker) != 1:
        raise ValueError('Restore DECISION_DATE to 2026-03-31 before packaging.')
    # Execute an edited copy independently; the delivered source stays unchanged.
    with tempfile.TemporaryDirectory(prefix='lab16_stress_') as temp:
        (Path(temp) / 'asof.py').write_bytes(
            source.replace(marker, b"DECISION_DATE = '2026-04-15'", 1))
        logs.append('APRIL 15: independent edited source copy')
        output = run(temp, 'asof.py')
        for ticker, display in [('AAA', '+5.83%, March 2026'),
                                ('BBB', '-5.15%, March 2026'),
                                ('CCC', '+1.82%, February 2026')]:
            line = next(line for line in output.splitlines() if line.startswith(ticker))
            if line.count(display) != 2:
                raise AssertionError(line)
        logs.append('PASS: all three April 15 as-of signals equal naive signals.')
    if (HERE / 'asof.py').read_bytes() != source:
        raise AssertionError('Delivered source changed during stress test.')
    logs.append('PASS: delivered source retains March 31 unchanged.')
    run(HERE, 'asof.py')
    run(HERE, '-m', 'unittest', '-v', 'test_asof.py')
    (HERE / 'validation_output.txt').write_text('\n'.join(logs), encoding='utf-8')
    (HERE / 'submission_checks.txt').write_text('\n'.join(logs), encoding='utf-8')
    archive = HERE.parent / 'Lab16_Submission.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as package:
        for name in FILES:
            package.write(HERE / name, 'Lab16/' + name)
    with zipfile.ZipFile(archive) as package:
        if package.testzip() is not None:
            raise AssertionError('ZIP integrity check failed.')
        for name in FILES:
            if package.read('Lab16/' + name) != (HERE / name).read_bytes():
                raise AssertionError(f'ZIP content mismatch: {name}')
        # Confirm the deliverable runs without relying on the workspace.
        with tempfile.TemporaryDirectory(prefix='lab16_package_') as temp:
            package.extractall(temp)
            run(Path(temp) / 'Lab16', 'asof.py')
            run(Path(temp) / 'Lab16', '-m', 'unittest', '-v', 'test_asof.py')
    print('\n'.join(logs))
    print(f'PASS: ZIP integrity, all {len(FILES)} files match, extracted program/tests pass.')
    print(f'Package: {archive}')
    print('Student-only blanks intentionally remain. Refresh this ZIP after filling them.')


if __name__ == '__main__':
    main()
