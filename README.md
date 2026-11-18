OpenAI Codex helped recover coursework, write and debug code, run tests, and draft explanations.

The student is responsible for the analysis and final decision. The student selected the fund universe, comparison benchmark, illustrative BIL proxy and CPI fallback, and agreed with the draft hold on deployment; personal source checks and final submission review remain pending. This is educational work, not investment advice.

# Cedar Scholarship Foundation: FIN 439 Project 2

A six-tab Streamlit investment committee dashboard built from the student's recovered Labs 13-17. The frozen research decision is **November 2, 2026**, using monthly adjusted prices through September 2026. It is not a live trading application.

## Start here: results and class materials

**[Submission review - all required files](SUBMISSION_REVIEW.md)** | [Student checklist](WHAT_I_NEED_TO_DO.md) | [Student decision log](docs/student-decision-log.md) | [Investment results](docs/checkout-results.md) | [Decision memo](docs/decision-memo.md) | [Final audit](FINAL_PROJECT_2_AUDIT.md)

The application evaluates whether Cedar should deploy the proposed portfolio process. The recommendation is **Reject deployment pending unresolved mandate evidence**. It does not recommend selling existing holdings. Results are a frozen educational analysis, not current market forecasts. [The student decision record](docs/student-decision-log.md) traces the earlier coursework and the student's later choices.

## Get your own copy

