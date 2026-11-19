# Cedar: investment results for the studio

**AI-assisted output; student selected the analytical design and selected the hold on deployment. A three-value CPI source check was student-reported on November 19, 2026; final review remains pending. Educational work, not investment advice.**

## Decision first

Reject deployment of Cedar's proposed portfolio process; reconsider only after the committee documents the missing mandate approvals and actual holdings/costs, the student validates the signal and completes the genuine locked record, and a rerun shows feasible allocations with acceptable stress results.

The proposed allocation to this unapproved process is **0%-0%**: the committee memo recommends committing no *new* money to this strategy until the missing evidence is reviewed. The model still calculates the research portfolio shown below. This does not direct liquidation of existing assets or certify missing client approvals. The full project is published at [AndrewK6637/fin439-project2](https://github.com/AndrewK6637/fin439-project2).

## Evidence boundary

Frozen research decision: **2026-11-02**. Monthly adjusted prices end **2026-09-30**. The baseline estimates use **60 monthly returns**, starting 2021-10-31. CPI assumption: **2.50%**; real-return spread: **3.00%**; illustrative additive hurdle: **5.50%**. Additional annual costs: **0 bps**, an unconfirmed illustration; actual turnover and transaction costs remain unknown. One basis point is 0.01 percentage point.

## Baseline results

All weights are percent of portfolio; return estimates and volatility are annualized percentages. Estimates are historical arithmetic summaries, not guaranteed future returns.

| Portfolio | BIL | IEF | LQD | VT | Annual mean estimate | Annual volatility | Mandate | Authorization gate | Mean vs benchmark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Equal weight | 25.00% | 25.00% | 25.00% | 25.00% | 3.22% | 7.50% | Fail | Fail | -3.59 pp |
| Inverse volatility | 86.81% | 5.75% | 4.49% | 2.95% | 3.33% | 1.40% | Fail | Fail | -3.48 pp |
| Constrained | 77.04% | 0.00% | 0.00% | 22.96% | 5.50% | 3.53% | Not Known | Fail | -1.31 pp |

Benchmark: 60% VT / 40% LQD; annual mean estimate **6.81%**, volatility **12.29%**. The student selected it as a comparison benchmark; Cedar approval is not documented. It is not a compliant reserve portfolio.

## Mandate and verdict

Cedar has $20 million, a ten-year horizon and $150,000 quarterly scholarships. The goal is CPI+3% after costs over rolling five years. The student chose to keep BIL/IEF/LQD/VT as the coursework fund universe and BIL as an illustrative reserve stand-in. The model is long only and fully invested. Reserve: $600,000 (3% at inception), 95% five-day liquidity, 5% nonexempt direct issuer maximum, annual rebalance and 20% annual one-way turnover cap. Cedar approval of the BIL proxy and a numeric risk-policy limit remain unresolved.

| Constrained candidate rule | Result |
| --- | --- |
| Weights sum to 100% | Pass |
| Long only | Pass |
| Position bounds | Pass |
| BIL reserve floor | Pass |
| Liquidity >= mandate minimum (course fund classification) | Pass |
| Direct nonexempt issuer <=5% (all allowed funds exempt) | Pass |
| Illustrative return hurdle | Pass |
| Numeric volatility cap | Not Known |
| Single-rebalance turnover approximation <=20% | Not Known |
| Actual annual turnover <=20% (trade ledger required) | Not Known |
| BIL reserve proxy approved | Not Known |
| Realized rolling-five-year CPI+3% after costs | Not Known |

**Not Known means the required evidence is missing, not that a calculation failed.** The numeric volatility limit was not recovered; actual holdings and trades are unavailable for turnover; BIL has not been approved as the reserve proxy; and a historical arithmetic return estimate cannot prove a realized rolling-five-year CPI+3% result after costs. The approval gate stays closed until those items are resolved.

## Existing ordinary stress evidence (not a classroom prediction record)

| Scenario | Solver | Weights BIL / IEF / LQD / VT | Annual mean estimate | Annual volatility | Largest weight change |
| --- | --- | --- | --- | --- | --- |
| VT return estimate minus 1 percentage point | Pass | 73.90% / 0.00% / 0.00% / 26.10% | 5.50% | 3.99% | 3.14 percentage points |
| Last 36 monthly observations | Pass | 92.86% / 0.00% / 0.00% / 7.14% | 5.50% | 0.89% | 15.82 percentage points |
| Trading cost 50 bps per side | Pass | 77.04% / 0.00% / 0.00% / 22.96% | 5.50% | 3.53% | 0.00 percentage points |
| Maximum fund weight 70% | Pass | 70.00% / 4.27% / 0.00% / 25.73% | 5.50% | 4.14% | 7.04 percentage points |

The cost stress uses hypothetical starting weights equal to the baseline candidate. Its near-zero trading cost does not establish actual client costs. Changing the estimation window alters the displayed research allocation; the unresolved approval evidence still prevents deployment. A no-change decision must be explained, not forced to flip.

## Monitor and reversal condition

Monitor reserve coverage, price age, signal vintage, feasibility, real after-cost outcomes and turnover. Stop for invalid data, infeasibility, a failed required stress or more than 20 percentage points of allocation instability. Reject deployment of Cedar's proposed portfolio process; reconsider only after the committee documents the missing mandate approvals and actual holdings/costs, the student validates the signal and completes the genuine locked record, and a rerun shows feasible allocations with acceptable stress results.

The present controls cannot certify missing client approvals or actual annual ledger evidence. Reversal requires documented human review and verified evidence; a favorable scenario alone is insufficient.

## Reproduction and unfinished evidence

From the project folder in PowerShell, run `.\.venv\Scripts\python.exe scripts\build_checkout_results.py` to regenerate this baseline page from the same pipeline as the app. This command does **not** run either changed-input experiment. See [the machine-readable results](../outputs/results.json), [decision memo](decision-memo.md), [validation](tuesday-checkout-validation.md), and [blank partner record](partner-cold-run-template.md). The partner record, genuine student AI-off prediction, and classroom before/after evidence remain incomplete; the student-reported CPI spot check awaits independent review. See [assumptions and next steps](student-assumptions-and-actions.md).
