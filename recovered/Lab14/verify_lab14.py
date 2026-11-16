"""Run the known-answer checks and execute changed copies of portfolio.py."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile

import portfolio as p

HERE = Path(__file__).resolve().parent


def run(path):
    return subprocess.run([sys.executable, str(path)], capture_output=True, text=True)


def main():
    source_path = HERE / "portfolio.py"
    original = source_path.read_text(encoding="utf-8")
    baseline = run(source_path)
    assert baseline.returncode == 0, baseline.stderr
    expected = [
        "Benchmark | 0.0 / 0.0 / 40.0 / 60.0 | 6.80% | 10.46% | 0.0% | yes",
        "Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 5.20% | 5.21% | 50.0% | no",
        "Inverse volatility | 84.3 / 6.0 / 7.0 / 2.6 | 3.77% | 1.05% | 90.3% | no",
    ]
    for row in expected:
        assert row in baseline.stdout, row
    logs = ["KNOWN ANSWERS: all fields match", baseline.stdout]
    with tempfile.TemporaryDirectory() as folder:
        probe = Path(folder) / "portfolio_probe.py"
        probe.write_text(original.replace("0.25", "0.50"), encoding="utf-8")
        changed = run(probe)
        assert changed.returncode == 0, changed.stderr
        assert "6.80% | 11.00% | 0.0% | yes" in changed.stdout
        logs.extend(["IG/equity correlation = 0.50 in both cells:", changed.stdout])
        probe.write_text(original.replace("0.25", "1.30"), encoding="utf-8")
        invalid = run(probe)
        assert invalid.returncode != 0 and "between -1 and 1" in invalid.stderr
        assert not invalid.stdout
        logs.extend(["IG/equity correlation = 1.30: rejected", invalid.stderr])
        probe.write_text(original.replace("0.25", "0.50", 1), encoding="utf-8")
        asymmetric = run(probe)
        assert asymmetric.returncode != 0 and "not symmetric" in asymmetric.stderr
        logs.extend(["Asymmetric correlation: rejected", asymmetric.stderr])
    assert source_path.read_text(encoding="utf-8") == original
    assert run(source_path).stdout == baseline.stdout
    logs.append("Original 0.25 correlation preserved; normal rerun matches.")

    spec = importlib.util.spec_from_file_location("mandate", HERE / "mandate.py")
    mandate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mandate)
    for name, weights in p.define_portfolios(p.SLEEVES).items():
        allocation = dict(zip(p.SLEEVES, weights))
        mapped = [100 * allocation.get(holding, 0) for holding in mandate.HOLDINGS]
        checks = mandate.evaluate(mapped)
        failures = [label for label, _, passed in checks if not passed]
        assert failures == (["Reserve"] if name == "Benchmark" else [])
        logs.append(f"{name} mandate allocation failures: {failures or 'none'}")
    assert mandate.CANDIDATES["E"] == [0, 0, 0, 60, 40, 0, 0, 0]
    mandate_run = run(HERE / "mandate.py")
    assert mandate_run.returncode == 0
    logs.extend(["MANDATE RERUN (including E)", mandate_run.stdout,
                 "ALL LAB 14 AUTOMATED CHECKS PASSED"])
    (HERE / "verification.txt").write_text("\n".join(logs), encoding="utf-8")
    (HERE / "portfolio_results.txt").write_text(baseline.stdout, encoding="utf-8")
    print("\n".join(logs))


if __name__ == "__main__":
    main()
