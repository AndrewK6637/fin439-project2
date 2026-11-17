# Six-minute code study guide

Study aid prepared with AI. Explain the code yourself during the partner exercise; do not claim these words are your AI-off classroom response. This guide gives formulas and existing baseline behavior, not a prediction for the reserved annual-cost scenario.

## 0:00-1:00 ? Where data becomes estimates

[`monthly_returns`](../src/data.py#L25) in `src/data.py`, lines 25-32 calculates each simple monthly return as current adjusted price divided by previous price minus one. No forward fill bridges missing observations. [`estimates`](../src/data.py#L34) in `src/data.py`, lines 34-37 calculates the monthly arithmetic mean times 12 and the sample covariance matrix times 12. These are historical estimates, not guaranteed forecasts.

## 1:00-2:00 ? The main investment numbers

[`metrics`](../src/engine.py#L31) in `src/engine.py`, lines 31-42. The line `variance=float(w@cov@w);gross=float(w@mu)` produces portfolio variance and the annual estimated return. `w` is weights in decimals, `mu` is annual mean estimates, and `cov` is annual covariance. The square root of variance is annual volatility. This is the source of the default 5.50% annual mean estimate and 3.53% volatility shown on the dashboard. `ongoing=config['ongoing_cost_bps']/10000` converts basis points to an annual decimal cost. The returned `net_return_before_trade_cost` subtracts that cost; actual transition costs remain unknown without holdings.

## 2:00-3:00 ? How weights are chosen

[`optimize`](../src/engine.py#L63) in `src/engine.py`, lines 63-78. `target` combines the illustrative CPI assumption, Cedar's real-return spread, and additional annual cost. The equality constraint makes weights sum to one. The return inequality compares weighted gross return minus modeled trade cost with the target. Bounds enforce long-only/position limits and the BIL reserve floor. SLSQP minimizes `w@cov@w`; multiplying the objective by 100 helps numerical scaling without changing its minimizer. The exact gradient is `200*cov@w`.

The solver must succeed **and** the independent rule check must find no failed testable constraint. A failed solve returns no usable allocation. The 77.04% BIL / 22.96% VT baseline is a calculated candidate, not a guaranteed ideal portfolio.

## 3:00-4:00 ? Compliance versus authorization

[`rules`](../src/engine.py#L44) in `src/engine.py`, lines 44-61. This function recomputes metrics and checks totals, long-only, bounds, reserve, liquidity assumptions, return hurdle and any supplied risk limit. Actual annual turnover needs a trade ledger. The final list separates failed rules from unknown evidence. Unknowns remain **Not Known**, but the authorization gate is **Fail** until they are resolved. Passing numerical checks does not establish suitability.

## 4:00-5:00 ? The recommendation

[`stop_decision`](../src/workflow.py#L37) in `src/workflow.py`, lines 37-53 uses solver status, vintage validity, data warnings, stress feasibility and allocation instability. It also lists unresolved mandate evidence. The current result is Reject deployment because that evidence is incomplete. The present research controls do not clear human approvals or verify the real five-year objective. A different allocation can coexist with the same action verb; explain the reasons instead of forcing the verb to change.

[`run`](../src/workflow.py#L55) in `src/workflow.py`, lines 55-87 ties data, signal, optimizer, baselines, checks, ordinary stresses and the decision together. `app.py` calls this shared workflow; it does not implement separate portfolio math.

## 5:00-6:00 ? A real test and three likely questions

Candidate test, if it addresses the student's own risky claim: `.venv\Scripts\python.exe -m pytest -q tests/test_final_audit.py -k unknown_mandate`. It tests that missing mandate evidence blocks authorization without inventing a numerical failed rule. The student must personally run/read it to claim verification.

1. **Why is volatility not the weighted average of fund volatilities?** Covariance matters: portfolio variance is the sum of every weighted pairwise covariance. Take the square root only after summing.
2. **Why can the optimizer succeed but authorization fail?** Solver success covers its numerical constraints. Missing risk-policy, reserve, annual-turnover and objective evidence still prevents full mandate certification.
3. **Is a return of 5.50% the same as achieving CPI+3% after costs over five years?** No. It is an annualized historical arithmetic estimate under an illustrative CPI assumption. Realized geometric returns, inflation and actual costs require separate evidence.

Before class, locate these functions in the editor and trace the baseline from CSV to result. Line references describe the current code; recheck them if the source changes. Do not use a previously published stress result as an unseen prediction.


## Exact calculation statements to point at

| File and line | Statement | What it does |
| --- | --- | --- |
| [src/engine.py:34](../src/engine.py#L34) | `variance=float(w@cov@w);gross=float(w@mu)` | Portfolio variance and annual gross return |
| [src/engine.py:38](../src/engine.py#L38) | `ongoing=config['ongoing_cost_bps']/10000` | Converts annual basis points to decimal cost |
| [src/engine.py:68](../src/engine.py#L68) | `target=config['cpi_assumption']+config['real_return_objective']+config['ongoing_cost_bps']/10000` | Forms the optimizer return hurdle |
| [src/engine.py:75](../src/engine.py#L75) | `res=minimize(` | Minimizes variance subject to constraints |
| [src/engine.py:77](../src/engine.py#L77) | `success=bool(res.success` | Requires solver success and the separate rule check |
| [src/workflow.py:49](../src/workflow.py#L49) | `status='Fail' if failed` | Combines failures and unknown evidence into process status |
