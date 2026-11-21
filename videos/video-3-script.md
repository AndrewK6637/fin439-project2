# Video 3 — Committee recommendation

**Rehearsal notes, not an actual transcript. Maximum 5 minutes.** Start the recording with the **live app already open** on Executive dashboard. Webcam on; clear audio.

**What this video does:** Give the committee a decision it can evaluate. In the live Streamlit app, click **Executive dashboard → Portfolio comparison → Point-in-time signal → Stress testing → Committee recommendation**. Point to the figures as you discuss them. Do not change sidebar inputs; this presentation uses the frozen default scenario. You may open the separate locked record after Stress testing if time allows.

**Before recording:** In the project folder terminal run `.venv\Scripts\python.exe -m streamlit run app.py`. Open the Local URL printed by Streamlit (usually `http://localhost:8501`). Wait until Executive dashboard is fully loaded and leave that tab visible before pressing Record. Turn on webcam and microphone. Keep the default 60-month and 2.5% illustrative CPI inputs.

**Show on screen:** On Executive dashboard, point to Reject deployment, 0% new capital, 77.04% BIL / 22.96% VT, 5.50% return, 3.53% volatility, and Full mandate Not Known. On Portfolio comparison, show why equal weight and inverse volatility miss the 5.50% hurdle. On Point-in-time signal, distinguish the 2.5% illustrative CPI input from the 3.72% historical reading and show the 3%-to-5% floor change. On Stress testing, point to the 36-month weight shift and explain that the 0.52% trading cost is for a separate hypothetical trade. On Committee recommendation, state what Cedar must verify before a small pilot could be considered.

## Opening — executive dashboard, visible from first frame

**SHOW:** Start recording with Executive dashboard already loaded. Point to Reject deployment and 0% new capital.

“OpenAI Codex helped with the complicated coding, source recovery, tests, and drafting. I used that work to analyze the numbers, question the model, and reach my own committee recommendation. I am responsible for reviewing the analysis and final decision. This is educational work, not investment advice.”

**SHOW:** Stay on the decision banner; point to the sentence about leaving existing holdings in place.

“My recommendation is to reject deployment for now: put 0% of new capital into this proposed strategy and leave Cedar's existing holdings alone. I would keep the app and the portfolio for research.”

## Candidate — dashboard and comparison tab

**SHOW:** Point to the candidate weights, 5.50% annual return, 3.53% volatility, and Full mandate Not Known. Then **CLICK** Portfolio comparison and point to the equal-weight and inverse-volatility rows.

“Cedar pays $150,000 in scholarships each quarter from a $20 million foundation. The app's candidate is 77.04% BIL and 22.96% VT, with an estimated 5.50% annual return and 3.53% annual volatility. The equal-weight and inverse-volatility alternatives miss the 5.50% illustrative return screen. This candidate passes the rules the app can measure, but the full mandate is Not Known and deployment authorization fails.”

**SHOW:** Keep Portfolio comparison visible. Point to the constrained candidate's 5.50% return and its rule status.

“This is where I question the AI-assisted result. The optimizer was asked to meet 5.50%, and it landed exactly there. A Pass tells me the math worked under the assumptions; it does not give Cedar a return cushion. A real transition cost or a lower future VT return could put it below the screen. The historical estimate also does not prove Cedar's rolling five-year CPI-plus-3% goal after costs.”

**SHOW:** Point to the candidate again; no new click is needed.

“I chose to hold off because I would have to defend an actual allocation of scholarship money, not just a clean calculation. The app helps me identify a candidate and expose missing evidence; it cannot decide Cedar's tolerance for risk.”

## Signal — point-in-time tab

**CLICK:** Point-in-time signal. Point first to the 2.5% illustrative CPI input in the sidebar, then to the 3.72% historical CPI reading and the effective 5% BIL floor.

“The 2.5% CPI assumption in the sidebar sets the illustrative hurdle. Separately, the historical CPI reading is about 3.72% year over year. I reported checking its source values and calculation. A proposed rule lifts the BIL floor from 3% to 5%, but 77% BIL already exceeds that. I would not claim this rule improves returns without testing it against a version without the rule.”

## Sensitivity — stress tab

**CLICK:** Stress testing. Point to the Last 36 monthly observations row (92.86% BIL / 7.14% VT), then the trading-cost explanation. If time permits, switch to the saved locked record for the 85% BIL result.

“Using 36 months instead of 60 changes the allocation to about 92.86% BIL and 7.14% VT. That makes me cautious about treating one optimized weight as stable. The 50-basis-point cost stress leaves the target almost unchanged because it assumes the target is already held. Its separate 0.52% cost belongs to a hypothetical trade, not Cedar's actual transition. In my locked test, an 85% BIL floor made the 5.50% hurdle infeasible. That shows the reserve-return trade-off, not a new Cedar policy.”

## Action — recommendation tab

**CLICK:** Committee recommendation. Point to the missing risk limit, reserve approval, holdings/costs, and the 0% new-capital action.

“The biggest missing item for my judgment is Cedar's approved volatility limit. I cannot say 3.53% is appropriate just because it sounds low. Cedar also needs to confirm whether BIL counts as reserve coverage and provide current holdings and costs. Those determine scholarship liquidity, turnover, and whether this result survives implementation. With those facts, I would rerun the model and consider a small pilot only if it stays within approved risk and clears the return hurdle after costs. Until then, my recommendation is 0% new capital.”
