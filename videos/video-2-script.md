# Video 2 — How the app reaches its answer

**Rehearsal guide, not an actual transcript. Maximum 5 minutes.** Webcam on; clear audio. The bold directions are actions, not words to read aloud. Do not claim a fresh personal test unless you run it.

**Before recording:** Open the repository in VS Code. Put `config/mandate.json`, `src/data.py`, `src/engine.py`, `outputs/results.json`, `src/signal.py`, `src/workflow.py`, `docs/changed-input-record.md`, and `outputs/locked_changed_input.json` in editor tabs, in that order. Enlarge the text. Start the live app using the [README](../README.md) and leave its Executive dashboard ready for the ending. Begin recording with `config/mandate.json` already on screen. Press Esc after each Ctrl+F search so the code remains easy to point to.

## 1. Start on Cedar's inputs

**SHOW:** `config/mandate.json` from the first frame. **SAY:** “This is Cedar's mandate file. It tells the app which research assumptions to use. OpenAI Codex helped with the complicated code, automated tests, and drafting. I used that work to question the numbers and make my own investment decision. I am responsible for the final recommendation. This is educational work, not investment advice.”

**Ctrl+F in `config/mandate.json`:** `"estimation_months": 60`. **SAY:** “The baseline uses 60 monthly returns through September 2026. The illustrative 2.5% CPI assumption plus Cedar's 3% real-return objective gives a 5.50% screening hurdle. That CPI assumption is separate from the historical signal I will show later.” Point to the nearby CPI and real-objective entries without another search.

**CLICK:** `src/data.py`. **Ctrl+F:** `def monthly_returns`. **SAY:** “Here, saved adjusted prices become monthly returns. The code drops incomplete observations instead of making up missing prices. Those returns supply the portfolio estimates.”

## 2. Show the optimizer and check its answer

**CLICK:** `src/engine.py`. **Ctrl+F:** `def optimize`. **SAY:** “The optimizer looks for the lowest-volatility mix that reaches the return hurdle. It must keep the weights within bounds and hold the effective BIL floor.”

**Ctrl+F in the same file:** `def rules`. **SAY:** “This is my concrete check on the proposed weights. The code checks that they add to 100%, meet the BIL floor and return hurdle, and meet a volatility cap if Cedar supplies one. I want to see which rules passed, not rely only on a solver success message.” Point to the nearby rule names; do not search again.

**CLICK:** `outputs/results.json`. **Ctrl+F:** `"Constrained"`. **SAY:** “The baseline candidate is 77.04% BIL and 22.96% VT. Its estimated return is 5.50% and volatility is 3.53%. BIL's estimated return is about 3.59%, while VT's is about 11.90%. The mix needs some VT to reach the hurdle. I questioned whether a result that lands right on the hurdle leaves enough room for real costs or weaker stock returns.”

## 3. Separate the CPI calculation from approval

**CLICK:** `src/signal.py`. **Ctrl+F:** `last.value/prior.iloc[0]-1`. **SAY:** “This calculation compares September 2026 CPI with September 2025 CPI. I checked the reported source values and got about 3.72% year over year. That supports the displayed reading.”

**Ctrl+F in the same file:** `def effective_reserve`. **SAY:** “Codex proposed using that reading to raise the analytical BIL floor from 3% to 5%. Cedar has not approved this rule. The baseline already holds 77% BIL, so the proposed floor does not change its weights.”

**CLICK:** `src/workflow.py`. **Ctrl+F:** `def stop_decision`. **SAY:** “The baseline passes the rules the app can test. This decision step also checks what the app cannot establish: Cedar's risk limit, approval to count BIL as reserve, and actual holdings and trading costs. With those items unresolved, the full mandate is Not Known, deployment is rejected, and new capital stays at 0%.” Point to the nearby `unknown` and `recommendation` lines without another search.

## 4. Show the prediction, result, and committee action

**CLICK:** `docs/changed-input-record.md`. **Ctrl+F:** `Student AI-off prediction`. **SAY:** “Before the locked run, I predicted that an 85% BIL floor would make the 5.50% target infeasible. Even 85% BIL and 15% VT estimated only about 4.84%. I committed the prediction before running the test.” Point to the commit link nearby.

**CLICK:** `outputs/locked_changed_input.json`. **Ctrl+F:** `"success": false` in the `"after"` section. **SAY:** “The saved run found no feasible portfolio, so it produced no after-run volatility. My recommendation stayed at 0% new capital. This tested the analytical floor; it did not change Cedar's real reserve policy.”

**CLICK:** Back to `config/mandate.json`. **Ctrl+F:** `"risk_limit": null`. Point to the nearby `current_weights: null` entry. **SAY:** “The code cannot supply Cedar's approved risk limit or current holdings. I would get that evidence, confirm reserve treatment and trading costs, then rerun the app under approved assumptions.”

**SWITCH:** Live app, Executive dashboard. Point to **Full mandate: Not Known**, **Reject deployment**, and **0% new capital**. **SAY:** “That is why I would keep this app for research and hold off on investing Cedar's money.”
