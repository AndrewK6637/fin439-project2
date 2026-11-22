# Video 1 — How my thinking changed

**Rehearsal notes, not an actual transcript. Maximum 3 minutes.** Webcam on; clear audio. Say only what you agree with and can explain.

**What this video does:** Show how your own questions and checks affected the recommendation. Click **Executive dashboard → Portfolio comparison → Point-in-time signal → your saved `docs/changed-input-record.md` in a browser tab → Executive dashboard**. Have both tabs open before recording; do not change inputs during this video.

**Before recording:** Open the project folder `fin439_project2_investment_management`. In its terminal run `.venv\Scripts\python.exe -m streamlit run app.py`, then open the Local URL printed by Streamlit (usually `http://localhost:8501`). Also open `docs/changed-input-record.md` in a separate browser or editor tab. Turn on webcam and microphone.

**Show on screen:** On Executive dashboard, point to Reject deployment, 0% new capital, 77.04% BIL / 22.96% VT, 5.50% return and 3.53% volatility. On Portfolio comparison, point to the two alternatives that miss the hurdle. On Point-in-time signal, point to the 3.72% historical CPI reading and 5% effective floor. In the locked record, point to your prediction, its earlier commit link, and the infeasible result. Return to the dashboard for your final decision.

## Opening — executive dashboard

**SHOW:** Keep Executive dashboard visible. Point to the decision banner and 0% new capital.

“OpenAI Codex helped with the complicated coding, source recovery, testing, and drafting. I used it as a tool so I could examine the financial results and make my own recommendation. I am responsible for reviewing the analysis and final decision.

**SHOW:** Still on Executive dashboard, point to Cedar's objective and scholarship amount.

“Cedar has $20 million, pays $150,000 in scholarships each quarter, and wants CPI plus 3% after costs over five-year periods. My question is whether the app gives a committee enough evidence to invest new money.”

## What I chose — README and comparison tab

**CLICK:** Portfolio comparison. Point to the four fund columns and the comparison portfolios. Briefly switch to the README only if it is already open.

“I kept the four-fund universe from earlier coursework: BIL, IEF, LQD, and VT. I chose to keep a 60% VT / 40% LQD portfolio for comparison and to use BIL as an *illustrative* reserve stand-in. Cedar has not approved those choices. Getting the app to run was only part of the work. Aidan later followed my README on his Mac and reproduced the baseline, but he also saw a blank first load for about one to two minutes.”

**SHOW:** Point to the constrained candidate, then the two alternatives.

“My input was deciding what question the model should answer and whether its answer was strong enough for a committee. I did not treat the portfolio weights as a recommendation just because a solver produced them.”

## One check — signal tab and data card

**CLICK:** Point-in-time signal. Point to the historical CPI value, its two source values, and the effective 5% BIL floor. If the source values are collapsed, open the raw record expander.

“I reported checking three values in the historical CPI file. September 2026 was 336.298 and September 2025 was 324.245. Dividing them and subtracting one gives about 3.72%. That supports the displayed arithmetic. I still questioned the AI-proposed rule: correct CPI math does not show that raising the BIL floor improves this portfolio or that Cedar approved the policy.”

## What I questioned — locked record

**SWITCH TAB:** Open `docs/changed-input-record.md`. Point to the prediction, prediction commit link, and actual infeasible result.

“The model came up with 77.04% BIL and 22.96% VT. The estimated return was 5.50%, which just met the target. That made me question how much confidence I should put in the app’s ‘Pass.’ Even a small trading cost could put the estimated return below the target. I also wanted to see what would happen if Cedar needed a bigger reserve. Before running the test, I committed my prediction that requiring at least 85% in BIL would make the target unreachable. The saved run confirmed it. That showed me how much the result depended on the reserve assumption, and it was one reason I recommended putting 0% of new money into the strategy for now.”

## Close — dashboard

**SWITCH TAB:** Return to Executive dashboard. Point again to Reject deployment and 0% new capital.

“My recommendation remains 0% of new capital and no change to existing holdings. The missing approved risk limit matters most to me: 3.53% estimated volatility may sound low, but I cannot call it acceptable without Cedar's limit. If Cedar confirms its limit, reserve treatment, holdings, and costs, I would rerun the analysis and consider a small pilot only if the result still clears the hurdle after costs.”
