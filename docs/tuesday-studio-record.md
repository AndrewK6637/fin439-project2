# Tuesday studio record — documented evidence and open student statements

Official sources: [Week 12 studio](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-12/student-handout.md) and [Week 13 Lab 20](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md). Week 12 was ungraded preparation; **Lab 20 is a separate 25-or-0 Tuesday completion checkout**. Aidan's later Cedar cold-run note, Andrew's separate review of Aidan's app, and the completed locked reserve experiment are linked below. The table in section 1 remains unverified as a pre-run AI-off statement because no dated record of one was supplied.

## 1. Before the partner run ? AI closed

Write your own committee decision and the one claim most likely to reverse it. The project memo contains an AI-assisted draft; copying it is not evidence that you authored this required statement without AI.

| Field | Student entry |
| --- | --- |
| Date/time | No dated pre-run AI-off statement was supplied. |
| My AI-off committee decision | Not recorded here; the later committee recommendation is Reject deployment and 0% new capital in the [decision memo](decision-memo.md). |
| The single claim most likely to reverse it | Not recorded before the partner run. The later memo identifies missing Cedar risk, reserve, holdings and cost evidence as conditions for reconsideration. |
| My reason | No contemporaneous AI-off explanation was supplied; do not present a later draft as one. |

### Current student committee reflection — November 19, 2026

The following statement was supplied by Andrew in the current conversation. It is a later reflection, not a claim that these words were recorded before Aidan's cold run:

> I’d recommend that Cedar commit 0% of its new capital to the strategy right now and leave its existing holdings in place. I’m skeptical of how clean the result looks. The optimizer was told to find a low-volatility mix that clears a 5.50% return hurdle, and it found one that lands right on 5.50%. That tells me the model found a solution under its assumptions. It also means even a small trading cost or a slightly lower return estimate could put the portfolio below the hurdle.
>
> The one piece of evidence most likely to change my decision is Cedar’s approved volatility limit. The app estimates volatility at 3.53%, but calling that low doesn’t tell me whether it’s low enough for a foundation that needs to fund scholarships every quarter. If 3.53% is close to or above Cedar’s limit, I’d keep the recommendation at 0%. If it’s comfortably below the limit, I’d be more open to considering a small pilot once we can verify the trading costs and check how much room the portfolio has above the return hurdle after those costs.

## 2. Partner run

Aidan's [full Cedar cold-run record](andrew-cold-run-by-aidan.md) reports a November 17 macOS/Python 3.14 clone, install and launch from the README without help from Andrew. He reproduced Reject, 5.50% estimated annual return and 3.53% volatility. An accidental two-line paste caused the first terminal error; rerunning commands separately worked. The browser remained blank for about 1–2 minutes before loading without an app error. Aidan changed no input. He disclosed Claude guidance for general Terminal use and did not supply an exact commit SHA. His note covers the then-current `main`, not later app edits.

### My later check of my partner's app (student-reported; not the original Lab 20 cold run of my repository)

