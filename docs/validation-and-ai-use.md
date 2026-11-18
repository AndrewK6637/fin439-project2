OpenAI Codex helped recover coursework, implement and debug the application, run automated validation, and draft documentation and scripts.

The student is responsible for the analysis and final decision. The student selected the coursework fund universe, comparator, illustrative reserve stand-in and CPI fallback, and agreed with the draft hold on deployment in AI-assisted discussion on November 18, 2026. Personal source checks and final submission review remain pending. This is educational work, not investment advice.

# Validation and AI use

## Tools, dates and responsibility

Material AI assistance occurred in this Codex session on November 16, 2026. The environment identifies the agent as Codex based on GPT-6; a more precise deployed model/build identifier was not independently exposed. No other AI model use is claimed. Codex generated the new application code, test code, proposed CPI fallback policy, draft memo and video scripts. Original student coursework remains in `recovered/` with provenance hashes.

Disposition: retain the tested code for research. The student selected the CPI fallback for Project 2 and agreed with the recommendation to withhold new investment for now. These choices are recorded, while personal source checks and final review remain open. Earlier coursework decisions are distinguishable from new analytical assumptions in configuration and the recovery inventory. No claim is made that the student personally checked the source values or completed the locked prediction; its fields remain blank.

The [student decision log](student-decision-log.md) records the student's actual choices made in AI chat on November 18, including the four-fund universe, comparison benchmark, illustrative BIL stand-in, CPI fallback, and agreement with holding deployment. This is evidence of human direction with AI assistance, not independent AI-off work or source verification.

## Sources and as-of boundary

The original Lab 14 Yahoo responses were retrieved October 20, 2026 and supply 61 month-end adjusted prices per fund through September 30. The frozen decision is November 2. `scripts/audit_sources.py` reconciled **244 prices exactly** to the raw adjusted-close field (maximum absolute difference zero for each fund) and verified all **54** recovered file hashes. Raw data, URLs and retrieval metadata are retained. These checks establish copying fidelity, not independent verification of provider adjustment methodology.

The CPIAUCSL signal uses an authentic ALFRED November 1 snapshot; its latest observation is September 2026. The transformation is 336.298 / 324.245 - 1 = approximately 3.71725%. Vintage identity, cutoff and source hash are checked. Current revised FRED observations are not substituted for this historical snapshot. The student chose to keep this AI-proposed fallback for Project 2 but must personally verify source observations; Lab 17 had quarantined its unspecified macro input.

## Original implementation validation (superseded by the final audit below)

- Main suite: `python -m pytest -q`: **31 passed, 0 failed, 4.62 seconds**. Exact output: `outputs/pytest-results.txt`.
- Copied project in a separate working directory, excluding the original virtual environment and Git directory: **31 passed, 0 failed, 3.81 seconds**, using the same installed interpreter. Source audit passed there too. Logs: `outputs/portable-test-results.txt`, `outputs/portable-source-audit.txt`.
- Streamlit started at `http://127.0.0.1:8520`; HTTP health endpoint returned **200 / ok**. Evidence: `outputs/server-smoke.json`.
- Streamlit AppTest exercised all six tabs, the 36-month input and an infeasible 10% maximum position cap. It observed no application exception and confirmed the infeasibility message.
- Browser visual rendering was not verified: browser host access was unavailable. AppTest and HTTP health are not represented as visual inspection.
- Dependency installation succeeded in the project's Python 3.13 virtual environment; versions are pinned in `requirements-lock.txt`. The portable check validates relative paths and runtime behavior; it is not claimed to be a second fresh dependency installation or a clean remote clone.

No test warnings were displayed in those original pytest summaries; that did not certify an absence of captured runtime logging. Streamlit's server startup message is informational. Tests were run before and after the numerical correction described below; an earlier run passed 30 tests, and the final added return-override test brings the suite to 31.

## Independently specified known answers and test scope

The two-asset fixture expects portfolio return 0.068, variance 0.010944 and volatility approximately 0.104613574. A separate inverse-volatility example has weights two thirds and one third. A minimum-variance fixture has the independently derived 80/20 allocation. These expected values are not computed by calling the production function under test.

Coverage includes return calculation, no forward fill, missing months, sample covariance/annualization, sum-to-one and bounds, long-only rules, reserve and risk constraints, infeasible targets, solver validation, zero/invalid covariance inputs, turnover and two-sided costs, known versus unknown compliance, signal dates/vintages/transformation, holdout training boundaries, stop conditions, four stresses, return overrides, and app controls. Recovered Lab 15 numerical estimates are separately compared with the new engine. The locked test only checks rejection of blank prediction fields; it does not execute the changed scenario.

## Errors discovered and corrections

An initial chronological-holdout optimization returned SLSQP's positive-directional-derivative failure despite a plausible candidate. The code did not accept that result as successful. Rescaling the objective and providing its analytical gradient produced successful convergence; the final holdout output includes the constrained portfolio. Feasibility is still checked independently of solver status.

The recovery copy initially included irrelevant dependency metadata under Lab 14. Only that newly created copy was removed after checking path containment; original files were untouched. Recovery inventory and hash audit now cover 54 relevant files. Raw and recovered files are protected from Git newline normalization through `.gitattributes`.

