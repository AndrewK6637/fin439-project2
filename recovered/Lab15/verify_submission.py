"""Reproduce the submission evidence without downloading or publishing anything."""
from pathlib import Path
import json
import subprocess
import sys
import urllib.request
import portfolio as p

HERE = Path(__file__).resolve().parent
run = subprocess.run([sys.executable, '-m', 'unittest', 'test_lab15', '-v'],
                     cwd=HERE, capture_output=True, text=True)
(HERE/'verification.txt').write_text(run.stdout + run.stderr, encoding='utf-8')
print(run.stdout + run.stderr)
if run.returncode:
    raise SystemExit(run.returncode)
output = subprocess.run([sys.executable, 'portfolio.py'], cwd=HERE, capture_output=True, text=True, check=True)
(HERE/'portfolio_results.txt').write_text(output.stdout, encoding='utf-8')
results = {'objective': .055, 'objective_status': 'Illustrative: prior lab CPI estimate 2.5% + Cedar 3%; no additional cost assumption',
           'reserve_minimum': .03, 'reserve_eligible': ['BIL']}
for label, last in [('all_months', False), ('last_36', True)]:
    estimates = p.estimate_prices(HERE/'prices.csv', last)
    result = p.optimize_portfolio(estimates['sleeves'], estimates['correlations'], .055, .03, {'BIL'})
    results[label] = {'estimates': estimates, 'result': result}
results['largest_weight_change_pp'] = p.largest_weight_change(
    results['all_months']['result']['weights'], results['last_36']['result']['weights'])
(HERE/'project2_results.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
print('Original output and Project 2 illustrative results reproduced.')
