# Requirements matrix

Official sources: [Project 2 assignment](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md), [student checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md), and [shared submission architecture](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/PROJECT-SUBMISSION-ARCHITECTURE.md). Downloaded copies are in `references/`. Requirement wording below is a faithful concise transcription, not invented scoring descriptors. Base items have no individually verified point allocation.

| Requirement | Feature/file | Evidence | Status | Source / points |
| --- | --- | --- | --- | --- |
| Runnable stranger-operated application | app.py; README.md | Streamlit AppTest, server health, portable-copy test | Implemented | Project 2 assignment; individual points not specified |
| Lab 13 mandate: objective, universe, benchmark, risk measure/limits | config/mandate.json; docs/methodology.md | Recovered Lab13/15 comparison, rule tests | Implemented; numeric limit and approvals unknown | Project 2 assignment; individual points not specified |
| Equal weight and transparent second baseline plus constrained portfolio; same mandate verdicts | src/engine.py; src/workflow.py | Known-answer variance, inverse-vol, feasibility and rule tests | Implemented | Project 2 assignment; individual points not specified |
| At least one point-in-time signal and data card | src/signal.py; docs/signal-data-card.md | ALFRED vintage hash, cutoff and transformation tests | Implemented proposed fallback; student review pending | Project 2 assignment; individual points not specified |
| Stress estimates, window, costs and constraints; process stop condition | src/workflow.py; app.py | Four executed scenarios and stop tests | Implemented | Project 2 assignment; individual points not specified |
| Locked AI-off prediction committed to GitHub before AI-off changed-input run | docs/changed-input-record.md; scripts/locked_experiment.py | Blank-prediction gate test; no experiment output | STUDENT ACTION REQUIRED | Project 2 assignment; individual points not specified |
| Committee recommendation, allocation range, triggers | docs/decision-memo.md; app.py | Actual outputs/results.json; Reject until unknowns cleared | Draft; student judgment pending | Project 2 assignment; individual points not specified |
| Opening AI and responsibility/education disclosures | README.md; docs/decision-memo.md; videos/ | Text inspection; student review explicitly pending | Prepared | Project 2 assignment; individual points not specified |
| Repository, environment, runnable source, visible output | requirements-lock.txt; outputs/visible-results.md | Tests and source audit; local Git history | Local complete; publication/access pending | Student checklist / shared architecture; individual points not specified |
| Decision and validation Markdown in docs and attached to Brightspace | docs/decision-memo.md; docs/validation-and-ai-use.md | Files prepared | Attachments/student submission pending | Student checklist / shared architecture; individual points not specified |
| Video 1 <=3 minutes and corrected transcript | videos/video-1-script.md | Timed script; no recording claimed | STUDENT ACTION REQUIRED | Student checklist / shared architecture; individual points not specified |
| Video 2 <=5 minutes and corrected transcript | videos/video-2-script.md | Timed script; no recording claimed | STUDENT ACTION REQUIRED | Student checklist / shared architecture; individual points not specified |
| Video 3 <=5 minutes; opens with live app; corrected transcript | videos/video-3-script.md | Live-demo instructions; no recording claimed | STUDENT ACTION REQUIRED | Student checklist / shared architecture; individual points not specified |
| Manifest stable links, durations, indices, access checks and frozen state | docs/submission-manifest.md; docs/submission-manifest.csv | 12-row legacy schema; placeholders clearly empty | STUDENT ACTION REQUIRED | Student checklist / shared architecture; individual points not specified |
| Cold check, accessible repository/videos, corrected finance captions, no secrets | docs/validation-and-ai-use.md; videos/recording-checklist.md | Local cold-run validation; external access not performed | External access checks pending | Student checklist / shared architecture; individual points not specified |
| Edition A/B and research-evolution excluded for Project 2 | references/projects/major-project-student-checklist.md | Explicit Project 2 owner ruling | Not applicable | Student checklist / shared architecture; individual points not specified |

## Verified 300-point categories

The full `MAJOR-PROJECT-ANALYTIC-RUBRIC.md` was referenced but absent from the public tree and returned 404. Detailed level descriptors cannot be verified. Syllabus weights are verified in `references/syllabus/FIN43900-Fall2026-syllabus.pdf` and extracted `references/syllabus.txt`. Points below are weight times 300, not a self-awarded score.

| Category | Weight | Points | Evidence / remaining weakness |
| --- | --- | --- | --- |
| Problem definition and usefulness | 15% | 45 | Authentic Cedar mandate; missing client approvals remain explicit |
| Data integrity | 15% | 45 | Raw-source reconciliation, hashes, vintage cutoff; student source checks pending |
| Financial soundness | 20% | 60 | Annualization, constraints, known answers; objective forecast and actual turnover unverified |
| Technical execution | 15% | 45 | Six-tab app, shared workflow, numerical optimizer, tests |
| Validation, sensitivity and reproducibility | 25% | 75 | Four stresses, portable run, holdout limitations; locked record incomplete |
| Communication | 10% | 30 | Draft memo, scripts and manifest; recordings/transcripts/links pending |
| Total | 100% | 300 | No grade estimate claimed |
