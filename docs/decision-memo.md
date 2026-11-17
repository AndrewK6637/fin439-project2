OpenAI Codex assisted with source recovery, software development, calculations implemented in Python, testing, and drafting this document.

The analysis and final decision are the responsibility of the student; this is educational work, not investment advice. Student review and approval are pending.

# Cedar Scholarship Foundation - Draft Committee Decision

**Recommendation: Reject deployment for now.** Reject deployment pending resolution of the listed failures and unknowns; retain the app for analytical review. The allocation range to this unapproved process is **0%-0% pending evidence clearance**; this is not an instruction to liquidate existing holdings.

## Mandate and evidence boundary

Cedar has $20 million, a ten-year horizon, and quarterly scholarships of $150,000. Its objective is CPI + 3% annually after costs over rolling five-year periods. The recovered universe is BIL, IEF, LQD and VT; the proposed comparator is the inherited 60% VT / 40% LQD mix, whose Cedar-specific approval is not documented. The minimum reserve is $600,000, or 3% at inception; five-day liquidity must cover 95%, direct nonexempt issuers are capped at 5%, and annual one-way turnover is capped at 20% without committee approval.

This frozen research decision is dated 2026-11-02, using monthly adjusted prices ending 2026-09-30 and 60 return observations. The 2.5% CPI assumption and resulting 5.5% nominal hurdle are inherited illustrations, not a confirmed forward CPI forecast. Historical means and sample volatility are estimates, not promises.

## Alternatives and constrained research allocation

| Portfolio | BIL | IEF | LQD | VT | Annual mean estimate | Annual volatility | Mandate | Authorization gate | Mean vs benchmark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Equal weight | 25.00% | 25.00% | 25.00% | 25.00% | 3.22% | 7.50% | Fail | Fail | -3.59 pp |
| Inverse volatility | 86.81% | 5.75% | 4.49% | 2.95% | 3.33% | 1.40% | Fail | Fail | -3.48 pp |
| Constrained | 77.04% | 0.00% | 0.00% | 22.96% | 5.50% | 3.53% | Not Known | Fail | -1.31 pp |

The comparator has an annual mean estimate of 6.81% and volatility of 12.29%, but no BIL reserve. Equal weight and inverse volatility fail the illustrative return hurdle. The constrained candidate passes testable rules, while full compliance stays Not Known because the numeric risk limit, reserve-proxy acceptance and actual turnover evidence are missing. Its allocation is a research result, not an authorized trade.

## Point-in-time signal

The proposed fallback is CPIAUCSL year-over-year inflation: 336.298 / 324.245 - 1 = 3.72%. The observation is 2026-09-01, from the 2026-11-01 ALFRED vintage, the calendar day before the decision. The proposed policy raises the analytical BIL floor to 5.00%. This does not change the baseline optimum because its BIL weight already exceeds that floor. The rule influences feasible construction, but is not represented as a proven return predictor or the student's prior Lab 17 choice.

## Stress evidence

| Scenario | Solver | Weights BIL/IEF/LQD/VT | Annual mean estimate | Volatility | Largest weight move |
| --- | --- | --- | --- | --- | --- |
| VT return estimate minus 1 percentage point | Pass | 73.90% / 0.00% / 0.00% / 26.10% | 5.50% | 3.99% | 3.14 pp |
| Last 36 monthly observations | Pass | 92.86% / 0.00% / 0.00% / 7.14% | 5.50% | 0.89% | 15.82 pp |
| Trading cost 50 bps per side | Pass | 77.04% / 0.00% / 0.00% / 22.96% | 5.50% | 3.53% | 0.00 pp |
| Maximum fund weight 70% | Pass | 70.00% / 4.27% / 0.00% / 25.73% | 5.50% | 4.14% | 7.04 pp |

The shorter window materially changes the allocation. The transaction-cost scenario starts from the baseline candidate as hypothetical holdings; because the optimal target is essentially unchanged, turnover is essentially zero. A separate equal-weight transition calculation demonstrates that nonzero trades do generate costs. This cannot establish the actual client trading costs without holdings and trade records. The ordinary stress tests do not substitute for the unrun Locked Changed-Input Record.

## Risks, monitoring and committee ask

Estimation error, the BIL reserve proxy, the unresolved forward CPI/cost basis, liquidity under stress and absent actual turnover evidence prevent deployment. The separate holdout exercise avoids training on evaluation-period returns, but uses a later downloaded adjusted-price snapshot; it is a diagnostic, not a point-in-time implementable backtest.

Monitor reserve coverage, vintage identity, price age, solver feasibility, costs, annual turnover, real outcomes and weight stability. Stop on an invalid signal, stale prices, infeasible optimization, a failed required stress, or a weight change above the analyst-defined 20-percentage-point stability threshold. That threshold is a disclosed process choice, not a recovered client limit.

The committee should reject deployment until the missing mandate inputs and proposed signal are reviewed, source checks are complete, and the student finishes the genuine AI-off experiment. Revisit the decision only with that evidence; do not relax the objective merely to obtain an allocation. See validation-and-ai-use.md for tests and limitations.

## Final decision line (AI-assisted draft)

Reject deployment of Cedar's proposed portfolio process; reconsider only after the committee documents the missing mandate approvals and actual holdings/costs, the student validates the signal and completes the genuine locked record, and a rerun shows feasible allocations with acceptable stress results.
