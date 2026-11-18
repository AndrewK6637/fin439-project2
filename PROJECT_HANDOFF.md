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

## PROJECT 2 FINAL AUDIT PROGRESS

### Objective and completion
Perform an independent-method audit of the existing project against fresh official requirements, correct confirmed bugs, verify finance and app behavior, and assess submission readiness. Audit completed November 16, 2026; original implementation and history preserved. No original mandate parameter, default allocation or locked prediction was changed.

### Requirements checked and statuses
Fresh assignment, checklist, shared submission architecture and Labs 13-17 downloaded/read under references/final-audit/. Core requirements: 4 Fully verified (app, alternatives, stress, disclosure); 4 Blocked by student action (mandate clarification, signal admission, locked record, final judgment). Six delivery requirements also student-blocked. Browser visual inspection Implemented but not independently verified; full rubric descriptors Incomplete due 404/absent tree. Verified syllabus maxima total 300; earned score/percentage pending, no invented allocation or grade.

### Bugs discovered and corrected
Exact ALFRED URL/query/hash validation; missing/nonfinite/latest CPI quarantine; removal of current holdings from historical optimization; one-rebalance turnover separated from actual annual ledger compliance; safe missing solver iteration metadata for fixed bounds; explicit empty/invalid data checks; visible nonzero hypothetical transaction-cost sensitivity; model/input freeze gate for locked experiment; binary authorization gate alongside unknown financial rules; obsolete Streamlit width API, disclosure ordering and transcript docs paths corrected. Ten finding groups recorded in docs/project2-final-audit.md.

### Tests and results
Baseline 31 passed in 4.55s. Final main suite 65 passed in 5.94s, zero failed. Fresh isolated pinned environment and separate project copy: 65 passed in 6.14s, zero failed. pip check: no broken requirements. HTTP server 8521 health 200/ok. Six-tab AppTest includes input controls, infeasibility and missing-data errors. Browser access host retried, unavailable; no visual claim.
Independent scalar arithmetic agrees with all three portfolios and benchmark within 1e-12. Raw source audit: 244 exact price matches, 54 recovery hashes. Independent ALFRED download: 957 matching rows and identical hash. Historical credential-pattern scan checked 132 blobs with zero matches; current tracked-file heuristic also zero; no >5MB tracked file at audit scan.
One intermediate test expected infeasibility from a single negative VT return while other assets still met the hurdle; corrected the erroneous test fixture, retained its failure log. Initial pip network request blocked; authorized retry installed dependencies. PowerShell surfaced pip update notice on stderr after successful installation; package inspection/check/tests verified installation.

### Files modified
src/engine.py, signal.py, workflow.py, data.py; app.py; scripts/locked_experiment.py; tests/test_app.py, test_locked_gate.py; new tests/test_final_audit.py and scripts/audit_finance.py. Updated README, memo/generated outputs, methodology, signal card, validation record, requirement matrix, manifests, video scripts, PROJECT_STATUS.md. New docs/project2-final-audit.md, docs/project2-grade-audit.md, outputs/audit-* evidence and fresh references/final-audit/.

### Git status and current task
Audit began at f93f2a8 on main. Initial commit 891dc5e retained. Completed audit corrections/evidence are saved in commit 6b8a942. A final metadata/byte-preservation checkpoint follows; use git log -1 --oneline and git status --short for its identifier. No remote/push/submission. This handoff records completion, not a low-context stop; exact token percentage unavailable.

### Next exact task / student actions
Read docs/project2-final-audit.md and docs/project2-grade-audit.md. Resolve/record mandate and signal judgments; personally verify source values. With AI closed, author genuine prediction, commit and push, then run and reconcile with AI closed. Do not execute the locked experiment in an AI session. Obtain full rubric and perform human visual review. Record three videos (3/5/5-minute maxima), save corrected actual transcripts in docs/, publish only when authorized, fill real manifest/access fields, attach the two Markdown documents and submit yourself. No remaining autonomous audit task requires a rebuild.

### Resume commands
.venv/Scripts/python.exe -m pytest -q
.venv/Scripts/python.exe scripts/audit_finance.py
.venv/Scripts/python.exe scripts/audit_sources.py
.venv/Scripts/python.exe -m streamlit run app.py --server.port 8521
Audit server currently running at http://127.0.0.1:8521; use existing server or another port if occupied. Detailed logs in outputs/audit-tests.txt and outputs/audit-clean-environment-tests.txt. Ignored .validation-work/ holds audit-venv and audit-portable; do not submit these environments.


## Tuesday studio preparation ? November 17, 2026 (in progress)

