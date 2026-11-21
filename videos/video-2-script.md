# Video 2 — How the app reaches its answer

**Rehearsal notes, not an actual transcript. Maximum 5 minutes.** Webcam on; clear audio. Show the code and a saved test result. Do not claim a fresh personal test unless you run it.

**What this video does:** Trace the displayed decision through code. In your editor, click **`config/mandate.json` → `src/data.py` → `src/engine.py` → `src/signal.py` → `src/workflow.py` → `docs/changed-input-record.md`**. Open `outputs/locked_changed_input.json` for the saved result. End on the running app's Executive dashboard. Put the files in easy-to-read editor tabs before recording.

**Before recording:** Open the project folder in VS Code. Open the named files as editor tabs, enlarge the text, and open a terminal. If you want the live app for your ending, run `.venv\Scripts\python.exe -m streamlit run app.py` and open the printed Local URL. Turn on webcam and microphone.

**Show on screen:** In `config/mandate.json`, point to `estimation_months: 60`, `cpi_assumption: 0.025`, `real_return_objective: 0.03`, and missing `risk_limit`/`current_weights`. In `src/data.py`, show where saved prices become monthly returns. In `src/engine.py`, show the `metrics`, `rules`, and `optimize` functions. In `src/signal.py`, show the CPI calculation/effective reserve rule. In `src/workflow.py`, show `stop_decision` and `run`. In the locked record and JSON, show the 85% prediction and infeasible result. Finish with the app's Not Known mandate and Reject decision. You do not need to read code line by line.

## Opening — project files

“OpenAI Codex helped with the complicated code, automated tests, and drafting. I used those tools to examine the results, challenge the assumptions, and make my own investment decision. I am responsible for reviewing the analysis and final decision. This is educational work, not investment advice.”

“I want to show how one number becomes a recommendation. The app estimates returns from saved fund prices, solves for weights, checks rules, and then asks whether Cedar has actually authorized deployment.”

“My contribution was choosing the research inputs I wanted to keep, questioning whether the output answered Cedar's real decision, and recording a prediction before the locked test. I want to show the calculation so I can defend the result rather than just read a number from the dashboard.”

## Inputs — `config/mandate.json`, `src/data.py`

“The baseline uses 60 monthly returns through September 2026. The 2.5% CPI input is an illustration. Add Cedar's 3% real-return objective and the screening hurdle is 5.50%. This is separate from the historical CPI signal. The data loader uses saved adjusted prices and does not fill missing months with invented prices.”

## Calculation — `src/engine.py`

“The code annualizes monthly average returns and the sample covariance. Portfolio return is the weighted average of the fund return estimates. Portfolio variance uses the weights and covariance matrix. The optimizer seeks the lowest variance while requiring weights to total 100%, stay in bounds, hold the effective BIL floor, and meet the return screen. Then the rules function checks the result again. A solver message by itself is not investment approval.”

“BIL's annualized historical mean is about 3.59% and VT's is about 11.90%. The selected 77.04% BIL / 22.96% VT mix reaches about 5.50%. This explains the math behind the weight choice. I second-guessed the AI-assisted conclusion that meeting that screen was enough: the estimate has no return cushion for costs or a weaker VT return.”

## Signal and decision — `src/signal.py`, `src/workflow.py`

“The stored CPI calculation is about 3.72% year over year. I reported checking the source values and arithmetic, but that does not prove the AI-proposed reserve rule is a good policy. Under that rule, the effective BIL floor rises from 3% to 5%. Since the candidate already has 77% BIL, the rule does not change its weights here. The workflow keeps unknown client evidence separate from failed numerical checks. This candidate passes testable constraints, but its full mandate is Not Known and authorization fails. That is why the app recommends no new capital.”

## Test — locked record and saved JSON

“I predicted that an 85% BIL floor would prevent the solver from reaching 5.50%. Before running it, I reasoned that even 85% BIL and 15% VT would estimate only about 4.84%. The saved run returned no feasible portfolio, so there is no after-run volatility to compare. My recommendation remained 0%. This is a scenario test of the analytical floor, not a change to Cedar's actual reserve.”

## Limit — dashboard

“The code cannot supply Cedar's approved volatility limit, current holdings, actual transaction costs, or permission to count BIL as the reserve. Those inputs decide whether a mathematically feasible candidate is appropriate for Cedar. My committee decision is to wait for that evidence and rerun the app under approved assumptions.”
