# Locked Changed-Input Record — Completed

The student-authored prediction was committed before the run at `295aa53dabfd930576c1fbe02043e544ed78ac73`. The saved result records that commit and the remote tip verified at run time. The student recorded the actual results and reconciliation afterward at `e1adc623310bcb013c6b1441c828f2912565ba99`.

| Field | Record |
|---|---|
| Experiment | cedar-reserve-85 |
| Original input | Analytical reserve_min = 0.03 (3% of portfolio); original client reserve rule unchanged |
| Changed input | Analytical reserve_min = 0.85 (85% of portfolio); scenario only, **not** a change to Cedar's actual 3% reserve rule |
| Other inputs | Frozen config/mandate.json, saved price/signal snapshots and current submitted source |
| Student AI-off prediction |I predict that raising the minimum BIL allocation from 3% to 85% will make it impossible for the model to find a portfolio that meets the 5.50% return hurdle. I expect my recommendation to stay at 0% new capital. |
| Reasoning |The original portfolio held about 23% in VT to reach the 5.50% hurdle. With at least 85% in BIL, there's only 15% left for the other funds. VT has the highest estimated return, so I checked what would happen if the full 15% went into VT. That mix would have an estimated annual return of about 4.84%, which is still below 5.50%. That's why I expect the model to say there's no feasible portfolio. |
| Expected output direction |I expect the 85% BIL minimum to make it harder to reach the 5.50% return target. With only 15% left for other funds, I expect the model to find no portfolio that meets both requirements. I expect the 85% BIL / 15% VT test mix to have lower annual volatility than the original 3.53%. The test mix holds less VT and more BIL, so I expect its returns to swing less. |
| Expected decision effect |I expect the recommendation to stay at 0% new capital. If the model cannot meet the return target with the higher reserve, that gives me another reason to hold off. |
| Prediction commit hash and GitHub link |[`295aa53dabfd930576c1fbe02043e544ed78ac73`](https://github.com/AndrewK6637/fin439-project2/commit/295aa53dabfd930576c1fbe02043e544ed78ac73) |
| Actual run timestamp | 2026-11-19T16:49:11.8244233-05:00 (output file last modified) |
| Before: BIL / IEF / LQD / VT weights (%) |77.04% / 0.00% / 0.00% / 22.96% |
| After: BIL / IEF / LQD / VT weights (%) |Unavailable. The solver did not return a feasible portfolio. |
| Before / after annual mean estimate (%) | 5.50% / unavailable |
| Before / after annual volatility (%) |3.53% / unavailable |
| Before / after solver feasibility and mandate status |Before: feasible, mandate Not Known. After: infeasible, mandate Fail. |
| Before / after committee recommendation |Reject deployment and recommend 0% new capital in both runs. |
| Difference from prediction |I expected the 85% floor to produce no feasible portfolio and the recommendation to stay at 0% new capital. Both matched. The solver returned no portfolio at 85%, so the run gave me no volatility estimate to compare with my prediction. |
| Diagnosis and what was learned |At an 85% BIL floor, only 15% was available for the other funds. Even putting that whole 15% into VT gave me a pre-run estimate of about 4.84%, below the 5.50% target. The run confirmed that the model couldn't find a portfolio that met both requirements. |
| Result file and after-run commit link |`outputs/locked_changed_input.json` — [After-run commit](https://github.com/AndrewK6637/fin439-project2/commit/e1adc62) |
