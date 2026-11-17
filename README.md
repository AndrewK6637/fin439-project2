OpenAI Codex helped recover coursework, write and debug code, run tests, and draft explanations.

The student is responsible for the analysis and final decision; student review is pending. This is educational work, not investment advice.

# Cedar Scholarship Foundation: FIN 439 Project 2

A six-tab Streamlit investment committee dashboard built from the student's recovered Labs 13-17. The frozen research decision is **November 2, 2026**, using monthly adjusted prices through September 2026. It is not a live trading application.

## Install and run

Python 3.13 was tested. From this project folder in PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.venv\Scripts\Activate.ps1
streamlit run app.py
```

Activation is optional: `.venv\Scripts\python.exe -m streamlit run app.py` works without changing execution policy. On macOS/Linux use `.venv/bin/python` and `source .venv/bin/activate`. No API keys are required for the bundled frozen analysis. Free dependencies require internet during installation; calculations then run offline.

```powershell
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe scripts/audit_sources.py
.venv\Scripts\python.exe scripts/build_reports.py
```

The last command regenerates the default decision memo and visible results. It never runs the locked experiment. Use `requirements.txt` for compatible ranges or the tested `requirements-lock.txt` for the exact environment. No runtime depends on the original absolute coursework paths; those paths are provenance records only.

## Mandate and model

Cedar has $20 million, a ten-year horizon, quarterly $150,000 scholarships, and an objective of CPI + 3% after costs over rolling five-year periods. The original universe is BIL, IEF, LQD and VT. The research comparator is 60% VT / 40% LQD inherited from Lab 14; Cedar-specific approval was not recovered.

The model compares equal weight, inverse volatility, and constrained minimum variance. Estimates use arithmetic monthly means multiplied by 12 and sample covariance multiplied by 12. A 2.5% illustrative CPI assumption produces a 5.5% nominal hurdle; this is not a verified forecast. The annual geometric real objective is not equivalent to this arithmetic estimate.

BIL is an unapproved proxy for the $600,000 cash/short-Treasury reserve. All portfolios face the same testable rules. Missing numeric risk limits, actual holdings/trades, and reserve approval remain **Not Known**. Failing baselines stay visible. Infeasible optimization is reported, never replaced with a fake solution.

The default constrained research allocation is approximately 77.04% BIL and 22.96% VT, with estimated return 5.50% and volatility 3.53%. Full compliance is not established. The draft recommendation is **Reject deployment**, allocating 0% to this unapproved process until missing evidence is resolved. That is not an instruction to liquidate existing client holdings.

## Data and point-in-time signal

`data/raw/` preserves the recovered Yahoo chart responses and download metadata. `data/processed/prices.csv` contains 61 month-end adjusted prices. The source audit reconciles every price exactly to raw adjusted close. These are provider-adjusted return proxies; dividends and splits were not independently reconstructed. Missing months are not bridged or forward-filled.

Lab 17 quarantined an unspecified macro signal. This project proposes CPIAUCSL inflation pressure, explicitly a fallback, not the student's original selection. The ALFRED November 1 snapshot precedes the November 2 decision. September 2026 CPI divided by September 2025 CPI implies 3.717% inflation; above 3% raises the analytical BIL floor to 5%. The default solution already exceeds that floor, so its weights do not change. Read `docs/signal-data-card.md` before interpreting it. Student source-value checks and approval remain pending.

The snapshot is reproducible, not automatically refreshed. `scripts/download_signal.py` documents retrieval of the frozen vintage. Archived Lab 14 download code is preserved under `recovered/`; a new date/universe requires deliberate source retrieval, metadata updates and validation, not a silent substitution. The holdout diagnostic separates training and evaluation but uses later revised prices, so it is not an implementable point-in-time backtest.

## Controls, stress tests and stop rules

Change estimation window, CPI assumption, annual costs, per-side transaction costs, reserve floor, maximum weight, optional risk cap, or individual annual return estimates in the sidebar. These are scenarios, not approvals to alter Cedar's mandate. The saved memo always describes the frozen default run; download the scenario JSON for customized results.

Four ordinary stresses perturb VT returns, use 36 observations, raise trading costs, and cap a fund at 70%. Transaction costs use explicit hypothetical holdings; actual turnover remains unknown. Invalid provenance, stale data, infeasible optimization or weight instability above 20 percentage points stops deployment. Unresolved evidence also blocks authorization.

## Student-only locked experiment

Read `docs/changed-input-record.md`. Write the prediction yourself with AI closed, commit and push it to GitHub, then run the gated command yourself with AI closed. **Do not ask AI for the prediction or execute the experiment beforehand.** The experiment is prepared but has never been run. Ordinary stress tests are separate.

## Files and submission

- `app.py`: six dashboard tabs.
- `src/`: data, portfolio engine, vintage checks, shared workflow.
- `config/`: recovered mandate and blank locked prediction fields.
- `tests/`: numerical, missing-data, feasibility, timing and Streamlit tests.
- `outputs/`: actual executed results, source audit and validation logs.
- `docs/`: memo, methodology, AI disclosure, requirement matrix, recovery inventory, final review and manifest.
- `videos/`: timed recording scripts and checklist; not recordings or transcripts.
- `references/`, `recovered/`: official requirements and original coursework copies.

No GitHub push, Brightspace submission, recording or upload has occurred. The full analytic rubric descriptor file was unavailable; verified syllabus weights are documented without inventing descriptors. See `PROJECT_HANDOFF.md` and `docs/final-review.md` for remaining student actions. The optional investor panel is deferred until mandatory evidence is complete.
