# FIN 439 Project 2 final submission checklist

**Current delivery status (November 21): start with the [submission review](SUBMISSION_REVIEW.md). On Windows, double-click `OPEN_APP.cmd` in the extracted project folder to launch the app.**

**Historical checklist:** the sections below describe the November 18 preparation stage. The three videos, transcripts, partner cold run, and locked experiment have since been recorded. Use the [submission review](SUBMISSION_REVIEW.md) for current open actions. OpenAI Codex assisted with code, tests, source checks, and drafts. The student owns the analysis and final decision. Educational work, not investment advice.

## Completed and checked

- [x] Read the preserved Project 2 assignment, major-project checklist, submission architecture, Labs 13–17, Lab 20 instructions, README, requirements matrix, and prior audits. Full analytic rubric descriptors were unavailable; the syllabus category weights were verified, but no score is claimed.
- [x] Six-tab Streamlit research app, three portfolio choices, shared mandate checks, point-in-time CPI fallback, four ordinary stresses, stop rules, scenario controls, and downloadable results are present.
- [x] README gives clean Windows Python 3.13 installation and run commands. An earlier public-clone check reported pinned install, 66 tests, and HTTP 200. This session reran 66 tests successfully with a project-local pytest temp path.
- [x] Independent scalar finance audit reconciled annual means, variance, volatility, and weight sums for all portfolios and benchmark. Source audit matched all 244 processed adjusted prices to the four stored raw source responses; 54 recovered file hashes verified.
- [x] Default output and memo agree on the constrained research weights (77.04% BIL, 22.96% VT), estimated return (5.50%), volatility (3.53%), and **draft** rejection of deployment.
- [x] [Plain-English explanation](PROJECT_2_SIMPLE_EXPLANATION.md) and this checklist added. Existing code and model were preserved.

The first test command in this session failed 19 test setups because the Windows global pytest temp directory denied access. Running `pytest -q --basetemp outputs\pytest-current -o cache_dir=outputs\pytest-cache` passed **66/66**. This is an environment permission issue, not a model failure. A real browser visual inspection was not completed in this session; earlier server and AppTest checks do not prove visual layout.

## Unresolved financial evidence and your decisions

- [ ] Read [the simple explanation](PROJECT_2_SIMPLE_EXPLANATION.md), [results](docs/checkout-results.md), and [draft decision memo](docs/decision-memo.md). Confirm or change the **Reject deployment / 0% new allocation** judgment in your own words. Do not call the draft your personal conclusion until you have reviewed it.
- [ ] Check whether Cedar has a documented numerical risk limit, benchmark approval, acceptance of BIL for the $600,000 reserve, current holdings, trade ledger, and cost schedule. If no evidence exists, leave each item **Not Known** and keep deployment unauthorized.
- [ ] Personally verify three dated CPIAUCSL observations and the November 1, 2026 ALFRED vintage using [the signal data card](docs/signal-data-card.md). Decide whether to adopt or reject the proposed fallback policy. The technical bytes were checked; your personal check remains open.
- [ ] Review the illustrative 2.5% CPI, zero additional annual-cost input, historical mean estimates, and real rolling five-year objective. Keep their different meanings explicit.
- [ ] Obtain the full rubric from Brightspace or the professor if available. The accessible official repository did not provide its performance descriptors.

## Mandatory Lab 20 actions only you and your partner can perform

- [ ] Partner receives **only the README link**, clones or downloads independently, follows it, and writes the real failure or “none” and timing in [the partner record](docs/partner-cold-run-template.md). Swap roles.
- [ ] With AI closed, write your own changed-input prediction with old/new values and units in [the blank record](docs/tuesday-changed-input-template.md). Commit and push that prediction **before** running the changed case. Then run default, changed, and restored inputs; save actual JSON outputs and explain any difference. Do not present the four existing stress runs as this exercise.
- [ ] Explain the real code for six minutes without AI, answer a partner question, and record what you could not explain in [the studio record](docs/tuesday-studio-record.md).
- [ ] Write your one-line committee action, reversal condition, and real partner cold-run finding. Submit the Lab 20 links through the course route.

## Project 2 delivery files and locations

| Item | File or location | State |
| --- | --- | --- |
| Public repository and working app | [GitHub project](https://github.com/AndrewK6637/fin439-project2), [README](README.md), `app.py`, `src/`, `config/`, `data/` | Published; final revision and grader access still need your check |
| Visible result | [results](docs/checkout-results.md), `outputs/results.json` | Present |
| Decision Markdown | [decision memo](docs/decision-memo.md) | Draft; review, then attach this actual file to Brightspace |
| Validation and AI-use Markdown | [validation](docs/validation-and-ai-use.md) | Present; update after genuine locked record, then attach this actual file |
| Locked changed-input record | [record](docs/changed-input-record.md), [classroom template](docs/tuesday-changed-input-template.md) | Student prediction, GitHub chronology, and result missing |
| Video 1, <=3:00, with corrected transcript | [recording](https://youtu.be/P-bziTgmBHY), [transcript](docs/transcript-video-1.txt) | 2:44; student transcript review pending |
| Video 2, <=5:00, with corrected transcript | [recording](https://youtu.be/JV2xpzFfczE), [transcript](docs/transcript-video-2.txt) | 4:25; student transcript review and captions pending |
| Video 3, <=5:00, with corrected transcript | [replacement recording](https://youtu.be/UfHrL-9ilAM), [transcript](docs/transcript-video-3.txt) | 4:46; student transcript review and captions pending |
| Submission manifest | [CSV](docs/submission-manifest.csv), [guide](docs/submission-manifest.md) | URLs, durations, and timestamps entered; final viewer check and frozen commit ID pending |

## Recording guide

1. Run `.venv\Scripts\python.exe -m streamlit run app.py` from this project folder. Verify the live page and reset controls to the 60-month default. Open each video with the required AI-use and student-responsibility/education disclosure from its script.
2. **Video 1 (<=3:00):** show README, the recovered mandate/source trail, and one specific AI-assisted output you actually checked. Explain how your own thinking changed only if that is true for you. Use [video 1 script](videos/video-1-script.md) as a prompt, not a transcript.
3. **Video 2 (<=5:00):** show `src/engine.py`, `src/workflow.py`, a test, and the terminal result. Explain `price ratio - 1`, `12 × monthly mean`, `12 × sample covariance`, weighted return, and portfolio volatility. Point out how missing mandate evidence fails authorization without inventing a numerical breach.
4. **Video 3 (<=5:00):** start with the **app already running**. Show Executive dashboard, Portfolio comparison, the 60-to-36-month sidebar change, Stress testing, and Committee recommendation. Say that the default research candidate is 77.04% BIL / 22.96% VT, 5.50% estimated annual arithmetic return, 3.53% volatility; 36 months changes the weights to 92.86% / 7.14%. Explain your personally confirmed decision and reversal condition. Restore 60 months before ending.
5. Record actual spoken words, upload all three videos, correct YouTube captions/transcripts, save the three real transcript files, and put working URLs, measured durations, timestamps, access checks, and final commit ID in the manifest. Check links while logged out where practical. Attach the memo and validation Markdown files to Brightspace and confirm the submission receipt.

The [student action checklist](WHAT_I_NEED_TO_DO.md) has the detailed Lab 20 command sequence. No partner work, student AI-off prediction, recording, personal source check, final judgment, or Brightspace submission is claimed here.