Latest user instruction explicitly forbids automatic commits/pushes. Leave all preparation changes uncommitted until approval. Starting HEAD 5fd1d50; no configured remote. Fresh official Week 12 handout says open studios with NO checkout points, contrary to the user's 25-or-0 premise. Prepared README-first navigation, generated baseline results, blank partner/classroom/studio records and code guide. Original locked reserve protocol preserved. Separate proposed annual-cost scenario is reserved and UNRUN; no prediction/result fields supplied.

Confirmed UI fix: enabling return overrides now starts from loaded estimates rather than replacing all funds with 5.5%; regression test added. Baseline and investment methodology unchanged. First current suite: 66 passed in 48.07s. New isolated .validation-work/tuesday-cold environment setup underway; final test and startup evidence pending. Do not claim partner cold run, GitHub publication or classroom evidence completed. Next: finish clean-environment tests/startup, write Tuesday validation/status and report readiness without committing.


### Tuesday preparation completed

Final report: docs/tuesday-preparation-report.md. Final main tests 66 passed in 12.01s; new isolated environment 66 passed in 17.34s. First deeply nested install failed due Windows path length; preserved outputs/tuesday-fresh-install.txt. Shorter .validation-work/c install succeeded; pip check and fresh-server HTTP 200 verified. Main server 8522 remains running; fresh server 8523 stopped. No visual/partner claim. No core strategy/configuration or locked record changed. No reserved annual-cost scenario executed.

All current preparation changes intentionally UNCOMMITTED and UNPUSHED; starting/latest HEAD remains 5fd1d50. Next exact action is owner review/approval for publication, then genuine AI-off studio decision and partner README-only run. Do not auto-commit based on older project instructions; latest user explicitly requires approval. Final submission videos/transcripts/URLs and genuine locked record still missing. README links generated results and all new classroom templates. Windows short-path troubleshooting added after actual failure. Source and independent arithmetic audits rerun successfully.

### Student checklist added November 17
Created START_HERE_Project_2_Checklist.docx, START_HERE.md, and scripts/build_student_checklist.py in the existing comprehensive project folder. Ten ordered student review and submission steps remain unchecked. DOCX reopened successfully and all guide links exist. Packaged renderer failed because bundled LibreOffice is absent; visual layout unverified. No strategy changes, file moves, commits, pushes, or student-only experiments. Previous next actions unchanged.

### GitHub publication preparation November 17
Owner explicitly authorized uploading the complete project to the public repository https://github.com/AndrewK6637/fin439-project2 (supersedes earlier no-push instruction and private preference). Remote verified reachable and empty. Latest pytest: 66 passed in 6.08s; source audit: 244 exact prices and 54 recovery hashes. Heuristic credential scan: 176 current files and 177 historical blobs, no matches; no files over 5MB. Environments/caches remain ignored. README now contains the real clone/download destination. Publication commit and push are next; verify remote HEAD before claiming success. AI-off prediction and partner records remain incomplete; no reserved experiment was run.


### GitHub publication verified
Uploaded the complete tracked project and preserved Git history to https://github.com/AndrewK6637/fin439-project2. Remote main was independently verified at c4f28ce53f74cd3e048ed816e72d594189424d48, matching local HEAD. Repository is public by the owner's latest choice. Authentication completed through Git Credential Manager; no credentials printed or committed. Initial ownership error resolved with a command-scoped safe.directory for this project only. README partner link: https://github.com/AndrewK6637/fin439-project2/blob/main/README.md. This status-only follow-up will be committed and pushed. No partner cold run, genuine AI-off prediction, videos, or Brightspace submission is claimed. Next: partner follows README from their own downloaded/clone copy; student completes remaining records honestly.


### November 18 final submission audit
Official Project 2 assignment/checklist and distinct Week 13 Lab 20 (25-or-0) reread. Project 1 score 218.4/300 supplied by student; actual feedback file not located in targeted coursework search, so no specific deductions invented. Current final report FINAL_PROJECT_2_AUDIT.md. Public repo cloned afresh; pinned dependency install and pip check succeeded, 66 tests passed in 22.22s; cloned app port 8531 returned HTTP 200 for root and health; server stopped. Main project after documentation fixes: 66 tests passed in 20.46s. Independent finance/source audits passed; 60-to-36-to-60 window altered weights and restored baseline exactly. Reserved AI-off cost experiment remained unrun. Reconciled misleading older Week 12/no-publication statements with dated notices; updated active Lab 20 template and real GitHub manifest links. No financial model/config/data, original mandate or draft decision changed. Student still owes genuine AI-off record, partner note/code explanation, policy/signal review, videos/transcripts, final judgment and Brightspace submission. Current task: commit and publish audit corrections if authorized by prior user upload instruction, then verify remote and report. Review git status/HEAD. No browser visual claim or Project 1 feedback-specific claim.

