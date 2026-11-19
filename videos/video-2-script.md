# Video 2 — How the code reaches the decision

**Aim: about 4 minutes. Maximum: 5 minutes.** Keep your webcam on and audio clear. Open the editor and a terminal before recording. This is a speaking guide, not an actual transcript.

## Opening — show the project files

**Say:** “I used OpenAI Codex to help develop and test this app and draft these speaking notes. I am responsible for the analysis and final decision. This is educational work, not investment advice.”

“I will trace one result from data to the committee decision. The four fund prices feed return estimates; the optimizer proposes weights; then the mandate and authorization checks determine what we can recommend.”

## Inputs — show `config/mandate.json` and `src/data.py`

**Say:** “The saved configuration sets a 60-month estimation window, a 2.5% illustrative CPI assumption, and Cedar’s 3% real-return spread. The screening hurdle is therefore 5.50% nominal. This 2.5% is a scenario input, not the historical CPI signal. The loader uses saved adjusted monthly prices for BIL, IEF, LQD, and VT, checks dates and values, and does not fill missing prices.”

## Calculation — show `src/engine.py`

**Say:** “The app estimates arithmetic annual returns from monthly returns and annualizes the sample covariance. For weights w, expected return is the weighted sum of fund means; variance is w-transpose times the covariance matrix times w. The constrained solver minimizes variance while requiring weights to sum to 100%, remain nonnegative, and meet the illustrative hurdle and reserve floor. It checks the returned weights again against the rules. A solver message alone is not proof of feasibility.”

## Signal and decision — show `src/signal.py`, then `src/workflow.py`

**Say:** “The saved November 1 ALFRED vintage gives 336.298 divided by 324.245 minus one, about 3.72% historical year-over-year CPI. Under the proposed rule, this raises the BIL floor from the entered 3% to an effective 5%. The baseline candidate already holds 77.04% BIL, so that floor does not bind. The workflow then separates testable constraints from unknown mandate evidence. The candidate passes testable rules, but full mandate status is Not Known and deployment authorization fails. That produces 0% new capital.”

## One test — show `docs/changed-input-record.md` and `outputs/locked_changed_input.json`

**Say:** “I wrote and committed a prediction before changing the BIL floor to 85%. I expected no portfolio to meet the 5.50% hurdle. The saved run returned no feasible constrained portfolio; the recommendation stayed at 0% new capital. The output records the prediction commit that the script checked on GitHub. I recorded the actual result in a later commit.”

## Validation and limit — show `tests/test_app.py` or the test command in README

**Say:** “The automated suite passed 66 tests in the latest local check. The holdout is a diagnostic using a later-downloaded adjusted-price snapshot, so I do not call it an implementable point-in-time backtest. The code cannot infer Cedar’s risk policy, current holdings, actual transaction costs, or approval of the BIL reserve proxy. Those are committee inputs, not missing lines of Python.”
