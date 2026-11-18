# Locked Changed-Input Record - NOT EXECUTED

**STUDENT ACTION REQUIRED.** This document is an empty protocol, not a prediction or completed record. The professor requires a genuine AI-off prediction committed to GitHub before the run; the shared architecture also calls for the run itself to be AI closed. No expected result or direction has been supplied by the agent.

| Field | Record |
|---|---|
| Experiment | cedar-reserve-85 |
| Original input | Analytical reserve_min = 0.03 (3% of portfolio); original client reserve rule unchanged |
| Changed input | Analytical reserve_min = 0.85 (85% of portfolio); scenario only, **not** a change to Cedar's actual 3% reserve rule |
| Other inputs | Frozen config/mandate.json, saved price/signal snapshots and current submitted source |
| Student AI-off prediction | |
| Reasoning | |
| Expected output direction | |
| Expected decision effect | |
| Prediction commit hash and GitHub link | |
| Actual run timestamp | |
| Before: BIL / IEF / LQD / VT weights (%) | |
| After: BIL / IEF / LQD / VT weights (%) | |
| Before / after annual mean estimate (%) | |
| Before / after annual volatility (%) | |
| Before / after solver feasibility and mandate status | |
| Before / after committee recommendation | |
| Difference from prediction | |
| Diagnosis and what was learned | |
| Result file and after-run commit link | |

Before running, close AI assistance. In `config/locked_experiment.json`, fill the four blank student fields yourself. Predict the effects on weights, estimated risk/return, feasibility and the committee decision; explain your financial reasoning without asking AI for the answer.

The earlier unrun 35% proposal was replaced during preparation because the baseline research allocation already holds about 77% BIL, so 35% would not test a binding reserve floor. **This 85% scenario was prepared with AI help. Its numerical and decision outcomes have not been run or supplied as a prediction.** The student's pre-run prediction must still be genuinely written with AI closed.

From the project root, inspect and commit your own prediction and freeze all material model/input files first:

```powershell
git status --short
git add config/locked_experiment.json docs/changed-input-record.md
git commit -m "Record student AI-off prediction before locked experiment"
git push origin main
git rev-parse HEAD
# Retain the genuine prediction commit hash and GitHub commit URL.
.venv\Scripts\python.exe scripts\locked_experiment.py --prediction-commit YOUR_REAL_HASH --remote-branch main --student-ai-off-run
```

Do not run the final command during an AI session. The gate checks nonblank committed student fields, unchanged prediction content and material model/input files, a GitHub origin and reachability from the live remote branch. A script cannot prove independent authorship; your genuine conduct and record remain required. Do not fill fields with placeholders merely to bypass the gate.

Afterward, inspect `outputs/locked_changed_input.json`. Its `before` and `after` objects contain the weights, return, risk, compliance and recommendation. Fill the actual-results rows above in your own words and preserve this record with a **second** commit. Add the result-file and record links to `docs/validation-and-ai-use.md`. The four ordinary stress tests are separate; they are not represented as this locked experiment.