The dashboard originally displayed a saved default memo without an explicit scenario distinction. It now labels that memo as the frozen default; live results and downloaded scenario JSON reflect changed inputs. Expected-return override controls were added and tested.

## Stress evidence and limitations

The default constrained portfolio is 77.04% BIL and 22.96% VT, estimated arithmetic return 5.50%, volatility 3.53%. All four ordinary stress optimizations succeeded. Largest allocation moves are 3.14 percentage points after lowering VT's return estimate, 15.82 points using 36 months, approximately zero with the specified cost-only scenario, and 7.04 points under the 70% fund cap. The cost case starts from hypothetical baseline holdings, so a near-zero optimal trade is expected from that setup; the output also reports the nonzero cost of a hypothetical baseline-to-equal-weight transition. Actual client costs remain unverified.

The 48-month-training/12-month-evaluation diagnostic avoids estimation leakage, but uses a later downloaded adjusted-price snapshot and does not apply the current signal retrospectively. It cannot establish an implementable historical PIT strategy or forecast. Arithmetic estimates do not establish Cedar's geometric real after-cost five-year objective.

The student chose 60% VT / 40% LQD as the coursework comparison and BIL as an illustrative reserve stand-in. Cedar approval of the benchmark or BIL, the numeric Cedar risk limit, actual holdings/trades and forward CPI/cost assumptions remain unresolved. The student said Cedar's current investments are unavailable beyond the published project. Therefore the process status is Not Known and the draft deployment recommendation is Reject; the student agreed with the hold on deployment in AI chat. This is a decision about authorizing the proposed process, not liquidating client assets.

## Locked Changed-Input Record and student verification

See `docs/changed-input-record.md`. The deterministic experiment is prepared behind a gate. No student prediction has been written by AI, no pre-run student commit fabricated, and no locked experiment run. The student must author and commit/push the prediction with AI closed, then run and reconcile it with AI closed under the official rule.

Student verification status: **design and draft-decision choices stated in AI chat; personal source-value checks, independent classroom evidence and final submission review pending**. Video recordings, corrected actual transcripts and Brightspace attachments are also pending. The public project repository is now published at https://github.com/AndrewK6637/fin439-project2; grader access through the final manifest has not been checked. The full analytic rubric descriptor file returned 404; verified syllabus category weights are recorded in the requirements matrix without inventing descriptors or a score.


## Final independent-method audit ? November 16, 2026

Latest main suite: **65 passed, zero failed** (`outputs/audit-tests.txt`). A fresh isolated virtual environment was installed from the pinned requirements; the final tests also passed from a separate copied project (`outputs/audit-clean-environment-tests.txt`). This supersedes the earlier limitation that only a shared interpreter had been tested. `pip check` found no broken requirements. Initial networking was blocked by sandbox policy; authorized retrieval succeeded. PowerShell surfaced pip's update notice as a native-command warning after installation; installed packages and executed clean-environment tests confirm the successful setup.

The fresh server on port 8521 returned HTTP 200/ok. Browser access was retried and unavailable; visual verification remains unperformed. AppTest covered all tabs, window/constraint/return controls and missing-data error handling. Bare-mode Streamlit context messages are test-harness logging; deprecated width controls were replaced. An intermediate audit test incorrectly assumed one negative equity estimate must make the portfolio infeasible while other assets still met the hurdle. The test fixture was corrected, not the model's valid solution; its failure log is retained.

Independent plain-Python scalar calculations verified all portfolio and benchmark annual means, sample covariance and volatility within 1e-12. A fresh ALFRED response matched all 957 frozen rows exactly, including the final three observations. These are agent checks, not student personal verification. Original 244 price matches and 54 recovery hashes still pass.

Confirmed corrections: stricter vintage URL/hash validation; no silent fallback from missing latest CPI; rejection of nonfinite CPI; removal of present holdings from historical optimization; separate hypothetical rebalance versus actual annual turnover; safe fixed-bound solver metadata; explicit invalid input checks; visible nonzero transaction-cost sensitivity; frozen model/input gate for the locked experiment; binary authorization gate with unknown financial rules retained; corrected transcript paths and opening disclosures. No original mandate parameter or default allocation was changed.

See `docs/project2-final-audit.md` for findings and `docs/project2-grade-audit.md` for verified weights and pending scoring. The student-only record remains incomplete and was never run. All model freeze tests use gate-only fixtures without authoring student predictions. Historical Git blobs were scanned for common credential patterns; this heuristic does not certify every possible secret format. No remote publication or submission occurred.


## November 17 studio preparation

The November 17 preparation evidence is in [Tuesday validation](tuesday-checkout-validation.md): 66 tests, clean setup and preserved installation failure. That document describes Week 12 only. [Week 13 Lab 20](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md) is a distinct 25-or-0 checkout. The public GitHub repository was subsequently published. The README, visible results, blank classroom/partner records and code study guide are prepared; student and partner evidence is not fabricated. The proposed annual-cost classroom scenario and existing locked reserve scenario remain unrun.
