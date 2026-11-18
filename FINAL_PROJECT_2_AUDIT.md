# FIN 439 Project 2 Final Audit

Audit date: November 18, 2026. Project: Cedar Scholarship Foundation. This is an AI-assisted technical and evidence audit, not the student's final investment approval or a professor's grade. Source hierarchy: [Project 2 assignment](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md), [major-project checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md), [Lab 20](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md), and Labs 13-17 preserved under `references/final-audit/`. Project 1's reported 218.4/300 score is student supplied; the professor's actual comments were not found in the accessible coursework files. Specific Project 1 deductions therefore remain **NOT VERIFIED**.

## Decision and highest grading risks

The AI-assisted draft says **Reject deployment** of the proposed process, with **0%-0% new allocation** until mandate approvals, real costs/holdings, signal admission and the locked record are resolved. This does not call for liquidating existing assets. The constrained research result is 77.04% BIL and 22.96% VT, 5.50% annual arithmetic mean estimate and 3.53% annualized volatility. Its testable numerical rules pass; complete mandate compliance is **Not Known**, so authorization fails. The student has not adopted the draft judgment.

| Priority | Finding | Status and action |
| --- | --- | --- |
| Critical | The required AI-off prediction, prior GitHub commit, subsequent run and reconciliation are absent. The public record is not a Locked Changed-Input Record. | **NEEDS ACTION:** student writes and commits/pushes prediction with AI closed before running; preserves before/after output and diagnosis. Do not relabel the AI-assisted discussion as AI-off. |
| Critical | Actual three videos, corrected transcripts, YouTube URLs and Brightspace attachments are absent. | **NEEDS ACTION:** record, correct, upload, verify and submit. Scripts are only preparation. |
| High | Original numeric risk limit, benchmark approval, BIL reserve-proxy eligibility, actual holdings/trades and cost schedule are unsupported. | **NEEDS ACTION:** find dated policy/account evidence or leave the rules Not Known and keep deployment rejected. |
| High | Lab 17 quarantined the original unspecified macro signal; CPIAUCSL is an AI-proposed fallback. | **NEEDS ACTION:** student reviews/adopts or rejects the fallback and independently checks the dated observations. The vintage and source bytes have technical verification. |
| High | Student committee decision, partner's README-only cold-run note and six-minute code defense are absent. | **NEEDS ACTION:** complete personally; AI tests do not substitute. |
| Medium | Previously published Week 12 preparation files mistakenly implied there was no 25-or-0 Lab 20 and that GitHub was unpublished. | **FIXED:** current student-facing templates, validation, result generator and dated preparation notices identify the distinct graded Week 13 Lab 20 and public repository. Older dated logs remain as historical evidence. |
| Medium | Earlier manifest had blank locations for already-published written artifacts. | **FIXED:** repository, visible results, memo and validation GitHub locations populated; video/transcript URLs and final access checks remain blank. |
| Low | Full analytic rubric performance descriptors were unavailable at the earlier source check. | **NOT VERIFIED:** only six published syllabus weights totaling 300 are used; no earned grade is invented. |

## Requirements checklist

| Requirement | Status | Evidence or remaining work |
| --- | --- | --- |
| Python web app and README start path | **PASS** | Fresh public clone, pinned dependency install, 66 passing tests and HTTP 200 for app and health. Human visual/browser review remains unverified. |
| Lab 13 objective, universe, benchmark, risk measure and limits | **NEEDS ACTION** | Original Cedar objective and BIL/IEF/LQD/VT recovered. Numeric risk limit, comparator approval and reserve proxy require student/client evidence. |
| Equal weight, transparent inverse-volatility baseline and constrained portfolio | **PASS** | All three displayed with weights, estimates, failed/unknown rules. Independent arithmetic agrees within numerical tolerance; infeasibility and errors tested. |
| Point-in-time signal and data card | **NEEDS ACTION** | Historical ALFRED vintage and 957 rows verified technically; student admission/three source-value checks remain pending. Later revised prices are not called a point-in-time backtest. |
| Estimates, window, costs and constraint stresses plus stop condition | **PASS** | Four executed ordinary stress scenarios, explicit stop triggers and documented hypothetical-cost limits. These stresses are not the locked experiment. |
| Locked Changed-Input Record | **NEEDS ACTION** | Blank student fields; no locked output or pre-run student commit. |
| Recommendation, allocation range, monitoring and reversal | **NEEDS ACTION** | Draft Reject with 0%-0% new-process allocation, monitors and evidence conditions is supported; student must own the final judgment. |
| Opening AI announcement and responsibility/education disclosures | **PASS** | README, memo and three scripts contain the statements; spoken video versions await recording. |
| Public repository, dependencies, data and visible result | **PASS** | Public clone succeeded; all needed frozen input folders are included. Reviewer access was technically verified by clone, not by a human grader. |
| Decision and validation Markdown attached to Brightspace | **NEEDS ACTION** | Files exist on GitHub; final content review and attachments remain student actions. |
| Videos 1-3 and corrected transcripts | **NEEDS ACTION** | Scripts exist; no actual recordings, captions/transcripts or verified video links. Limits: 3/5/5 minutes; Video 3 opens with live app. |
| Final manifest and access confirmation | **NEEDS ACTION** | Written GitHub links now filled; video/transcript rows, durations, timestamp indices and frozen revision remain pending. |
| Lab 20 partner cold run, fix/clean outcome and code explanation | **NEEDS ACTION** | Blank real partner record. Separate automated clone is technical evidence only. Lab 20 is 25 or 0. |
| Full rubric descriptor audit and Project 1 feedback comparison | **NOT VERIFIED** | Published syllabus category maxima are 45/45/60/45/75/30; full descriptors and actual Project 1 feedback comments were not accessible. |

