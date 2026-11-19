# FIN 439 Project 2 Student Checklist

Start here. The app and public GitHub repository are working, but the Lab 20 evidence and final submission are incomplete. Check a box only after you actually finish that step. The [final audit](FINAL_PROJECT_2_AUDIT.md) explains what was tested and what is still unknown.

## First review your decision

- [ ] **Read the results.** Open [checkout-results.md](docs/checkout-results.md). Be able to explain Cedar's $20 million scholarship objective, the four funds, the three portfolios, and why the current draft says **Reject deployment**.
- [x] **State your coursework design choices.** You chose to keep BIL/IEF/LQD/VT, use 60% VT/40% LQD as a comparison, use BIL as an illustrative reserve stand-in and keep the proposed CPI fallback. These choices are documented in [the assumption guide](docs/student-assumptions-and-actions.md). Cedar approval, the numeric risk limit, real costs and actual holdings remain unknown.
- [ ] **Review the short assumption guide.** [This page](docs/student-assumptions-and-actions.md) separates what you previously told AI, what the model assumes, and what only you or your partner can complete. Correct any statement that does not reflect your view.
- [x] **Verify the CPI source values.** On November 19 you reported finding three dated observations in the linked ALFRED vintage CSV and independently calculated 0.037173 (about 3.7173%). Your report is recorded in [the signal data card](docs/signal-data-card.md). This does not establish Cedar approval of the signal policy.
- [ ] **Finish your committee reasoning.** You said the research strategy is good but agreed with **Reject deployment for now**. Read [the draft memo](docs/decision-memo.md) and state in your own words why the missing evidence blocks deployment and what would reverse the decision. Keep its numbers consistent with [the results](docs/checkout-results.md).

## Complete the graded Lab 20 checkout

The [official Lab 20 page](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md) calls this a **25-or-0 completion checkout**. It requires genuine student and partner evidence. The Week 12 studio was separate preparation.

- [x] **Link Aidan's cold-run evidence.** [His full record](docs/andrew-cold-run-by-aidan.md) documents a successful README-based macOS/Python 3.14 launch and baseline decision. It preserves his paste error, 1–2 minute blank screen, Claude assistance, and statement that he changed no inputs. [My separate check of his app](docs/my-check-of-partners-project2.md) includes his emailed answer.
  Aidan changed no input during this cold run. The [official Lab 20 instructions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md) put the changed-input test in a separate student step; his no-input cold run still documents the required README-to-result check.
- [ ] **Make an AI-off changed-input prediction before the changed run.** Close AI tools. Choose one input yourself. In [the blank classroom record](docs/tuesday-changed-input-template.md), write the old and new value **with units**, expected direction of important numbers, expected effect on the decision, and your finance reasoning. Do not copy the AI-assisted prediction discussion from this chat and label it AI-off. The earlier cost and reserve examples were discussed with AI; choose and justify your own genuine test, and ask the instructor how to handle prior AI discussion if needed. Leave the actual-results section blank.
- [ ] **Commit and push the prediction before running.** From the project folder in VS Code Terminal, with AI still closed, run:

  ```powershell
  git status --short
  git add docs/tuesday-changed-input-template.md
  git commit -m "Record my AI-off prediction before Lab 20 run"
  git push origin main
  git rev-parse HEAD
  ```

  Save the real commit hash and GitHub commit link in the record. Confirm the prediction is visible on GitHub **before** changing the app input. If Git reports a conflict or uncommitted code/data changes, stop and resolve that before the experiment; do not claim the chronology if it was not preserved.
- [ ] **Run and reconcile, still with AI closed.** Start the app with the README command. Record and download the default scenario. Change **only the input and value you personally predicted**; download the changed scenario with a different name. Restore the original value and verify the original result returns. Keep the three JSON files in `outputs/` and fill the record's actual-results table. Explain whether the decision changed and why the results matched or differed from your prediction. Preserve the prediction text unchanged. Commit and push the completed record and output files afterward. Link the completed record in [validation-and-ai-use.md](docs/validation-and-ai-use.md). Do not run the separate reserve experiment merely to fill a second record.
- [ ] **Explain the code without AI for six minutes.** Open [the code study guide](docs/code-explanation-study-guide.md), then `src/engine.py` and `src/workflow.py`. Explain how return, covariance, weights, constraints, and the authorization gate produce the displayed decision. Answer one question your partner asks from the actual code, swap roles, and record what you could not explain in [the studio record](docs/tuesday-studio-record.md).
- [ ] **Finish the Lab 20 decision line and fix record.** In [the studio record](docs/tuesday-studio-record.md), write your own one-line action and the condition that would reverse it. Record your partner's first failure and fix, or a clean run with no fix needed. Record what you learned from the cold run and what you will leave alone before the deadline. Submit the required GitHub file links for the checkout through the course's Lab 20 submission route.

## Finish Project 2 submission

- [ ] **Personally check the final package.** Run the app again and compare the README, [results](docs/checkout-results.md), [memo](docs/decision-memo.md), and [validation document](docs/validation-and-ai-use.md). Confirm that each uses the same data date, numbers, decision, and reversal condition. Do not claim client approval or student verification that did not happen.
- [ ] **Check attribution before recording and submitting.** Confirm the videos, [partner evidence](docs/andrew-cold-run-by-aidan.md), and [AI-use disclosure](docs/validation-and-ai-use.md) accurately distinguish Aidan's README-only run with Claude terminal guidance, my AI-assisted review of his app, my locked 85% BIL experiment, and automated agent tests. Aidan changed no input in his Cedar run.
- [ ] **Record three videos.** Use the scripts in [videos](videos/recording-checklist.md), then speak in your own words. Video 1 (at most **3:00**) explains how the system and your thinking changed and one AI output you checked. Video 2 (at most **5:00**) walks through the actual code and a test. Video 3 (at most **5:00**) opens with the **app already running** and gives the committee recommendation. Begin each with the required AI-use and student-responsibility/education disclosures. Upload to YouTube; verify each link.
- [ ] **Correct actual transcripts.** Enable YouTube transcripts/captions, correct the spoken finance terms and numbers, and save the real transcripts as `docs/transcript-video-1.txt`, `docs/transcript-video-2.txt`, and `docs/transcript-video-3.txt`. Do not submit the scripts as transcripts. Commit and push these files.
- [ ] **Complete the manifest.** Fill [submission-manifest.csv](docs/submission-manifest.csv) with the three real YouTube URLs, transcript GitHub links, measured durations, timestamp indices, access checks and final commit ID. Check the links in a logged-out browser where applicable. Do not invent links or access checks.
- [ ] **Submit on Brightspace.** Follow the assignment header for the exact deadline. Submit the public GitHub repository, the decision memo and validation GitHub links, the three YouTube links with transcripts, and the completed manifest. **Attach the actual `docs/decision-memo.md` and `docs/validation-and-ai-use.md` files to Brightspace too.** Confirm the submission receipt yourself. Project 2 does not require Edition A/B or a research-evolution PDF.

## Commands to find and run your app

In VS Code, open the `fin439_project2_investment_management` folder. In Terminal:

```powershell
.venv\Scripts\python.exe -m streamlit run app.py
```

Open the Local URL printed by Streamlit. If you download a fresh copy instead, follow [README.md](README.md) to create `.venv` and install dependencies first. Your partner must use their own copy and environment.
