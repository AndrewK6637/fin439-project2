# Visible executed output

As-of: 2026-11-02. Price end: 2026-09-30. Estimates from 2021-10-31. All returns and risks are annualized decimals displayed as percentages.

| Portfolio | BIL | IEF | LQD | VT | Annual mean estimate | Annual volatility | Mandate | Authorization gate | Mean vs benchmark | Failed rules | Unknown rules |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Equal weight | 25.00% | 25.00% | 25.00% | 25.00% | 3.22% | 7.50% | Fail | Fail | -3.59 pp | Illustrative return hurdle | Numeric volatility cap; Single-rebalance turnover approximation <=20%; Actual annual turnover <=20% (trade ledger required); BIL reserve proxy approved; Realized rolling-five-year CPI+3% after costs |
| Inverse volatility | 86.81% | 5.75% | 4.49% | 2.95% | 3.33% | 1.40% | Fail | Fail | -3.48 pp | Illustrative return hurdle | Numeric volatility cap; Single-rebalance turnover approximation <=20%; Actual annual turnover <=20% (trade ledger required); BIL reserve proxy approved; Realized rolling-five-year CPI+3% after costs |
| Constrained | 77.04% | 0.00% | 0.00% | 22.96% | 5.50% | 3.53% | Not Known | Fail | -1.31 pp | None among testable rules | Numeric volatility cap; Single-rebalance turnover approximation <=20%; Actual annual turnover <=20% (trade ledger required); BIL reserve proxy approved; Realized rolling-five-year CPI+3% after costs |

## Stress results

| Scenario | Solver | Weights BIL/IEF/LQD/VT | Annual mean estimate | Volatility | Largest weight move |
| --- | --- | --- | --- | --- | --- |
| VT return estimate minus 1 percentage point | Pass | 73.90% / 0.00% / 0.00% / 26.10% | 5.50% | 3.99% | 3.14 pp |
| Last 36 monthly observations | Pass | 92.86% / 0.00% / 0.00% / 7.14% | 5.50% | 0.89% | 15.82 pp |
| Trading cost 50 bps per side | Pass | 77.04% / 0.00% / 0.00% / 22.96% | 5.50% | 3.53% | 0.00 pp |
| Maximum fund weight 70% | Pass | 70.00% / 4.27% / 0.00% / 25.73% | 5.50% | 4.14% | 7.04 pp |

## Decision

{
  "status": "Not Known",
  "failed": [],
  "unknown": [
    "Cedar numeric risk limit not documented",
    "Actual holdings/trades unavailable; turnover and transition costs unverified",
    "BIL reserve-proxy acceptance not confirmed",
    "CPI fallback selected for coursework and spot-checked by student; Cedar policy approval remains unconfirmed",
    "Cedar benchmark approval not recovered",
    "Forward CPI and cost assumptions not client-confirmed",
    "Realized rolling-five-year real objective is not established by an arithmetic estimate"
  ],
  "recommendation": "Reject",
  "committee_ask": "Reject deployment pending resolution of the listed failures and unknowns; retain the app for analytical review.",
  "new_process_allocation_range": "0%-0% pending evidence clearance"
}

## Chronological holdout (revised snapshot, not PIT backtest)

{
  "label": "Chronological holdout diagnostic using a later downloaded adjusted-price snapshot; NOT a point-in-time implementable backtest. Signal not applied retrospectively.",
  "train_end": "2025-09-30",
  "evaluation_start": "2025-10-31",
  "evaluation_end": "2026-09-30",
  "constrained_solver_status": "Optimization terminated successfully",
  "results": {
    "Equal weight": {
      "weights": [
        0.25,
        0.25,
        0.25,
        0.25
      ],
      "realized_gross_return": 0.030839566901070148,
      "realized_volatility": 0.05114799250109694
    },
    "Inverse volatility": {
      "weights": [
        0.8629741219176711,
        0.05971733178788709,
        0.04575879131004785,
        0.03154975498439412
      ],
      "realized_gross_return": 0.032704246051532104,
      "realized_volatility": 0.008357921190803854
    },
    "Benchmark": {
      "weights": [
        0,
        0,
        0.4,
        0.6
      ],
      "realized_gross_return": 0.08259581228532875,
      "realized_volatility": 0.0918324714673181
    },
    "Constrained": {
      "weights": [
        0.7370606653739014,
        0.0,
        0.0,
        0.2629393346260987
      ],
      "realized_gross_return": 0.07025132147803381,
      "realized_volatility": 0.03504900439154359
    }
  }
}