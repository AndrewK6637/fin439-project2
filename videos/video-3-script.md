# Video 3 — Committee recommendation

**Rehearsal notes, not an actual transcript. Maximum 5 minutes.** Start the recording with the **live app already open** on Executive dashboard. Webcam on; clear audio.

**What this video does:** Present your decision to the committee, explain what the app is useful for today, and name the evidence needed before Cedar could invest. In the live Streamlit app, click **Executive dashboard → Portfolio comparison → Point-in-time signal → Stress testing → Committee recommendation**. Do not change sidebar inputs. Videos 1 and 2 cover the detailed checks and code; keep this one focused on your judgment.

**Before recording:** In the project folder terminal run `.venv\Scripts\python.exe -m streamlit run app.py`. Open the Local URL printed by Streamlit (usually `http://localhost:8501`). Wait until Executive dashboard is fully loaded and leave that tab visible before pressing Record. Turn on webcam and microphone. Keep the default 60-month and 2.5% illustrative CPI inputs.

**How to use this guide:** Read only the words in quotation marks. Follow each bold **POINT**, **CLICK**, or **SWITCH** cue as it appears beside the sentence you are saying. Keep the sidebar at its default inputs throughout.

## Opening — executive dashboard, visible from first frame

**POINT:** On the already loaded Executive dashboard, show the **Reject deployment** banner and **0% new capital**. **SAY:** “Here is my committee decision. Codex helped with coding, tests, and drafting. I questioned the investment case and made the recommendation myself. This is educational work, not investment advice.”

**POINT:** Stay on the banner and show the sentence about existing holdings. **SAY:** “I recommend 0% of new capital and no change to Cedar's existing holdings. I would keep the app for research, but I would not use it to invest Cedar's money today.”

**POINT:** Cedar's **$20 million** foundation size and **$150,000 quarterly scholarships** on the dashboard. **SAY:** “My decision starts with what this money is for. Four scholarship payments total $600,000 a year. An attractive estimated return does not tell me which assets will fund each payment. Before investing, I would ask Cedar for a payment schedule and an approved reserve plan.”

## Candidate — dashboard and comparison tab

**POINT:** On Executive dashboard, show the candidate weights, estimated return, and the three statuses: **testable constraints**, **full mandate**, and **deployment authorization**. **SAY:** “The candidate is about 77% BIL and 23% VT. Its 5.50% estimated return just reaches the hurdle before actual transition costs. I would not present it as a trade ticket. This dashboard separates a numerical pass from a verified mandate and permission to deploy. Those are different committee questions.”

**CLICK:** **Portfolio comparison**. **POINT:** Equal weight, inverse volatility, and constrained candidate rows. **SAY:** “Equal weight and inverse volatility miss the return screen. The constrained candidate reaches it by adding VT. I would not choose a row just for its estimated return; Cedar needs scholarship liquidity and approved risk limits.”

**POINT:** The BIL, IEF, LQD, and VT columns in the allocation chart. **SAY:** “I kept these four funds from earlier coursework. The solver gives IEF and LQD zero weight in this sample. I would not tell Cedar those funds are worthless; this estimation window simply did not favor them.”

**POINT:** The large **BIL** weight in the allocation chart. **SAY:** “BIL is my illustrative stand-in for short-term reserves, not cash already set aside for next quarter's scholarships. Even with most of the candidate in BIL, I would need Cedar to say whether fund shares count toward its reserve and how they would be converted into payment cash. That is an operational decision the optimizer cannot make.”

**POINT:** The constrained candidate's **5.50%** return and rule status. **SAY:** “My concern is the thin margin. A small cost or weaker VT return could erase this pass. An annual historical estimate also cannot prove Cedar will meet CPI plus 3% after costs over five-year periods.”

**POINT:** Keep the candidate row visible, then scroll to the **separate holdout diagnostic**. **SAY:** “I would ask someone else to challenge the return estimates before committing scholarship money. The mix relies on VT to reach the hurdle. Weaker future stock returns would change the case. This holdout adds a check, but its prices came from a later-downloaded snapshot. It is not a live, point-in-time trading record.”

## Signal — point-in-time tab

**CLICK:** **Point-in-time signal**. **POINT:** The **3.72% historical CPI** reading and **5% effective BIL floor**. **SAY:** “Video 1 covered my CPI check. I kept Codex's proposed series as a disclosed research fallback. Checking its arithmetic supported the number, but did not prove the policy is useful. Cedar has not approved it, and the baseline does not show it helped because BIL already exceeds 5%. I would compare results over the same dates with the rule turned off.”

## Sensitivity — stress tab

**CLICK:** **Stress testing**. **POINT:** The **Last 36 monthly observations** row, especially **92.86% BIL / 7.14% VT**. **SAY:** “A shorter estimation window moves the mix to about 93% BIL and 7% VT. I would test whether the strategy remains acceptable across reasonable windows, rather than pick the answer I like best.”

**POINT:** The **Trading cost 50 bps per side** row and its explanation. **SAY:** “This example assumes the target is already held; the separate 0.52% comes from a hypothetical trade. Neither gives Cedar's actual transition cost. Without holdings and a cost schedule, I cannot check the 20% turnover limit or after-cost return.”

## Action — recommendation tab

**CLICK:** **Committee recommendation**. **POINT:** The unresolved risk limit in the recommendation/memo. **SAY:** “My first question to Cedar is its approved volatility limit. I cannot call 3.53% acceptable without that boundary, especially with quarterly scholarships. That is why I chose 0% instead of treating the solver's Pass as approval. If Cedar's limit is below 3.53%, this candidate fails its risk test. Even if the limit is higher, I would still check the reserve and costs before a pilot. I would not change Cedar's risk boundary just to make this portfolio pass.”

**POINT:** The **0% new-capital** decision again. **SAY:** “I considered whether a small allocation now would be a compromise. I do not think it solves the problem. Even a small trade needs approved risk and reserve policies and an implementation plan. Zero percent is my decision about authorization today, not a claim that BIL and VT can never be useful.”

**POINT:** The reserve, holdings, and cost discussion. **SAY:** “I would also ask whether BIL counts toward the $600,000 reserve, how Cedar will fund payments, and what it currently owns. Those answers determine liquidity, turnover, and costs.” **POINT:** The committee ask and monitoring list. **SAY:** “Then I would rerun the app and check proposed trades against Cedar's actual holdings. If the candidate meets approved limits and an after-cost hurdle, I would bring a small pilot back for a vote. During a pilot, I would monitor reserve coverage and whether the allocation stays stable. If the strategy misses the agreed hurdle or breaks an approved limit, I would return to the committee and revise the strategy rather than quietly lower Cedar's objective. For now, the decision is 0%.”
