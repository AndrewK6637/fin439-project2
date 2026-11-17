# FIN 439 Project 2 final audit

Audited November 16, 2026 by OpenAI Codex. This audit uses new source retrieval, independent calculations and new tests, but it is still AI-assisted review in the same project session, not an external human audit. Student ownership and verification are not claimed.

## 1. Overall readiness

**Functionally tested research application; not submission-ready and not authorized for investment deployment.** Working components were preserved. Original Cedar mandate parameters, fund universe, benchmark configuration, proposed signal policy and frozen data were not changed. The default allocation and draft Reject recommendation remain unchanged.

Status meanings: **Fully verified** means the stated check was actually performed; **Implemented but not independently verified** means code/artifact exists but the relevant check was unavailable; **Incomplete** means required evidence or an audit source is absent; **Blocked by student action** means genuine authorship, judgment, recording, authorization or submission is required.

Eight core requirements: **4 Fully verified; 4 Blocked by student action**. Six submission-delivery requirements are also Blocked by student action. Two separate audit checks: browser visual inspection is Implemented but not independently verified; full rubric descriptor review is Incomplete due unavailable source. Thus 14 assignment/delivery checks comprise 4 complete and 10 student-blocked; these are not rubric subcriterion counts. See the requirements matrix for each item.

## 2. Verified completed requirements

The Python web app starts from the documented dependency setup. Six tabs expose the mandate, construction, portfolio alternatives, vintage signal, stresses and committee decision. Equal weight, inverse volatility and constrained minimum variance share one engine and constraint checker. Every alternative now displays a Pass/Fail authorization gate and the underlying failed or unknown rule. Four ordinary stress categories run. Opening AI-use and student-responsibility disclosures are present in the README, memo and all video scripts.

Fresh official assignment/checklist/architecture and Labs 13-17 were read. Project 2 excludes edition/research-evolution submission, retains the locked record, and requires YouTube videos/transcripts and Markdown attachments. Full rubric descriptors remain unavailable; syllabus category maxima total 300.

## 3. Incomplete and student-blocked requirements

Cedar's section H does not specify a numeric risk limit or its own benchmark. The inherited volatility objective and 60VT/40LQD comparator are labeled, not silently treated as approved. BIL's reserve-proxy acceptance, actual holdings/trades, costs and forward assumptions need review. The CPI fallback is technically supported by the historical source, but student source checks and admission are pending. The committee memo is a draft awaiting the student's judgment.

Git history contains development commits, no genuine student prediction commit. Prediction fields remain blank and `outputs/locked_changed_input.json` is absent. No locked run occurred. No personal GitHub remote, actual videos, corrected spoken transcripts or live manifest links exist. Brightspace attachments and access checks are not performed.

## 4. Independent financial findings

`python scripts/audit_finance.py` recalculates all portfolio and benchmark means, covariance and volatility using CSV data, scalar Python sums and sample denominator n-1, without calling the production estimator or NumPy covariance. Errors versus production are below 1e-12. `outputs/audit-independent-finance.json` preserves the results.

| Portfolio | Annual arithmetic mean estimate | Annual volatility | Financial mandate / authorization |
| --- | ---: | ---: | --- |
| Equal weight | 3.223698% | 7.498824% | Fail hurdle / Fail |
| Inverse volatility | 3.331902% | 1.395810% | Fail hurdle / Fail |
| Constrained | 5.500000% | 3.526988% | Not Known / Fail evidence gate |
| Benchmark | 6.814740% | 12.291532% | Comparator, not an approved client allocation |

The constrained weights remain 77.04% BIL and 22.96% VT. Manual examples check two successive 10% returns compound to 21%, a two-asset portfolio returns 6.8% with variance 0.010944 and volatility 10.461357%, and 20% one-way turnover at 50 bps per traded side costs 0.2% of assets. A 6% annual excess return over 20% annual volatility gives a proxy Sharpe of 0.3. Monthly means/covariance multiply by 12; volatility scales by square root of 12. No daily/monthly or percent/decimal error was found in the default calculations.

Source audit reconciles all 244 prices exactly and verifies 54 recovered-file hashes. A new ALFRED response matches all 957 frozen observations with zero numeric difference and identical SHA-256. This establishes historical-vintage source consistency, not the student's personal review or intraday publication times. Holdout data are still later-download adjusted prices, so the diagnostic is not a fully implementable PIT backtest. Arithmetic expected return does not establish the client's realized geometric real after-cost objective.

## 5. Tests and application smoke

- Baseline before changes: **31 passed, zero failed**, 4.55 seconds (`outputs/audit-baseline-tests.txt`).
- Final main suite: **65 passed, zero failed, 5.94 seconds** (`outputs/audit-tests.txt`).
- Fresh isolated environment installed from `requirements-lock.txt`; `pip check` found no broken requirements. Separate copied project passed **65 tests in 6.14 seconds** (`outputs/audit-clean-environment-tests.txt`).
- New server launched at `http://127.0.0.1:8521`; health returned **HTTP 200 / ok** (`outputs/audit-server-smoke.json`).
- AppTest exercises six tabs, window changes, infeasible position bounds, expected-return controls and missing-data error display. It confirms no uncaught app exception for those cases.
- Browser host was retried and unavailable. No visual rendering or actual browser interaction is claimed.

An intermediate test expected a single negative VT estimate to make the entire problem infeasible, but other funds were still assigned the exact hurdle. That was an incorrect test assumption, not a model error. The fixture now makes all expected returns negative and correctly observes infeasibility. Its failed output is retained in `outputs/audit-intermediate-test-failure.txt`.

