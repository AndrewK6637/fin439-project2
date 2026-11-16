"""Reproduce numerical checks and the temporary on-disk negative-weight probe."""
import ast
import importlib.util
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "mandate.py"
log = [f"Python executable: {sys.executable}"]


def run_checker():
    result = subprocess.run([sys.executable, "mandate.py"], cwd=ROOT,
                            capture_output=True, text=True, check=True)
    log.append("COMMAND: python mandate.py\nExit code: 0\n" + result.stdout)
    return result.stdout


def load_checker():
    # Compile directly so a temporary edit cannot be masked by cached bytecode.
    namespace = {"__name__": "mandate_test"}
    exec(compile(SOURCE.read_text(encoding="utf-8"), str(SOURCE), "exec"), namespace)
    return namespace


original = SOURCE.read_text(encoding="utf-8")
ast.parse(original)
log.append("SYNTAX: ast.parse(mandate.py) PASS")
normal = run_checker()
m = load_checker()
assert m["reserve_minimum"]() == 3.0
expected = {
    "A": ([100, 0, 14, 100, 0], [True] * 5),
    "B": ([100, 0, 1, 85, 9], [True, True, False, False, False]),
    "C": ([100, 0, 2, 100, 8], [True, True, False, True, True]),
    "D": ([100, 0, 100, 100, 0], [True] * 5),
    "E": ([100, 0, 0, 100, 0], [True, True, False, True, True]),
}
for name, (values, passes) in expected.items():
    checks = m["evaluate"](m["CANDIDATES"][name])
    assert [c[1] for c in checks] == values
    assert [c[2] for c in checks] == passes
    for label, value, passed in checks:
        assert f"{label}: {value:.1f}% {'pass' if passed else 'FAIL'}" in normal
log.append("PASS: all A/B/C/D/E measured values and rule outcomes; reserve minimum 3.0%")
try:
    modified = original.replace('"A": [2, 2, 10, 60, 26, 0, 0, 0]',
                                '"A": [-2, 2, 10, 64, 26, 0, 0, 0]')
    assert modified != original
    SOURCE.write_text(modified, encoding="utf-8")
    probe = run_checker()
    p = load_checker()
    checks = p["evaluate"](p["CANDIDATES"]["A"])
    assert [c[1] for c in checks] == [100, -2, 10, 100, 0]
    assert [c[2] for c in checks] == [True, False, True, True, True]
    assert "fails 1 rule(s)" in probe.split("Candidate B")[0]
    (ROOT / "probe_results.txt").write_text(
        "Temporary A: Cash 2 -> -2; Global equity 60 -> 64.\n"
        "COMMAND: python mandate.py\nExit code: 0\n\n" + probe +
        "\nASSERTIONS: PASS; A has exactly one failure (minimum weight).\n",
        encoding="utf-8")
    log.append("PASS: negative-weight probe; actual output saved in probe_results.txt")
finally:
    SOURCE.write_text(original, encoding="utf-8")
restored = run_checker()
assert restored == normal
assert SOURCE.read_text(encoding="utf-8") == original
(ROOT / "normal_results.txt").write_text(restored, encoding="utf-8")
log.append("PASS: original weights restored and normal output reproduced exactly")
# Input perturbations demonstrate dynamic calculations and shared-issuer grouping.
m["QUARTERLY_DISTRIBUTION"] = 1_000_000
assert m["reserve_minimum"]() == 4
m["QUARTERLY_DISTRIBUTION"] = 750_000
assert m["evaluate"]([0, 0, 0, 90, 0, 0, 6, 4])[-1][1:] == (10, False)
m["LIQUIDITY_WINDOW"] = 1
assert m["evaluate"](m["CANDIDATES"]["A"])[3][1] == 14
assert normal.count("requires CIO clarification") == len(expected)
assert all(len(m["evaluate"](w)) == 5 for w in m["CANDIDATES"].values())
log.append("PASS: changed inputs affect reserve, issuer exposure, and liquidity; exactly five numeric checks")
report = ROOT / "Lab13_Report.md"
if report.exists():
    content = report.read_text(encoding="utf-8")
    for i in range(1, 11):
        assert f"S{i}" in content
    for section in "ABCDEFGH":
        assert f"## {section}." in content
    assert "## I. Code understanding" in content
    assert "## Submission coverage" in content
    d_output = restored[restored.index("Candidate D"):].split("Candidate E")[0].strip()
    assert d_output in content
    log.append("PASS: report includes S1-S10, A-H, code understanding, coverage map, and exact D output")
log.append("SOURCE REVIEW: results derive from inputs; S9 is printed only, never tested numerically.")
log.append("GITHUB: no .git in workspace or any ancestor; no existing remote available. No commit or push performed.")
(ROOT / "verification.txt").write_text(
    "COMMAND: python verify_lab13.py\n" + "\n\n".join(log) + "\n", encoding="utf-8")
print("PASS: numerical checks, negative-weight probe, restoration, dynamic-input tests, and available report checks")
