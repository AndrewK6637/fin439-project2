# Purdue FIN 43900 - Fall 2026

This project is for educational and research purposes only.
# Lab 16: Provenance Gate

**Student name:** [ENTER YOUR NAME]  
**Section:** [ENTER YOUR SECTION]  
**Submission date:** [ENTER DATE]  
**GitHub Lab16 folder URL:** [PASTE AFTER UPLOADING]  
**GitHub asof.py URL:** [PASTE AFTER UPLOADING]

## Objective

Determine which training-table observations were knowable on March 31, 2026,
and compare a point-in-time signal with a naive signal that uses later releases
and revisions. The inputs are the supplied 12-row training table, not live data.

## Implementation

`asof.py` uses Python's standard library. The decision date and complete input
table are editable at the top. Each record retains its original row ID.

1. Quarantine missing or blank tickers.
2. Remove exact duplicates using ticker, measurement month, publication date,
   and price value; retain the smallest original row ID.
3. Remove publications strictly after the decision date; allow same-day releases.
4. Retain the latest publication for each ticker/month. If dates tie, retain
   the smallest original row ID, independent of input order.

The naive calculation starts again from the original data and applies rules 1,
2 and 4 without the publication-date cutoff. Neither path mutates the inputs.

## March 31 results

| Rule | Input rows | Removed | Output rows | Original removed IDs |
|---|---:|---:|---:|---|
| 1: Missing tickers | 12 | 1 | 11 | 11 |
| 2: Exact duplicates | 11 | 1 | 10 | 7 |
| 3: Publication cutoff | 10 | 3 | 7 | 3, 8, 10 |
| 4: Latest available vintage | 7 | 1 | 6 | 2 |

Reconciliation: 12 original rows - 6 removed rows = 6 surviving rows.

| Original row | Ticker | Month measured | Published on | Price |
|---|---|---|---|---:|
| 1 | AAA | 2026-01 | 2026-02-10 | 101.0 |
| 4 | AAA | 2026-02 | 2026-03-25 | 103.0 |
| 5 | BBB | 2026-01 | 2026-02-10 | 98.0 |
| 6 | BBB | 2026-02 | 2026-03-10 | 97.0 |
| 9 | CCC | 2026-01 | 2026-02-10 | 110.0 |
| 12 | CCC | 2026-02 | 2026-03-10 | 111.0 |

Signal = `(latest available price / previous available price - 1) * 100`.
Values below are fund returns computed from the supplied training prices.

| Ticker | As-of calculation | As-of signal/month | Naive calculation | Naive signal/month |
|---|---|---|---|---|
| AAA | (103/101 - 1) * 100 | +1.98%, February 2026 | (109/103 - 1) * 100 | +5.83%, March 2026 |
| BBB | (97/98 - 1) * 100 | -1.02%, February 2026 | (92/97 - 1) * 100 | -5.15%, March 2026 |
| CCC | (111/110 - 1) * 100 | +0.91%, February 2026 | (112/110 - 1) * 100 | +1.82%, February 2026 (revised) |

AAA's March measurement was published April 10. CCC's later February revision
was published April 5. Neither was knowable on March 31. Rule 4 selects AAA's
March 25 February revision of 103 instead of its March 10 value of 104.

## Validation evidence

All 11 automated tests passed. They check the four funnel steps, survivor IDs,
both sets of signals and their months, displayed rounding, same-day publication,
missing tickers, duplicates, revisions, ties, order independence, nonmutation,
insufficient history, and a zero denominator.

The separate April 15 CLI test yields identical as-of and naive signals:
AAA +5.83% for March; BBB -5.15% for March; CCC +1.82% for February.
The delivered default is restored to March 31. See `validation_output.txt`
for actual execution output and `submission_checks.txt` for package verification.

```powershell
python asof.py
python -m unittest -v test_asof.py
```

## Student work to complete

Complete the clearly marked fields in `LAB16_REFLECTION.md`: your own answers,
actual partner explanation and swap, observed partner-test results, and personal
reflection. Those fields intentionally remain blank; automated testing does not
represent a completed partner exercise. Study notes are labeled as assistant-prepared.

## Final submission checklist

- [x] Program and editable training data included.
- [x] March 31 known answers and April 15 convergence verified.
- [x] Automated tests and actual execution output included.
- [ ] Enter name, section and date above.
- [ ] Complete your answers and actual partner/reflection fields.
- [ ] Run `python prepare_submission.py` after edits to refresh the ZIP.
- [ ] Upload the complete Lab16 folder to your chosen GitHub repository.
- [ ] Paste the actual GitHub URLs above; refresh the ZIP if submitting it.
- [ ] Follow the actual Brightspace attachment/link requirements and verify receipt.

The ZIP is a prepared file package, not evidence of GitHub or Brightspace submission.
The README contains source references and GitHub instructions.
