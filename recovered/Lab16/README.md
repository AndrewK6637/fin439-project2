# FIN 43900 — Lab 16: Provenance Gate

This project is for educational and research purposes only.

Start with [SUBMISSION.md](SUBMISSION.md), the completed technical report and final checklist.
Fill only the clearly marked student fields there and in [LAB16_REFLECTION.md](LAB16_REFLECTION.md).
Run `python prepare_submission.py` after edits to refresh `../Lab16_Submission.zip`.
The ZIP contains only the nine listed deliverable files, without caches or previous labs.

Tuesday's 12-row training-table exercise, using Python standard library only.
No market downloads, packages, or Thursday ALFRED project are required.
Edit `DECISION_DATE` and `TRAINING_TABLE` at the top of `asof.py`.
Original row IDs must remain unique integers; dates use YYYY-MM-DD and months YYYY-MM.

From this folder:

```powershell
python asof.py
python -m unittest -v test_asof.py
```

## Rules and verified answers

Apply in order: quarantine missing/blank tickers; remove exact data-field duplicates
(ignoring row IDs); exclude publication dates strictly after the decision date;
select the latest available publication for each ticker/month. Lowest original ID
wins duplicates and tied publication dates. Inputs are not mutated.

| Rule | Before -> after | Original rows removed |
|---|---|---|
| 1 | 12 -> 11 | 11 |
| 2 | 11 -> 10 | 7 |
| 3 | 10 -> 7 | 3, 8, 10 |
| 4 | 7 -> 6 | 2 |

March 31 panel: **1, 4, 5, 6, 9, 12**, sorted by ticker/month.

Signal = `(latest available month price / previous available month price - 1) * 100`.
This is the fund's return measured as the percentage change in price. Missing history or
a zero denominator prints N/A. Rounding occurs only for display.

| Ticker | As-of | Latest month | Naive | Latest month |
|---|---:|---|---:|---|
| AAA | +1.98% | February 2026 | +5.83% | March 2026 |
| BBB | -1.02% | February 2026 | -5.15% | March 2026 |
| CCC | +0.91% | February 2026 | +1.82% | February 2026 (revised) |

AAA uses February 103 from row 4. CCC uses 111 from row 12 as-of, but naive uses
112 from row 10, published April 5. The naive path independently starts from all
original rows and applies rules 1, 2 and 4, deliberately omitting rule 3.

## Validation

`test_asof.py` contains 11 unittest tests covering every funnel step, survivor IDs,
both signals and months, two-decimal formatting, inclusive cutoff, missing tickers,
duplicates, revisions, deterministic ties, shuffled input, input nonmutation,
insufficient history, zero denominator and April 15 convergence.

An independent CLI stress run changes the top-level date to April 15 in a temporary
copy, runs `python asof.py`, and asserts identical displayed as-of/naive results
for all three tickers. The delivered file retains March 31 unchanged, then the
program and all tests are rerun. Actual output and exit codes are regenerated in
`validation_output.txt` and `submission_checks.txt` by `prepare_submission.py`.
To repeat manually, change the date, run the program, restore March 31, then run
both commands above. The default-date test intentionally requires March 31.

## References and scope

Reviewed October 27, 2026: [official course repository](https://github.com/CinderZhang/FIN43900-Fall2026),
[Week 10 prework](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-10/student-prework.md),
[Week 10 handout](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-10/student-handout.md),
and [ALFRED Help](https://alfred.stlouisfed.org/help).
The handout confirms rule order and AAA results. ALFRED documents historical
vintages and release-date provenance. GitHub raw/directory requests were unavailable;
the rendered prework and handout were accessible. Brightspace was not accessed;
the user's pasted Lab 16 instructions govern this implementation. Lab 14 and Lab 15
were inspected for context and left unchanged.

## GitHub and Brightspace submission

No commit or push was performed: this workspace is not a Git repository and has
no configured remote. Git is installed at `C:/Program Files/Git/cmd/git.exe` but
is not on PATH. Do not initialize the entire course workspace accidentally.

After copying this `Lab16` folder into the root of your chosen existing course
Git repository, run these PowerShell commands from that repository root:

```powershell
$gitExe = 'C:/Program Files/Git/cmd/git.exe'
& $gitExe status --short
& $gitExe remote -v
python -m unittest discover -s Lab16 -p test_asof.py -v
& $gitExe add -- Lab16/asof.py Lab16/test_asof.py Lab16/README.md Lab16/LAB16_REFLECTION.md Lab16/validation_output.txt Lab16/submission_checks.txt Lab16/SUBMISSION.md Lab16/prepare_submission.py Lab16/.gitignore
& $gitExe diff --cached --name-only
& $gitExe diff --cached -- Lab16
# Confirm the staged list contains only intended Lab16 files before committing.
& $gitExe commit -m 'Complete Lab 16 point-in-time provenance gate'
& $gitExe push
```

If unrelated changes are already staged, resolve that staging before committing.
Use the actual configured branch/upstream; if none is configured, configure your
chosen repository first. No repository name or GitHub URL is assumed here.
After pushing, open GitHub, choose the pushed branch, open `Lab16/asof.py` and
copy the address bar URL (repeat for other requested files). Use the folder URL
for the complete deliverable. Check instructor access and submit the requested
links/files in Brightspace, then verify its receipt.

Before final submission, complete your actual partner explanation, swap and
personal reflection in `LAB16_REFLECTION.md`. Its study notes and blank fields
do not represent those student activities as completed.

## Simple upload option (no Git commands)

Open your own course repository on GitHub and use **Add file > Upload files**.
Upload the contents under a `Lab16` folder, preserving that folder name. Include
all nine deliverable files listed in `prepare_submission.py`; exclude `__pycache__`.
Commit with `Complete Lab 16 point-in-time provenance gate`.
Open the uploaded folder and `asof.py` to copy their actual URLs into `SUBMISSION.md`.
Upload the completed report again if you added those URLs after the first upload.
Do not upload to the instructor's course-content repository.

The optional ZIP is convenient for Brightspace only if its actual instructions
allow ZIP attachments. Upload readable source files to GitHub, not just the ZIP.

The latest supplied assignment labels the numeric column **Price** and the signal
as the **fund's return**. Code, tables and output use that terminology.
