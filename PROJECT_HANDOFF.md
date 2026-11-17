# FIN 439 Project 2 handoff

## Objective and project location
Build the Cedar investment management application from authentic coursework, with baselines, constrained optimization, PIT signal, stress tests, validation and submission materials.
Absolute directory: C:/Users/jklai/Documents/Courses/AIFinance2026/JKLai/fin439_project2_investment_management

## Completed progress
Recovered 54 files from Labs 13-17 without changing originals. Read downloaded official assignment/checklist/architecture/labs and syllabus. Built six-tab Streamlit app, shared financial engine, equal weight and inverse-volatility baselines, constrained minimum variance, honest mandate checks, authentic ALFRED vintage fallback signal, four ordinary stress categories, holdout diagnostic and gated locked experiment. Completed source audit, memo, methodology, AI-use validation, requirement matrix, final review, README, pinned dependencies, three timed video scripts and manifest templates.

## Important files
app.py; src/data.py, engine.py, signal.py, workflow.py; config/mandate.json; config/locked_experiment.json; scripts/build_reports.py, audit_sources.py, locked_experiment.py; tests/; docs/; videos/; outputs/results.json and visible-results.md; requirements-lock.txt.

## Decisions and results
Authentic Cedar mandate: $20m, quarterly $150,000 scholarships, CPI+3% after costs over rolling five years, $600,000 reserve, long-only fully invested, 95% five-day liquidity, 5% nonexempt issuer cap, annual rebalance and 20% turnover cap. Universe BIL/IEF/LQD/VT. Inherited 60VT/40LQD comparator lacks Cedar-specific approval. Numeric volatility cap, actual holdings/costs and BIL reserve proxy approval unknown. CPI forecast 2.5% remains illustrative.
Frozen decision 2026-11-02, prices through 2026-09-30. Proposed CPIAUCSL fallback uses authentic ALFRED 2026-11-01 vintage; source checks/student approval pending. Lab17 original was quarantine, not an approved CPI signal.
Constrained research weights 77.04% BIL / 22.96% VT, annual arithmetic estimate 5.50%, volatility 3.53%; full mandate Not Known. Equal weight 3.22%/7.50%; inverse-vol 3.33%/1.40%; both fail illustrative hurdle. Four ordinary stresses feasible; largest weight move 15.82pp. Draft Reject deployment, 0% allocation to unapproved process, not a liquidation instruction.

## Tests and executed commands
Main pytest: 31 passed, 0 failed, 4.62s. Portable copied-project pytest: 31 passed, 0 failed, 3.81s using same installed interpreter. Both source audits pass: 244 prices exactly reconciled and 54 recovered hashes verified. pip check: no broken requirements. AppTest exercises six tabs, window change and infeasible cap. Streamlit launched on 127.0.0.1:8520, HTTP health 200/ok. Browser visual rendering unverified; browser host unavailable. Fresh second dependency installation/remote clone not claimed. Logs in outputs/.
The held-out optimizer initially returned a failure status; objective scaling and analytic gradient corrected convergence. No failed solver was accepted as successful.

## Git state
Local main branch; initial implementation commit 891dc5e. Final implementation/documentation checkpoint is being committed after this handoff update. Run git log -1 and git status --short for the final checkpoint identifier/state. No remote configured and no push performed. Command-local automation identity is explicit, not the student's identity. .validation-work/ and .venv/ are ignored; the former contains the portable smoke-test copy.

## Blockers and remaining work
Full analytic rubric descriptor URL returned 404; only verified six syllabus categories totaling 300 are claimed. No authenticated personal GitHub repository was recoverable (no configured relevant remotes/GitHub CLI). Mandate approvals and student verification remain missing. No videos, actual transcripts or submission links exist. Optional investor panel deferred until mandatory evidence complete.
Locked experiment NOT RUN. Prediction fields remain blank; AI must not fill them or supply directional predictions. Student must author and commit/push with AI off, then execute and reconcile with AI off. Blank gate test is not the changed-input run.

## Current task and exact next step
Implementation and agent-controlled validation are complete. Next: student reviews recovered mandate and proposed signal, then supplies missing policy evidence. Do not rebuild the app or rerun the locked experiment autonomously. After genuine student review, update configuration and regenerate ordinary reports/tests; preserve the frozen outputs and genuine prediction chronology.

## Resume commands (PowerShell from project folder)
Get-Content PROJECT_HANDOFF.md
git status --short
git log -1 --oneline
.venv/Scripts/python.exe -m pytest -q
.venv/Scripts/python.exe scripts/audit_sources.py
.venv/Scripts/python.exe scripts/build_reports.py
.venv/Scripts/python.exe -m streamlit run app.py --server.port 8520
If 8520 is already occupied, use the existing server or select a new port; do not terminate unrelated processes.

## Student actions
1. Review/confirm risk policy, benchmark, reserve proxy, costs/current holdings, source observations and signal choice.
2. Complete genuine AI-off prediction/GitHub commit/run/reconciliation as instructed in docs/changed-input-record.md.
3. Review final recommendation personally; record real verification.
4. Record videos (3/5/5-minute maxima), upload to YouTube and save corrected actual transcripts.
5. Authorize GitHub publication, verify reviewer access, fill/freeze manifest, attach required MD documents and submit to Brightspace yourself.

Exact remaining context/account token allowance is not exposed. No percentage is claimed. All completed work and next actions are saved here.
