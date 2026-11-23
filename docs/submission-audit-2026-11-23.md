# Project 2 submission audit — November 23, 2026

This is an AI-assisted check of the published Cedar Project 2 package against the [official Project 2 brief](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md) and [major-project checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md). It is not a grade. The optional [research-evolution reflection](research-evolution.md) is supplemental; Project 2 does not require a Research Evolution PDF or Editions A/B.

| Requirement | Status | Evidence and remaining limit |
| --- | --- | --- |
| Runnable Python web app and stranger instructions | **Verified** | [README](../README.md), [app](../app.py), [Aidan's cold run](andrew-cold-run-by-aidan.md). A fresh clone of the preceding published code revision passed 67 tests; Aidan's independent cold run was on an earlier November 17 revision. |
| Mandate with objective, universe, benchmark, risk measure and limits | **Verified as a research mandate; Cedar approvals unverified** | [Configuration](../config/mandate.json), [decision memo](decision-memo.md). Cedar's numerical volatility limit, reserve treatment and current holdings are not supplied. The app reports these as unknown rather than inventing them. |
| Two baselines and constrained candidate with rule verdicts | **Verified** | [Visible results](checkout-results.md) and [engine](../src/engine.py). The candidate is 77.04% BIL / 22.96% VT, 5.50% estimated return and 3.53% volatility. Equal weight and inverse volatility miss the return screen. |
| Point-in-time signal with data card | **Verified for the coursework research process; policy approval unverified** | [Data card](signal-data-card.md), stored vintage and [signal code](../src/signal.py). The student-reported three-value spot check supports about 3.72% historical CPI; it does not establish that Cedar approved the reserve-floor rule. |
| Stress on estimates, window, costs and constraints; stop condition | **Verified** | [Stress results](checkout-results.md), [workflow](../src/workflow.py). Actual transition costs cannot be computed without Cedar's holdings. |
| Locked changed-input record | **Verified in repository chronology and saved result; AI-off authorship is student-attested** | [Prediction and reconciliation](changed-input-record.md), [saved result](../outputs/locked_changed_input.json). The 85% BIL floor produced no feasible portfolio; 0% new-capital recommendation stayed. |
| Recommendation with range, triggers and committee ask | **Verified as stated student judgment** | [Decision memo](decision-memo.md) and [Video 3 transcript](transcript-video-3.txt): reject deployment, 0% new capital, leave existing holdings, seek approved limits and implementation evidence before a pilot. |
| AI-use and education statements | **Verified with student-reported instructor clarification** | [README](../README.md), [memo](decision-memo.md) and all three transcripts contain the statements. Videos 1 and 2 speak the AI-use and student-responsibility disclosure; their education disclaimer is written at the top of each transcript and explicitly labeled as not spoken. Video 3 also speaks it. Andrew reports that his professor clarified spoken repetition is unnecessary. The published Project 2 brief still says the two statements open each video; this oral clarification has not been independently documented. |
| Three YouTube links, lengths and transcripts | **Verified** | [Manifest](submission-manifest.csv) lists 2:44, 4:25 and replacement Video 3 at 4:46, all within 3/5/5-minute limits. The student confirmed links and transcripts. English automatic captions are available; automatic text can still mishear finance terms, so the repository transcripts are the corrected record. |
| Written attachments and Brightspace receipt | **Not yet verified** | [Decision memo](decision-memo.md) and [validation record](validation-and-ai-use.md) are present on GitHub; only the student can confirm what Brightspace received. |

## Checks run

- `python -m pytest -q --basetemp outputs/pytest-submission-1123 -o cache_dir=outputs/pytest-cache`: **67 passed** on the working tree.
- `scripts/audit_sources.py`: **244 adjusted prices reconciled** to stored raw responses and **54 recovered files verified**.
- `scripts/audit_finance.py`: independent scalar calculation reproduced the constrained **5.50%** annual mean and **3.53%** volatility from 60 monthly returns; weight sum was 100% within floating-point precision.
- `docs/submission-manifest.csv`: 12 rows, nine consistent columns. All local links in the optional research-evolution page resolve.

## Before submitting

Andrew reports that his professor accepts the education disclaimer in writing at the top of each transcript, so this audit no longer calls for re-recording Videos 1 and 2. The transcript labels preserve what was and was not spoken. After reviewing the optional reflection, decision memo and validation record, attach the two required Markdown files in Brightspace, provide the manifest and transcript links/files, and retain the receipt.
