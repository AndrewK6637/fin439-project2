# Video 3 — Committee recommendation

**Rehearsal notes, not an actual transcript. Maximum 5 minutes.** Start the recording with the **live app already open** on Executive dashboard. Webcam on; clear audio.

**What this video does:** Give the committee a decision it can evaluate. In the live Streamlit app, click **Executive dashboard → Portfolio comparison → Point-in-time signal → Stress testing → Committee recommendation**. Point to the figures as you discuss them. Do not change sidebar inputs; this presentation uses the frozen default scenario. You may open the separate locked record after Stress testing if time allows.

**Before recording:** In the project folder terminal run `.venv\Scripts\python.exe -m streamlit run app.py`. Open the Local URL printed by Streamlit (usually `http://localhost:8501`). Wait until Executive dashboard is fully loaded and leave that tab visible before pressing Record. Turn on webcam and microphone. Keep the default 60-month and 2.5% illustrative CPI inputs.

**How to use this guide:** Read only the words in quotation marks. Follow each bold **POINT**, **CLICK**, or **SWITCH** cue as it appears beside the sentence you are saying. Keep the sidebar at its default inputs throughout.

## Opening — executive dashboard, visible from first frame

**POINT:** On the already loaded Executive dashboard, show the **Reject deployment** banner and **0% new capital**. **SAY:** “OpenAI Codex helped with the complicated coding, source recovery, tests, and drafting. I used that work to analyze the numbers, question the model, and reach my own committee recommendation. I am responsible for reviewing the analysis and final decision. This is educational work, not investment advice.”

**POINT:** Stay on the banner and show the sentence about existing holdings. **SAY:** “My recommendation is to reject deployment for now: put 0% of new capital into this proposed strategy and leave Cedar's existing holdings alone. I’d keep the app for research and hold off on using it to invest Cedar’s money.”

## Candidate — dashboard and comparison tab

**POINT:** On Executive dashboard, show the candidate weights, 5.50% estimated return, 3.53% volatility, and **Full mandate: Not Known**. **SAY:** “Cedar pays $150,000 in scholarships each quarter from a $20 million foundation. The app's research candidate is 77.04% BIL and 22.96% VT, with an estimated 5.50% annual return and 3.53% volatility.”

**CLICK:** **Portfolio comparison**. **POINT:** Equal weight, inverse volatility, and the constrained candidate rows. **SAY:** “The equal-weight and inverse-volatility alternatives miss the 5.50% illustrative return screen. The constrained candidate passes the rules the app can measure, but its full mandate is Not Known and deployment authorization fails.”

**POINT:** The constrained candidate's **5.50%** return and rule status. **SAY:** “This is where I question the AI-assisted result. The optimizer was asked to meet 5.50%, and it landed right on that hurdle before Cedar's actual transition costs. A Pass tells me the math worked under these assumptions. Even a small cost or a lower future VT return could put the portfolio below the screen. The historical estimate also does not prove Cedar's rolling five-year CPI-plus-3% goal after costs.”

**POINT:** Keep the candidate row visible. **SAY:** “I chose to hold off because I would have to defend an actual allocation of scholarship money, not just a clean calculation. The app helps me identify a candidate and expose missing evidence; it cannot decide Cedar's tolerance for risk.”

## Signal — point-in-time tab

**CLICK:** **Point-in-time signal**. **POINT:** The sidebar's **2.5% illustrative CPI** input. **SAY:** “The 2.5% CPI assumption sets the illustrative return hurdle.” **POINT:** The tab's **3.72% historical CPI** reading and **5% effective BIL floor**. **SAY:** “Separately, the historical CPI reading is about 3.72% year over year. I reported checking its source values and calculation. A proposed rule lifts the BIL floor from 3% to 5%, but 77% BIL already exceeds that. I would not claim the rule improves returns without comparing it with a version that does not use the rule.”

## Sensitivity — stress tab

**CLICK:** **Stress testing**. **POINT:** The **Last 36 monthly observations** row, especially **92.86% BIL / 7.14% VT**. **SAY:** “Using 36 months instead of 60 changes the allocation to about 92.86% BIL and 7.14% VT. That makes me cautious about treating one optimized weight as stable.”

**POINT:** The **Trading cost 50 bps per side** row and its explanation. **SAY:** “This cost stress leaves the target almost unchanged because it assumes the target is already held. The separate 0.52% cost belongs to a hypothetical trade, not Cedar's actual transition.” **POINT:** The locked-experiment note on the tab; if time permits, **SWITCH** to the [saved locked record](../docs/changed-input-record.md). **SAY:** “In my locked test, an 85% BIL floor made the 5.50% hurdle infeasible. That shows the reserve-return trade-off, not a new Cedar policy.”

## Action — recommendation tab

**CLICK:** **Committee recommendation**. **POINT:** The unresolved risk limit in the recommendation/memo. **SAY:** “The first client decision I would check is Cedar's approved volatility limit. I cannot say 3.53% is acceptable just because it sounds low, especially when the foundation must fund scholarships every quarter.”

**POINT:** The reserve, holdings, and cost discussion. **SAY:** “Cedar also needs to decide whether BIL counts as reserve coverage and provide current holdings and trading costs. Those tell me how scholarships will be funded, how much trading is needed, and whether the portfolio still clears the hurdle after implementation.” **POINT:** The committee ask. **SAY:** “I would rerun the app with those facts and bring back a small pilot only if the result meets Cedar's approved limits. Until then, my recommendation is 0% new capital.”
