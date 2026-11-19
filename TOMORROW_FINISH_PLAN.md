# Finish Project 2 tomorrow

**Tomorrow: November 19, 2026.** The technical app is running and was tested from a clean copy. The remaining work is mainly your genuine review, partner evidence, three recordings, and submission. This page is a work order, not a claim that those steps are done.

## Open the app in one step

Download the entire [GitHub repository](https://github.com/AndrewK6637/fin439-project2) as a ZIP, extract it to a short path such as `C:\fin439`, and double-click **`OPEN_APP.cmd`**. The first run creates `.venv` and installs pinned packages; later runs start the app directly. Keep the black terminal window open. If the browser does not open, use the Local URL printed in it. You need Python 3.13 and internet for the first installation. [README](README.md) has the manual command and troubleshooting.

## Priority 1 — protect the graded AI-off chronology

Do this **before** a changed-input run. Close AI tools. Read [the Lab 20 student checklist](WHAT_I_NEED_TO_DO.md) and [the blank record](docs/tuesday-changed-input-template.md). Choose your own input, write a specific prediction and reasoning with units, then commit and push the prediction. Check that the prediction appears on GitHub. Only then run the app with default, one changed input, and restored default; save three differently named scenario JSON files. Fill the actual-results and reconciliation fields and make a later evidence commit. Existing stress tables are not this exercise. This is the highest-priority sequencing risk because a prediction written after the run cannot be made genuine retroactively.

## Priority 2 — make the analysis yours

Read [the simple explanation](PROJECT_2_SIMPLE_EXPLANATION.md), [actual results](docs/checkout-results.md), [decision memo](docs/decision-memo.md), and [signal data card](docs/signal-data-card.md). In your own words, decide whether the draft **Reject deployment / 0% new allocation** is your recommendation and what evidence would change it. Check three CPI observations and the vintage yourself. If Cedar's real risk limit, reserve approval, benchmark approval, holdings, trades, or costs are unavailable, say **Not Known**; do not fill gaps with assumptions. The 5.50% return and 3.53% volatility are historical arithmetic estimates, not proof of Cedar's rolling real-return objective. Revise the memo only where your review supports a change.

Your individual improvements are the **reasoning** behind your final recommendation, your own explanation of the window/assumption sensitivity, an independent source check, and your response to a partner's question. The software can show numbers; it cannot establish your judgment or experience.

## Priority 3 — get the real partner and code-defense evidence

Send your partner **only [the README GitHub link](https://github.com/AndrewK6637/fin439-project2/blob/main/README.md)**. Have them download, install, launch, locate the decision and move a control without coaching. Ask them to complete [the cold-run record](docs/partner-cold-run-template.md) with their actual first failure or “none,” timing, and observation. Swap roles. Then explain `src/engine.py` and `src/workflow.py` without AI for six minutes, answer their real question, and complete [the studio record](docs/tuesday-studio-record.md). If the partner finds a defect, fix and retest it before the videos.

## Priority 4 — record and submit

Use [the recording checklist](videos/recording-checklist.md) and [video scripts](videos/) as prompts. Record three actual videos: 1 <=3:00, 2 <=5:00, 3 <=5:00. Open each with the required AI-use and student-responsibility statements. Video 3 must begin with the live app already on screen. Correct the actual captions and save three real transcripts under `docs/`; do not submit scripts as transcripts. Upload to YouTube and verify the links. Complete [the manifest](docs/submission-manifest.csv) with real URLs, durations, timestamps, access checks, and final commit. Attach both `docs/decision-memo.md` and `docs/validation-and-ai-use.md` to Brightspace, add the required links, and check the receipt. Use [the full submission checklist](FINAL_SUBMISSION_CHECKLIST.md) for every file.

## What is already technically checked

A new Python 3.13 environment in a clean folder installed `requirements-lock.txt`, passed `pip check` and **66 tests**, started Streamlit, and returned HTTP 200. Independent finance and source audits reconciled the saved results. `OPEN_APP.cmd` is an easier entry point; it does not replace the required partner cold run or your own browser review.

**Stop point:** do not mark the project submission-ready until the prediction chronology, partner record, your reviewed recommendation, three videos and transcripts, manifest, and Brightspace attachments are real and checked.