## Financial soundness

This is a portfolio allocation project, so **WACC, terminal growth and valuation multiples do not apply**. Its load-bearing assumptions are historical arithmetic means and sample covariance from 60 monthly returns; a 2.5% CPI illustration plus the 3% real spread to form a 5.5% additive screening hurdle; zero additional annual costs in the baseline; 10 bps per-side illustrative trading cost; a 60% VT/40% LQD comparator; BIL as a $600,000 reserve proxy; and a proposed CPIAUCSL trigger above 3% that raises the analytical BIL floor to 5%. The source and mathematics are documented; **forward reasonableness and client approval are not established**. The five-year compounded real after-cost mandate is not proven by an annual arithmetic estimate. Obtain client policy, actual positions/trades, cost schedule, dated macro checks and committee approval before any deployment claim.

The independent scalar audit reconstructed portfolio means and sample covariance from the CSV without the production estimator; all three portfolios and the benchmark agree within 1e-12. The source audit matches 244 processed prices to the preserved raw responses exactly and verifies 54 recovered file hashes. These checks support arithmetic and provenance, not a forecast or a client mandate approval.

## Reproduction and tests actually executed

Public GitHub commit `61be6f5` was cloned into a separate ignored folder. In a fresh Python 3.13 Windows environment, `pip install -r requirements-lock.txt` succeeded after a sandbox-network retry; `pip check` found no broken requirements; **66 tests passed, 0 failed in 22.22 seconds**. The cloned Streamlit app started on port 8531 and returned HTTP 200 for `/` and `/_stcore/health`. Browser visual inspection was not performed. The initial sandboxed pip request failed due network restriction; the authorized retry succeeded. Earlier tests also documented an actual Windows long-path installation failure and short-path recovery.

The default constrained weights were `[0.7704206870, 0, 0, 0.2295793130]`, annual mean `0.0550000000` and volatility `0.0352698837`. Changing the **already published** estimation window from 60 to 36 months yielded `[0.9285923216, ~0, 0, 0.0714076784]`, annual mean about `0.055` and volatility `0.0088726611`. Restoring 60 months reproduced the original weights, mean and volatility exactly in the executed check. The reserved 0-to-75-bps classroom experiment was **not** run.

Exact Windows commands after cloning into `fin439-project2`:

```powershell
cd fin439-project2
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.venv\Scripts\python.exe -m streamlit run app.py
.venv\Scripts\python.exe -m pytest -q
```

The first four commands are enough to reach the dashboard; tests are optional for a partner. On macOS/Linux use the platform commands in `README.md`; that path was not executed in this audit. A real partner must still run the README alone and record the first failure, elapsed time and result location.

## Changes and submission order

Safe corrections in this audit update the Lab 20 status, current publication statements, reproducible results generator, existing written manifest links and this report. No financial model, mandate configuration, source data, default figures or investment decision was changed. Historical dated test records were retained and labeled as such. Project 1 feedback was requested but was not available to compare line by line.

1. Student reviews mandate, source assumptions, CPI fallback and the draft decision; record a personal decision and reversal condition.
2. For Lab 20, give the partner only the [published README](https://github.com/AndrewK6637/fin439-project2/blob/main/README.md). Partner records their own cold run; student explains the actual code with AI closed and records the first fix or clean run.
3. With AI closed, write the genuine input-change prediction, commit and push it **before** the changed run. Save before/after evidence, reconciliation and subsequent commit. The blank `docs/tuesday-changed-input-template.md` and `docs/changed-input-record.md` are preparation only; choose one genuine record and link it from validation.
4. Record and upload the three videos to YouTube; correct real transcripts in `docs/`; finish the manifest with actual links, durations, access checks and final commit.
5. Submit the GitHub repository, `docs/decision-memo.md`, `docs/validation-and-ai-use.md`, the three YouTube links and transcripts, and the completed manifest. Attach the same two Markdown files to Brightspace. The exact due date is the Brightspace assignment header and was not verified here.

**Readiness:** technically reproducible from a fresh Windows clone; **not ready for final submission** because the locked record, student/partner evidence, final judgment, videos/transcripts and attachments are missing.
