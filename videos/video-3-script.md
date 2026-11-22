# Video 3 — Committee recommendation

**Rehearsal notes, not an actual transcript. Maximum 5 minutes.** Start the recording with the **live app already open** on Executive dashboard. Webcam on; clear audio.

**What this video does:** Present your decision to the committee, explain what the app is useful for today, and name the evidence needed before Cedar could invest. In the live Streamlit app, click **Executive dashboard → Portfolio comparison → Point-in-time signal → Stress testing → Committee recommendation**. Do not change sidebar inputs. Videos 1 and 2 cover the detailed checks and code; keep this one focused on your judgment.

**Before recording:** In the project folder terminal run `.venv\Scripts\python.exe -m streamlit run app.py`. Open the Local URL printed by Streamlit (usually `http://localhost:8501`). Wait until Executive dashboard is fully loaded and leave that tab visible before pressing Record. Turn on webcam and microphone. Keep the default 60-month and 2.5% illustrative CPI inputs.

**How to use this guide:** Read only the words in quotation marks. Follow each bold **POINT**, **CLICK**, or **SWITCH** cue as it appears beside the sentence you are saying. Keep the sidebar at its default inputs throughout.

## Opening — executive dashboard, visible from first frame

**POINT:** On the already loaded Executive dashboard, show the **Reject deployment** banner and **0% new capital**. **SAY:** “Here is my committee decision. Codex helped with coding, tests, and drafting. I questioned the investment case and made the recommendation myself. This is educational work, not investment advice.”

**POINT:** Stay on the banner and show the sentence about existing holdings. **SAY:** “I recommend 0% of new capital and no change to Cedar's existing holdings. I would keep the app for research, but I would not use it to invest Cedar's money today.”

## Candidate — dashboard and comparison tab

**POINT:** On Executive dashboard, show the candidate weights, estimated return, and **Full mandate: Not Known**. **SAY:** “The research candidate is about 77% BIL and 23% VT. Its 5.50% estimated return just reaches the hurdle before Cedar's actual transition costs. I would not present it as a trade ticket.”

**CLICK:** **Portfolio comparison**. **POINT:** Equal weight, inverse volatility, and constrained candidate rows. **SAY:** “Equal weight and inverse volatility miss the return screen. The constrained candidate reaches it by adding VT. I would not choose a row just for its estimated return; Cedar needs scholarship liquidity and approved risk limits.”

**POINT:** The constrained candidate's **5.50%** return and rule status. **SAY:** “My concern is the thin margin. A small cost or weaker VT return could erase this pass. An annual historical estimate also cannot prove Cedar will meet CPI plus 3% after costs over five-year periods.”

**POINT:** Keep the candidate row visible. **SAY:** “I can use this row for discussion. I cannot defend committing scholarship money from it yet.”

## Signal — point-in-time tab

**CLICK:** **Point-in-time signal**. **POINT:** The **3.72% historical CPI** reading and **5% effective BIL floor**. **SAY:** “Video 1 covered my CPI check. Cedar has not approved using it to change the reserve rule. This baseline does not show the rule helped because the candidate already exceeds 5% BIL. I would ask Cedar to approve or reject the rule.”

## Sensitivity — stress tab

**CLICK:** **Stress testing**. **POINT:** The **Last 36 monthly observations** row, especially **92.86% BIL / 7.14% VT**. **SAY:** “A shorter estimation window moves the mix to about 93% BIL and 7% VT. I would test whether the strategy remains acceptable across reasonable windows, rather than pick the answer I like best.”

**POINT:** The **Trading cost 50 bps per side** row and its explanation. **SAY:** “This example assumes the target is already held; the separate 0.52% comes from a hypothetical trade. Neither gives Cedar's actual transition cost. Without holdings and a cost schedule, I cannot check the 20% turnover limit or after-cost return.”

## Action — recommendation tab

**CLICK:** **Committee recommendation**. **POINT:** The unresolved risk limit in the recommendation/memo. **SAY:** “My first question to Cedar is its approved volatility limit. I cannot call 3.53% acceptable without that boundary, especially with quarterly scholarships. A numerical pass is not deployment authority.”

**POINT:** The reserve, holdings, and cost discussion. **SAY:** “I would also ask whether BIL counts toward the $600,000 reserve, how Cedar will fund payments, and what it currently owns. Those answers determine liquidity, turnover, and costs.” **POINT:** The committee ask. **SAY:** “Then I would rerun the app. If the candidate meets approved limits and an after-cost hurdle, I would bring a small pilot back for a vote. Otherwise, I would revise the strategy rather than lower Cedar's objective. For now, the decision is 0%.”
