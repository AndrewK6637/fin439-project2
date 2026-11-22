# Video 2 — How the app reaches its answer

**Rehearsal notes, not an actual transcript. Maximum 5 minutes.** Webcam on; clear audio. Show the code and a saved test result. Do not claim a fresh personal test unless you run it.

**What this video does:** Trace the displayed decision through code. In your editor, click **`config/mandate.json` → `src/data.py` → `src/engine.py` → `src/signal.py` → `src/workflow.py` → `docs/changed-input-record.md`**. Open `outputs/locked_changed_input.json` for the saved result. End on the running app's Executive dashboard. Put the files in easy-to-read editor tabs before recording.

**Before recording:** Open the project folder in VS Code. Open the named files as editor tabs, enlarge the text, and open a terminal. Put `config/mandate.json` on screen **before you press Record**. For the live app ending, run `.venv\Scripts\python.exe -m streamlit run app.py` and open the printed Local URL. Turn on webcam and microphone. In VS Code, use **Ctrl+F within the file currently on screen**; press Esc after finding a term so you can point to it.

**Show on screen:** In `config/mandate.json`, point to `estimation_months: 60`, `cpi_assumption: 0.025`, `real_return_objective: 0.03`, and missing `risk_limit`/`current_weights`. In `src/data.py`, show where saved prices become monthly returns. In `src/engine.py`, show the `metrics`, `rules`, and `optimize` functions. In `src/signal.py`, show the CPI calculation/effective reserve rule. In `src/workflow.py`, show `stop_decision` and `run`. In the locked record and JSON, show the 85% prediction and infeasible result. Finish with the app's Not Known mandate and Reject decision. You do not need to read code line by line.

## Opening — start on `config/mandate.json`

**SHOW:** Start recording with `config/mandate.json` open and the file explorer visible. **Ctrl+F:** `"estimation_months": 60`.

“This is Cedar's mandate file. I used these inputs to test a research portfolio, then decided whether the result was enough to invest. OpenAI Codex helped with the complicated code, automated tests, and drafting. I used that work to examine the numbers and challenge the assumptions. The investment recommendation is mine. This is educational work, not investment advice.”

**SHOW:** Point to the open `config/mandate.json`, `src/engine.py`, and `src/workflow.py` editor tabs. **Ctrl+F:** stay on `"estimation_months": 60`.

“I’ll trace how saved prices become portfolio weights, rule checks, and a committee decision.”

**SHOW:** Stay on the file tabs. Point to your saved locked record tab. **Ctrl+F after opening that record later:** `Student AI-off prediction`.

“I chose the research inputs, questioned the result, and committed a prediction before the locked test.”

## Inputs — `config/mandate.json`, `src/data.py`

**SHOW:** In `config/mandate.json`, **Ctrl+F:** `"estimation_months": 60`; then `"cpi_assumption": 0.025`; then `"real_return_objective": 0.03`. **CLICK:** `src/data.py`; **Ctrl+F:** `def monthly_returns`, then `pct_change(fill_method=None)`. Point to the missing-month handling.

“The baseline uses 60 monthly returns through September 2026. The illustrative 2.5% CPI input plus Cedar's 3% real objective gives a 5.50% screening hurdle. That input differs from the historical CPI signal. The data loader does not invent missing prices.”

## Calculation — `src/engine.py`

**CLICK:** `src/engine.py`. **Ctrl+F:** `def metrics`, then `def optimize`, then `def rules`. At `def rules`, point to `BIL reserve floor`, `Illustrative return hurdle`, and `Numeric volatility cap`.

“The optimizer looks for the lowest-volatility mix that reaches the return hurdle. The weights must total 100%, stay within the fund limits, and meet the effective BIL floor. The `rules` function checks the proposed weights again. That second check matters: I want to see which rules actually passed, not rely on a solver success message.”

**SHOW:** Open `outputs/results.json` or the app's Portfolio comparison tab. In the JSON, **Ctrl+F:** `"Constrained"`; point to the BIL/VT weights and 5.50% estimate. If using the app, point to the Constrained research candidate row.

“BIL's estimated return is about 3.59% and VT's about 11.90%. The 77.04% BIL / 22.96% VT mix reaches 5.50%. I questioned whether that was enough: there is no return cushion for actual costs or weaker VT performance.”

## Signal and decision — `src/signal.py`, `src/workflow.py`

**CLICK:** `src/signal.py`; **Ctrl+F:** `def evaluate_signal`, then `last.value/prior.iloc[0]-1`, then `def effective_reserve`. **CLICK:** `src/workflow.py`; **Ctrl+F:** `def stop_decision`, then `Cedar numeric risk limit not documented`, then `new_process_allocation_range`. You already showed `rules` in `src/engine.py`. Show the app's Executive dashboard statuses after the locked record.

“The stored CPI calculation is about 3.72% year over year. I checked the reported values and arithmetic, but that does not approve Codex's proposed reserve rule. It lifts the effective BIL floor from 3% to 5%; the candidate already holds 77% BIL. The `rules` function we just saw checks the proposed weights against what the app can measure. The baseline passes those testable rules. Here in `stop_decision`, Cedar's approved risk limit, BIL reserve treatment, and actual holdings and trading costs are still unresolved. The full mandate is Not Known, authorization fails, and the recommendation is 0% new capital.”

## Test — locked record and saved JSON

**CLICK:** `docs/changed-input-record.md`; **Ctrl+F:** `Student AI-off prediction`, then `Prediction commit hash`, then `After: BIL`. **CLICK:** `outputs/locked_changed_input.json`; **Ctrl+F:** `"changed": 0.85`, then `"after":`, then `"success": false`. Point to the infeasible result.

“Before the run, I predicted an 85% BIL floor would make 5.50% infeasible. Even 85% BIL and 15% VT estimated only 4.84%. The saved run found no feasible portfolio and no after-run volatility. I kept 0% new capital. This tested the analytical floor; it did not change Cedar's reserve policy.”

## Limit — dashboard

**CLICK:** Return to `config/mandate.json`; **Ctrl+F:** `"risk_limit": null`, then `"current_weights": null`. **SWITCH:** Show the app's Executive dashboard. Point to **Full mandate: Not Known**, **Reject deployment**, and **0% new capital**.

“The code cannot supply Cedar's risk limit, holdings, actual trading costs, or approval to count BIL as reserve. I would wait for that evidence and rerun the app with approved inputs.”