- **Start and duration:** November 19, 2026, 9:40 EST; approximately 15 minutes (date confirmed by Aidan's email).
- **Partner repository:** [Project 2 on the `lab-20-readiness` branch](https://github.com/aidanklebenow/VISA-Research-NEW/tree/lab-20-readiness/Project-2). The README's first “Reproduce the decision” command, `python3 Project-2/model.py`, failed from the repository root on Windows: “Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.” The installed Python 3.14 launcher command, `py -3.14 Project-2/model.py`, succeeded.
- **Decision found:** Keep the portfolio for research and hold off on investing client money. The best candidate was 55% SGOV, 30% VTI, and 15% VXUS. It was the only portfolio that passed the model's checks: 7.5% estimated annual return and 6.8% estimated volatility against a proposed 10% limit. The two other portfolios fell short of the return target.
- **Reason to hold off:** Client risk limits and withdrawal schedule still needed verification. Application of the 7% issuer limit to holdings inside funds and to Treasuries needed clarification.
- **Input I changed:** Annual return target from 7.5% to 10%. The app shifted toward U.S. stocks and away from short-term Treasuries. Modeled return became 10.01%; estimated volatility rose from 6.80% to 10.84%, exceeding the 10% proposed limit. The displayed candidate went from passing to failing.
- **Question I asked:** “When I raised the return target to 10%, why did the app show a portfolio that exceeded the 10% volatility limit? How does the code decide what to show when it can't find a portfolio that meets both targets?” **Aidan answered by email:** his app displays the lowest-volatility mix meeting the return target and SGOV reserve, then marks it FAIL when it breaches the separate 10% volatility limit. At a 10% target, that mix had 10.84% volatility. If no mix reaches the return target, his app shows two comparison portfolios and STOP. See [my partner-project review](my-check-of-partners-project2.md).
- **Method note:** Student reported using Codex for much of the GitHub app-opening process. This was an AI-assisted partner-app check, not an AI-off exercise.

## 3. Challenge one risky claim

After identifying your own risky claim, request/choose one concrete test, check the result yourself, and repair, qualify or drop the claim. Existing candidate tests are listed in the study guide; their prior agent pass does not prove you personally checked them.

| Field | Student entry |
| --- | --- |
| My risky claim | The later locked prediction questioned whether an 85% BIL minimum could still meet the 5.50% illustrative return hurdle; see the [student prediction](changed-input-record.md). This was not documented as the pre-partner-run risky claim in section 1. |
| Test chosen and why it addresses that claim | The separate locked run changed only the analytical BIL floor from 3% to 85% and tested whether the solver could meet the hurdle; the [saved before/after result](../outputs/locked_changed_input.json) identifies the prediction commit checked before execution. |
| Command I personally ran | Exact terminal command and time of personal execution were not recorded in this studio note. The result file records the prediction commit; only Andrew can attest to the run method. |
| Actual result/evidence path | [Locked result](../outputs/locked_changed_input.json): baseline feasible with 77.04% BIL / 22.96% VT, 5.50% annual mean and 3.53% volatility; 85% floor produced no feasible constrained portfolio. |
| Repair / qualify / drop / retain, and reason | The later [student reconciliation](changed-input-record.md) retained the prediction that the 85% floor would be infeasible and the 0% new-capital recommendation. It could not compare after-run volatility because no feasible portfolio was returned. |
| Partner question and my response | Andrew asked Aidan why his 10% target case showed FAIL; [Aidan's emailed answer](my-check-of-partners-project2.md) is recorded. A separate question from Aidan about Cedar code, and Andrew's line-by-line response, have not been recorded. |

## 4. Freeze the must-fix list ? no new analysis

| Priority | Issue actually observed | Owner | Fix/evidence required | Status |
| --- | --- | --- | --- | --- |
| 1 | Aidan observed a blank white page for about 1–2 minutes on first load, then a successful dashboard | Andrew | Add a first-load note to the README and keep the partner observation | Documented locally in [README](../README.md); publish after review |
| 2 | The completed partner and locked records were still described as missing in current-facing pages | Andrew | Link the genuine records and correct status wording without changing historical evidence | Updated locally; publish after review |
| 3 | Actual Cedar risk limit, holdings/trading costs and BIL reserve approval remain unknown | Cedar / committee | Obtain written mandate and implementation evidence before any new allocation | Open; 0% new capital remains the recommendation |
| 4 | Videos, actual transcripts, manifest links and Brightspace receipt are absent | Andrew | Record, upload, verify access and submit | Open |

**Reflection from the recorded evidence:** Aidan reached the decision but reported that the initial blank screen could make a new user think the app had failed. His first command error was a paste mistake, not a broken README command. Andrew previously wrote that a working app also needs organized files and reproducible instructions. The remaining pre-deadline work is documentation and delivery; no new financial assumption is needed to explain this cold run.

The project repository is published at [AndrewK6637/fin439-project2](https://github.com/AndrewK6637/fin439-project2). [Aidan's Cedar cold run](andrew-cold-run-by-aidan.md) and the [locked record](changed-input-record.md) are now documented. Aidan changed no input during his cold run; Lab 20 assigns the changed-input test to a separate student step. Videos/transcripts and final submission links remain unresolved.
