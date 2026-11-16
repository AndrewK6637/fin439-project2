# Locked Changed-Input Record ? NOT EXECUTED

**STUDENT ACTION REQUIRED.** This document is an empty protocol, not a prediction or completed record. The professor requires a genuine AI-off prediction committed to GitHub before the run; the shared architecture also calls for the run itself to be AI closed. No expected result or direction has been supplied by the agent.

| Field | Record |
|---|---|
| Experiment | cedar-reserve-35 |
| Original input | Analytical reserve_min = 0.03 (3% of portfolio); original client reserve rule unchanged |
| Changed input | Analytical reserve_min = 0.35 (35% of portfolio); scenario only |
| Other inputs | Frozen config/mandate.json, saved price/signal snapshots and current submitted source |
| Student AI-off prediction | |
| Reasoning | |
| Expected output direction | |
| Expected decision effect | |
| Prediction commit hash and GitHub link | |
| Actual run timestamp | |
| Actual result | |
| Difference from prediction | |
| Diagnosis and what was learned | |

Before running, close AI assistance. In `config/locked_experiment.json`, fill the four blank student fields yourself. Predict the effects on weights, estimated risk/return, feasibility and the committee decision; explain your financial reasoning without asking AI for the answer.

From the project root, inspect and commit your own prediction and freeze all material model/input files first:

```powershell
git status --short
git add config/locked_experiment.json docs/changed-input-record.md
git commit -m "Record student AI-off prediction before locked experiment"
git rev-parse HEAD
# STUDENT ACTION REQUIRED: configure your actual GitHub origin and authorize/push this commit.
git push -u origin main
# Retain the genuine prediction commit hash and GitHub commit URL.
python scripts/locked_experiment.py --prediction-commit YOUR_REAL_HASH --remote-branch main --student-ai-off-run
```

Do not run the final command during an AI session. The gate checks nonblank committed student fields, unchanged prediction content, a GitHub origin and reachability from the live remote branch. A script cannot prove independent authorship; your genuine conduct and record remain required. Do not fill fields with placeholders merely to bypass the gate.

Afterward, inspect `outputs/locked_changed_input.json`, fill the actual results and diagnosis here, and preserve this record with a subsequent commit. Link the same record from validation-and-ai-use.md. The four ordinary stress tests are separate; they are not represented as this locked experiment.