Initial dependency retrieval was blocked by sandbox networking. Authorized retry installed all pinned packages. PowerShell marked pip's update notice on stderr as NativeCommandError after the successful installation; installed-package inspection, pip check and clean-environment tests confirmed the environment. Streamlit bare-mode context messages can arise in AppTest; obsolete width-argument warnings were corrected.

## 6. Corrections made and verified

| Finding | Correction | Verification |
| --- | --- | --- |
| Signal accepted a hostname substring and optional checksum | Require exact HTTPS ALFRED host, correct series/vintage query and checksum | Spoofed host, wrong series/date and missing hash rejected |
| Missing latest CPI could silently use older data; invalid values could propagate | Reject missing/nonpositive/nonfinite latest or prior-year input and post-cutoff dates | Five invalid-value/date fixtures plus valid 10% example |
| Current holdings could enter historical optimization | Remove present holdings from historical config | Holdout unchanged when current holdings change |
| One rebalance labeled as actual annual turnover compliance | Separate scenario approximation from unknown annual ledger requirement | Hypothetical zero trade cannot certify annual compliance |
| Fixed-bound optimizer result may omit iteration count | Read optional solver iteration metadata safely | Exactly fixed 25% weights accepted without crash |
| Empty/nonfinite estimation inputs lacked clear validation | Explicit nonempty-vector, covariance and missing-date validation | Empty data, missing/duplicate dates and invalid inverse-vol inputs rejected |
| Transaction-cost slider's effect obscured when actual holdings absent | Expose nonzero hypothetical transition costs at sidebar versus stress bps | Fivefold bps change produces fivefold cost |
| Locked gate froze prediction but not material model/input files | Verify clean material files and equality to prediction commit | Dirty or subsequently changed model rejected without executing experiment |
| Not Known compliance lacked a binary authorization answer | Add Pass/Fail evidence gate while preserving unknown financial rules | Unknown mandate blocks authorization without fabricated failed rule |
| Presentation/document drift | Update width API, disclosures first, transcript docs paths, benchmark differences and audit evidence | AppTest, regenerated outputs and document inspection |

## 7. Remaining bugs and limits

No unresolved calculation or app exception was observed in the executed test scope. This is not proof that every possible input is correct. A zero-volatility asset makes inverse volatility undefined and is rejected with an error rather than assigned fabricated weights. The app uses a fixed approved universe; unknown tickers are rejected, not downloaded. No live refresh or automated trading is implemented. Browser layout remains uninspected. Actual annual turnover requires a ledger. Provider adjustments, liquidity classifications and future objective attainment are assumptions/limitations, not newly verified economic facts.

## 8. Committee-member walkthrough

| Question | Answer available in the app/documents |
| --- | --- |
| Objective? | Cedar: CPI+3% after costs over rolling five years; quarterly scholarship spending |
| Assets? | Recovered BIL, IEF, LQD, VT; no new fund substitution |
| Benchmark? | Inherited 60% VT / 40% LQD, pending Cedar approval |
| Controlled risks? | Long-only/full investment, reserve and position bounds; scenario volatility/turnover; unknown actual policy clearly flagged |
| Why different portfolios? | Equal capital, inverse individual volatility, and constrained covariance-based variance minimization |
| Is the optimized portfolio preferable? | Meets illustrative hurdle at modeled minimum variance, but does not establish suitability or deployment approval |
| Signal contribution? | Historical CPI inflation can raise reserve floor to 5%; default candidate already exceeds it |
| Assumptions change? | Four ordinary stresses and editable controls reveal allocation/cost sensitivity |
| Failure causes? | Bad provenance, stale data, infeasibility, instability, missing policy evidence, realized purchasing-power shortfall |
| Committee decision? | Reject deployment now; resolve evidence and rerun before revisiting; not an instruction to liquidate existing assets |

## 9. Documentation and video readiness

Memo regenerated from actual outputs. README, data card, methodology, validation record, matrix and manifests were reconciled. Video scripts open with disclosures and match real files and figures. Video 1 leaves personal reflection to the student. Video 2 shows the actual code and tests. Video 3 starts with the app live. Limits remain 3/5/5 minutes. These are scripts, not recordings or transcripts. Corrected actual transcripts belong in `docs/transcript-video-1.txt` through `docs/transcript-video-3.txt`.

## 10. GitHub and submission readiness

Local Git history is preserved; only audit corrections are committed locally. No push, upload or submission. 132 historical Git blobs and current tracked content were scanned for common credential patterns and large files; results are in `outputs/audit-repository-scan.json`. No matches or tracked files over 5 MB were found at that scan. This heuristic is not a guarantee against every secret format. No personal remote or submitted URL can be validated. Runtime paths are relative; absolute recovery paths are provenance only. Exact CSV column order is retained from the prior template but not independently verified from accessible official sources; the documented required manifest fields and twelve legacy rows are present.

## 11. Grade estimate

See `project2-grade-audit.md`. Category maxima are verified: 45 + 45 + 60 + 45 + 75 + 30 = 300. **Earned total and percentage are pending**, because full performance descriptors and mandatory student artifacts are unavailable. No precise grade or item-specific deduction is invented. Passing software tests does not imply submission completion.

## 12. Prioritized remaining checklist

- [ ] Confirm/document missing mandate interpretations and approve or quarantine the proposed signal after personal source checks.
- [ ] Close AI, write the genuine prediction, commit and push it, then run the gated experiment with AI closed and reconcile honestly. Follow `docs/changed-input-record.md`; do not backdate anything.
- [ ] Review and own the final committee judgment; record actual personal verification.
- [ ] Obtain the full rubric and visually walk through the app; address any newly revealed issue.
- [ ] Record the three videos within limits, correct actual transcripts, upload to YouTube and verify access.
- [ ] Authorize GitHub publication, fill real manifest links/durations/timestamps, freeze the final revision, and attach the same decision/validation Markdown files to Brightspace yourself.
