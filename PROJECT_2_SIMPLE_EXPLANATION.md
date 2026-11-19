# Project 2 in plain English

OpenAI Codex helped draft this explanation and test the code. You must review the investment judgment and explain it in your own words. This is coursework, not investment advice.

## The question

Cedar Scholarship Foundation has $20 million, pays $150,000 in scholarships each quarter, and wants to earn CPI plus 3% after costs over rolling five-year periods. The app asks whether a proposed four-fund portfolio process is ready for Cedar to use. The answer in the **draft** is **reject deployment for now**. That means 0% new money into this process until missing evidence is resolved; it does not mean selling existing holdings.

## What goes into the model

The funds are BIL (short Treasury bills), IEF (intermediate Treasuries), LQD (investment-grade corporate bonds), and VT (global stocks). The frozen decision date is November 2, 2026. The price history ends September 30, 2026. Sixty monthly returns are used in the default run. The comparison portfolio is 60% VT and 40% LQD, inherited from Lab 14; Cedar's approval of it is unknown.

For each fund, monthly return is `adjusted price this month / adjusted price last month - 1`. Estimated annual arithmetic return is `12 × average monthly return`. Annual covariance is `12 × sample monthly covariance`. Portfolio return is `sum(weight × fund return)`. Portfolio volatility is `sqrt(weights' × annual covariance × weights)`. These are historical estimates, not forecasts or a proof of the rolling five-year real objective.

The 2.5% CPI input is an illustration. Adding Cedar's 3% real target gives a 5.5% *illustrative arithmetic* return hurdle. The exact one-year compounded nominal equivalent would be `(1.025 × 1.03) - 1 = 5.575%`; neither number proves a future after-cost outcome. Actual costs and current holdings are unknown.

## The three portfolios

| Choice | How weights are set | Estimated return | Volatility | Main finding |
| --- | --- | ---: | ---: | --- |
| Equal weight | 25% in each fund | 3.22% | 7.50% | Misses illustrative hurdle |
| Inverse volatility | More weight in historically less volatile funds | 3.33% | 1.40% | Misses illustrative hurdle |
| Constrained minimum variance | Lowest estimated variance subject to the model's testable rules | 5.50% | 3.53% | Numerical rules pass; full mandate is Not Known |

The constrained research weights are about **77.04% BIL and 22.96% VT**. The 60% VT / 40% LQD comparator estimates 6.81% return and 12.29% volatility, but has no BIL reserve. A higher estimated return by itself does not settle mandate compliance.

## Why the app still says no

The optimizer finds a mathematical allocation. Cedar has not documented a numerical risk limit, approval of BIL as the reserve asset, its actual holdings and trade costs, or approval of the comparison benchmark. The model cannot turn those unknowns into a pass. The authorization gate therefore fails even though the constrained portfolio passes the rules that can be measured. **Your judgment to confirm:** whether rejecting deployment is the right committee decision given these gaps.

## What changes when inputs change

The app recalculates when a sidebar control changes. In an already executed ordinary stress, using 36 months instead of 60 moved the constrained allocation to **92.86% BIL and 7.14% VT**; the largest weight change was **15.82 percentage points**. A 70% maximum fund weight produced **70.00% BIL, 4.27% IEF, and 25.73% VT**. Lowering VT's assumed return by one percentage point produced **73.90% BIL and 26.10% VT**. These are scenario results, not the required student-only AI-off prediction exercise.

The proposed point-in-time CPI signal uses the November 1 ALFRED vintage, before the November 2 decision. September 2026 CPI of 336.298 divided by September 2025 CPI of 324.245 minus one is about 3.72%. The proposed rule raises the analytical BIL floor from 3% to 5% when inflation exceeds 3%. It does not change the default weights because BIL is already above 5%. The fallback policy and three source values still need your personal review.

## How to explain the decision in a video

“I compared two simple baselines with a constrained minimum-variance portfolio. The constrained research portfolio estimates 5.50% return and 3.53% volatility, but the estimate is based on historical prices and illustrative inflation and costs. I cannot certify Cedar's full mandate because the risk limit, reserve approval, and actual trading evidence are missing. My draft recommendation is no new allocation to this process until those facts are documented and the model still works under stress.” Review and adapt that wording yourself before recording.

For the exact source trail, calculations, and limitations, see [the results](docs/checkout-results.md), [methodology](docs/methodology.md), [signal data card](docs/signal-data-card.md), and [decision memo](docs/decision-memo.md).