Open **[AndrewK6637/fin439-project2](https://github.com/AndrewK6637/fin439-project2)**. Choose **Code > Download ZIP**, extract it into a short folder such as `C:\fin439`, and open a terminal in the folder containing **this README, `app.py`, `requirements-lock.txt`, `src/`, `config/` and `data/`**. Alternatively, run `git clone https://github.com/AndrewK6637/fin439-project2.git` and then `cd fin439-project2`. Download the entire project, not just this README. Each person creates their own virtual environment below.

## Install dependencies (Windows PowerShell)

Install Python **3.13**, the tested version. Use a short extraction path on Windows (for example `C:\fin439`) rather than many nested folders. From the project folder:

```powershell
python --version
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
```

If Windows cannot find `python`, use `py -3.13` for the first two commands. Internet is needed for installation; the bundled analysis runs offline afterward. No API key, paid service, login or personal coursework folder is needed.

## Run the application - one command

```powershell
.venv\Scripts\python.exe -m streamlit run app.py
```

Open **http://localhost:8501** when the terminal reports the server is ready. Leave that terminal running; Ctrl+C stops it. No virtual-environment activation or execution-policy change is necessary. If port 8501 is occupied, append `--server.port 8522` and open the port printed in the terminal. If installation reports `OSError: [Errno 2]` for a very long path inside Streamlit, extract a fresh copy into a shorter folder and repeat installation; do not change system security settings. A missing Streamlit module means the installation step used a different interpreter; rerun the exact pip command above.

On macOS/Linux, use `python3 -m venv .venv`, `.venv/bin/python -m pip install -r requirements.txt`, then `.venv/bin/python -m streamlit run app.py`. Those platform steps are provided for convenience; only Windows/Python 3.13 has been verified.

## Find the result and try a documented demonstration

1. Start at **Executive dashboard**. Read the draft decision, estimated annual return, volatility and full mandate status.
2. Open **Portfolio comparison** for all three allocations, benchmark differences, failed rules and unknown evidence. **Fail authorization** can mean missing evidence; it is not a fabricated numerical breach.
3. In the sidebar change **Estimation months** from **60 to 36**. The app recalculates automatically; **Rerun model** also reruns the page. Compare the new weights and estimates with [the already executed stress table](docs/checkout-results.md). Restore **60** afterward.
4. Open **Stress testing** for four documented scenarios, and **Committee recommendation** for the decision and monitors. The saved memo describes the frozen default; the live values and **Download this scenario** reflect the current controls.

This 36-month demonstration was already executed during development. It is **not your unseen classroom prediction exercise** and must not be presented as one. Use the separate [blank classroom template](docs/tuesday-changed-input-template.md) only after writing your own prediction with AI closed. The existing [locked record](docs/changed-input-record.md) is preserved separately.

## Included inputs and outputs

`config/mandate.json` holds the recovered mandate and labeled assumptions. `data/processed/prices.csv` contains the four funds' monthly adjusted prices. `data/raw/` holds their source responses, metadata and the historical ALFRED signal snapshot. Keep these folders together. `outputs/results.json` and [checkout-results.md](docs/checkout-results.md) contain actual generated default results. Do not replace missing inputs with invented data.

Main controls: estimation window; illustrative CPI; additional annual costs in **basis points**; per-side transaction costs; reserve/position bounds; optional illustrative risk cap; and annual return assumptions in **percent**. Return override boxes start from the loaded estimates, so simply enabling them does not silently replace every fund's return. Overrides are scenarios, not changes to the original client mandate. Unknown holdings mean actual transaction costs cannot be certified.

## Reproduce and validate (optional for first launch)

```powershell
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe scripts/audit_sources.py
.venv\Scripts\python.exe scripts/audit_finance.py
.venv\Scripts\python.exe scripts/build_reports.py
.venv\Scripts\python.exe scripts/build_checkout_results.py
```

The report commands regenerate baseline and existing ordinary stress evidence, never either student-only experiment. Test logs and reproduction limits are in [Tuesday validation](docs/tuesday-checkout-validation.md). A partner must fill [their own cold-run record](docs/partner-cold-run-template.md); agent testing is not partner evidence.

## Mandate and model

Cedar has $20 million, a ten-year horizon, quarterly $150,000 scholarships, and an objective of CPI + 3% after costs over rolling five-year periods. The original universe is BIL, IEF, LQD and VT. The research comparator is 60% VT / 40% LQD inherited from Lab 14; Cedar-specific approval was not recovered.

The model compares equal weight, inverse volatility, and constrained minimum variance. Estimates use arithmetic monthly means multiplied by 12 and sample covariance multiplied by 12. A 2.5% illustrative CPI assumption produces a 5.5% nominal hurdle; this is not a verified forecast. The annual geometric real objective is not equivalent to this arithmetic estimate.

BIL is the student's chosen **illustrative stand-in** for the $600,000 cash/short-Treasury reserve, not a documented Cedar-approved reserve holding. All portfolios face the same testable rules. Missing numeric risk limits, actual holdings/trades, and Cedar reserve approval remain **Not Known**. Failing baselines stay visible. Infeasible optimization is reported, never replaced with a fake solution.

The default constrained research allocation is approximately 77.04% BIL and 22.96% VT, with estimated return 5.50% and volatility 3.53%. Full compliance is not established. The recommendation is **Reject deployment for now: no new allocation to this process** until missing evidence is resolved. That is not an instruction to liquidate existing client holdings.

## Data and point-in-time signal

`data/raw/` preserves the recovered Yahoo chart responses and download metadata. `data/processed/prices.csv` contains 61 month-end adjusted prices. The source audit reconciles every price exactly to raw adjusted close. These are provider-adjusted return proxies; dividends and splits were not independently reconstructed. Missing months are not bridged or forward-filled.

Lab 17 quarantined an unspecified macro signal. The student chose to keep this AI-proposed CPIAUCSL inflation-pressure fallback for Project 2; it was not the original Lab 17 selection. The ALFRED November 1 snapshot precedes the November 2 decision. September 2026 CPI divided by September 2025 CPI implies 3.717% inflation; above 3% raises the analytical BIL floor to 5%. The default solution already exceeds that floor, so its weights do not change. Read `docs/signal-data-card.md` before interpreting it. Personal source-value checks and Cedar deployment approval remain pending.

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

GitHub publication is authorized by the owner. Brightspace submission, video recording and video upload remain student actions. Historical audit files describe their actual earlier state before publication. The full analytic rubric descriptor file was unavailable; verified syllabus weights are documented without inventing descriptors. See `PROJECT_HANDOFF.md` and `docs/final-review.md` for remaining student actions. The optional investor panel is deferred until mandatory evidence is complete.


## Earlier audit (November 16)

The final audit expanded validation to 65 tests, independently reconciled portfolio arithmetic and the ALFRED snapshot, and tested a fresh pinned environment. Run `python scripts/audit_finance.py` for the independent numerical reconciliation. Read `docs/project2-final-audit.md` and `docs/project2-grade-audit.md` for current readiness. The dashboard's authorization gate is binary: unknown mandate evidence fails authorization while the financial rule remains Not Known. The transaction-cost stress exposes a hypothetical nonzero transition at both the sidebar cost and 50 bps; it does not invent client holdings.
