# Tuesday studio preparation and validation

**Current status, November 18:** This document records the earlier Week 12 preparation, when the repository had not yet been published. The distinct [Week 13 Lab 20 checkout](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md) is **25 or 0** and requires the partner cold run, committed pre-run AI-off prediction, one fix or recorded clean run, and decision line. The project is now [published on GitHub](https://github.com/AndrewK6637/fin439-project2). The older statements below are dated preparation evidence, not current submission status. See [final audit](../FINAL_PROJECT_2_AUDIT.md) for current testing and remaining work.

OpenAI Codex helped prepare documentation, repair one input-control issue, and run software checks. Student/partner classroom evidence remains blank. Educational work, not investment advice.

## Official scope verified

The freshly retrieved [Week 12 handout](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-12/student-handout.md) says both meetings are open studios with **no lab checkout or lab points**. Tuesday asks for an AI-off committee decision and reversal claim, a partner README-only cold run, a test of the riskiest claim, and a frozen must-fix list. The **25-or-0** label appears in [Lab 11](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-06/lab-11-proforma-what-if.md); it is not the current Week 12 grading statement. A different private Brightspace instruction is unverified.

The [Project 2 assignment](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md) still requires the app, mandate, alternatives, PIT signal/data card, ordinary stresses, genuine locked record, recommendation and disclosures. Official downloads are preserved in `references/tuesday-checkout/` with retrieval status.

## Evidence map

| Item | Evidence | Status |
| --- | --- | --- |
| Baseline run | `outputs/results.json`, `docs/checkout-results.md` | Executed; same 77.04% BIL / 22.96% VT candidate, 5.50% annual mean estimate and 3.53% volatility |
| Mandate check | Per-rule table in checkout results; `src/engine.py:rules` | Executed; constrained numerical checks pass, full mandate Not Known, authorization Fail |
| Stress run | Four existing scenarios in checkout results and raw JSON | Executed; not a new classroom prediction record |
| Independent arithmetic | `outputs/audit-independent-finance.json`, `scripts/audit_finance.py` | Rerun; scalar means/covariance/volatility agree within 1e-12 |
| Source reconciliation | `outputs/source-audit.json` | Rerun; 244 exact price matches and 54 recovered hashes |
| Unit and AppTest suite | `outputs/tuesday-tests.txt` | 66 passed, zero failed, 12.01 seconds in final main run |
| Fresh setup | `outputs/tuesday-fresh-install.txt`, `outputs/tuesday-short-install.txt` | First long-path install failed and is preserved; shorter-path retry succeeded, pip check passed, 66 tests passed in 17.34 seconds; fresh server returned HTTP 200/ok. See `outputs/tuesday-cold-tests.txt` and `outputs/tuesday-cold-smoke.json` |
| App server | `outputs/tuesday-server-smoke.json` | Main app started on port 8522; HTTP 200/ok |
| Student/partner cold run | `docs/partner-cold-run-template.md` | Blank; agent tests are not partner evidence |
| Existing Locked Record | `docs/changed-input-record.md`, `config/locked_experiment.json` | Protocol only; student fields blank; actual run absent |
| New classroom scenario | `docs/tuesday-changed-input-template.md` | Blank prediction and observed outcomes; reserved scenario not executed |

## Corrections and reproducibility limits

The return-override checkbox formerly initialized every fund to 5.5%, so simply opening overrides could silently change several inputs. It now initializes each box from the same loaded estimate used by the model. `test_enabling_overrides_preserves_loaded_estimates` verifies this within 1e-12. The dashboard also displays the estimate after additional annual costs, before unverified transition costs. No portfolio method, original mandate parameter, source data or investment decision was changed.

The first fresh installation failed in the deeply nested `tuesday-cold/.venv` folder with a long Windows path inside Streamlit. The error is retained, not erased. The README now recommends a short extraction path and explains how to repeat setup without changing security settings. Final retry evidence is recorded above. Windows/Python 3.13 is the verified platform; macOS/Linux commands are supplied but untested.

Visual browser rendering has not been verified. AppTest exercises tables, tabs and controls programmatically; HTTP health confirms server startup. Neither is a claim of a real partner run.

The default analysis remains frozen at November 2 with prices ending September 30, 2026. It is not updated market advice. Missing risk-policy interpretation, benchmark/reserve approval, actual holdings/costs, student signal review and real after-cost objective evidence block deployment. Reconsideration requires those issues to be resolved and the model to be reviewed again, not a forced action-verb change.

## Classroom evidence protection

No annual-cost classroom scenario was run. No prediction direction, observed before/after result, partner response or personal reflection was supplied by AI. The existing reserve locked protocol and JSON are unchanged. The new template is separate and must be genuinely completed with AI closed; link it explicitly only after completion if it becomes the submitted final Locked Record.

## GitHub and final submission

Starting HEAD: `5fd1d50`. No remote is configured. Prepared changes are intentionally **uncommitted and unpushed** under the latest user instruction. Therefore results and new instructions are ready locally, not verified as visible on GitHub. A partner cannot use a real repository README link until the owner authorizes and publishes the reviewed package.

All three video scripts exist, but no actual video URLs or corrected transcripts are supplied. Video 1 covers system/thinking changes and a checked AI output (maximum 3 minutes); Video 2 explains code/tests (maximum 5 minutes); Video 3 starts with the live app and presents the committee decision (maximum 5 minutes). The student must record/upload, save actual transcripts under `docs/transcript-video-1.txt` through `-3.txt`, fill manifest links/access checks, and attach the decision/validation Markdown files to Brightspace. Scripts are not transcripts.

## Before-class order

1. Review and authorize committing/publishing the preparation changes; provide the actual README URL to your partner.
2. Close AI and write your own decision and reversal claim in `tuesday-studio-record.md`.
3. Partner follows only README, records real first failure/time/result and swaps roles; do not coach.
4. Personally test your chosen risky claim, then freeze the must-fix list. Do not add new analysis during that studio step.
5. If doing the separate changed-input requirement, complete the genuine pre-run prediction/commit first; never use the published 36-month example as an unseen prediction.
