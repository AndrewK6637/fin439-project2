# Lab 16 study notes and student completion space

This project is for educational and research purposes only.

These are assistant-prepared study notes, not the student's completed reflection
or evidence of a partner conversation.

- Look-ahead bias means using information unavailable at the historical decision time.
- Measurement time identifies the period described; publication time identifies when
  the observation becomes available. A March measurement is not automatically known in March.
- Revisions change past measurements. Use the vintage available then, not today's revised history.
- AAA's naive +5.83% uses 109/103 - 1, multiplied by 100. The March value 109 was
  published April 10, so this signal was not knowable March 31.
- Rule 4 most directly changes AAA's February result: it replaces row 2's 104
  with row 4's 103, published March 25. The as-of signal is (103/101 - 1)*100 = +1.98%.
- A naive backtest might claim a March 31 strategy could react to AAA's +5.83%
  or CCC's revised +1.82%. Both leak later information. These are fund returns from the training prices; no trading-strategy profitability is established.

## Rule 4, line by line

In `latest_vintages` in `asof.py`:

```python
winners = {}
for row in records:
    key = (row['ticker'], row['month_measured'])
    rank = (date.fromisoformat(row['published_on']), -row['row_id'])
    if key not in winners or rank > winners[key][0]:
        winners[key] = (rank, dict(row))
return [winners[key][1] for key in sorted(winners)]
```

1. Create a dictionary of winning vintages.
2. Examine each eligible row. In the as-of path, rule 3 has already excluded late publications.
3. Group by both ticker and measurement month, so different months remain separate.
4. Rank by publication date first. Negative row ID gives the smaller original ID
   priority when dates tie, even if input order changes.
5. Accept a group's first row or replace its winner when the candidate ranks higher.
6. Save the rank and a copy of the original row, retaining its ID.
7. Return the winning rows sorted by ticker and month.

Professor explanation practice: "For each ticker and month, I keep the most recent
publication that survived the date cutoff. I break publication-date ties using
the smaller original row ID and preserve those IDs for the audit."

## Student answers - complete these yourself

Replace each bracketed prompt with your own response. The notes above may help
with studying, but these answers should reflect your understanding.

### 1. Why must the cutoff run before vintage selection?

[WRITE YOUR ANSWER HERE]

### 2. Why does CCC's naive February value differ from its as-of February value?

[WRITE YOUR ANSWER HERE]

### 3. Why does the April 15 run converge, and when might a later cutoff still not converge?

[WRITE YOUR ANSWER HERE]

## Actual partner exercise - student to complete

**Partner name:** [ENTER PARTNER NAME]  
**Exercise date:** [ENTER DATE]

### My explanation of rule 4 to my partner

[DESCRIBE WHAT YOU ACTUALLY EXPLAINED, IN YOUR OWN WORDS]

### Partner swap and independent test

**Files exchanged:** [ENTER FILE NAMES]  
**Who ran whose code:** [ENTER DETAILS]  
**Exact command run:** [ENTER COMMAND]  
**Decision date or input changed:** [ENTER ACTUAL CHANGE]

**Expected result before running:**

[ENTER YOUR PREDICTION]

**Actual output observed:**

[PASTE OR DESCRIBE THE REAL PARTNER-TEST OUTPUT]

**Difference, bug, or disagreement and how it was resolved:**

[DESCRIBE WHAT HAPPENED; IF NONE, SAY SO ONLY AFTER THE TEST]

## Personal reflection - student to complete

In your own words, describe what this exercise taught you about publication
lags and revisions, what surprised you, and one check you would use before
trusting a historical backtest. Mention any remaining uncertainty.

[WRITE YOUR PERSONAL REFLECTION HERE]

The automated April 15 test does not substitute for a real partner swap.
