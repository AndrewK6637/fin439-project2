# Student-only changed-input record ? BLANK, NOT EXECUTED

Prepared November 17, 2026. This is an optional Project 2/Week 6-style prediction protocol, not completed classroom evidence. The current Week 12 handout calls Tuesday an open studio with no checkout points; it does not require a new changed-input run before the partner cold run. Follow any newer instructor/Brightspace direction if provided.

## Proposed independent input

- Input: additional annual costs, configuration key `ongoing_cost_bps`.
- Original: **0 basis points per year**, the existing illustrative baseline; not a claim that real costs are zero.
- Proposed new value: **75 basis points per year** (0.75% of assets annually), a disclosed scenario, not a newly approved client cost assumption.
- UI location: sidebar **Additional annual costs (bps)**. Change this box only; leave all other controls at startup defaults.
- Why this input: one directly editable scalar enters the modeled net-return calculation and optimizer return constraint. Unlike actual transaction costs, this scenario does not require inventing current holdings. The scenario's numerical result and decision effect have **not** been calculated during preparation.
- Relevant code: `src/engine.py`, `metrics` and `optimize`; see the code study guide. No predicted direction is supplied here.

## Student completes BEFORE running (AI closed)

| Required field | Student entry |
| --- | --- |
| Date/time and timezone of prediction | |
| Student AI-off prediction for weights | |
| Predicted direction and rough size of annual return/volatility change | |
| Predicted effect on feasibility and mandate verdict | |
| Predicted effect on committee recommendation | |
| Financial reasoning and support for the proposed range | |
| Partner checked units and only one independent input changes | |
| Genuine prediction commit hash | |
| GitHub link proving prediction published before run | |

Do not ask AI to fill these fields. First obtain authorization to commit/publish the prepared repository and ensure its model/data files are frozen. With AI closed, write your prediction, save this file, commit it, and push that genuine prediction commit before the changed run if using it for the final Project 2 Locked Record. Keep the actual commit URL. Do not backdate anything.

## Student executes AFTER prediction is locked (AI closed)

1. Start a fresh app session with the README command. Restore all baseline controls: 60 months, CPI 2.5%, additional annual costs 0 bps, transaction costs 10 bps, reserve 3%, maximum fund weight 100%, optional risk cap off, return overrides off.
2. Record the default outputs yourself and use **Committee recommendation > Download this scenario** to preserve the before JSON.
3. Change **only Additional annual costs (bps) to 75**. Let the model recalculate. Do not change the objective or another control to force feasibility.
4. Record results even if infeasible or the action verb does not change. Download the after JSON. Save both with distinct names and record actual timestamps; do not overwrite prior evidence.
5. Restore the cost input to **0**, record the restored result and verify it matches the first baseline within displayed rounding. Save before/after/restored evidence paths below.
6. Explain the result in your own words, then commit the completed record and actual output files. This after-run commit must follow the genuine prediction commit.

| Actual classroom evidence | Before | After | Restored baseline |
| --- | --- | --- | --- |
| Execution timestamp | | | |
| Additional annual cost (bps/year) observed in app | | | |
| Weights BIL / IEF / LQD / VT (%) | | | |
| Estimated annual gross return (%) | | | |
| Annual additional-cost deduction (%) | | | |
| Estimated return after annual costs (%) | | | |
| Estimated annual volatility (%) | | | |
| Solver feasible? | | | |
| Financial mandate status and failed/unknown rules | | | |
| Authorization gate | | | |
| Recommendation and reasons | | | |
| Saved scenario JSON path | | | |

| Reconciliation | Student entry |
| --- | --- |
| Was the prediction correct? | |
| Difference between predicted and observed result | |
| Explanation, including any unchanged decision | |
| Partner's question and my response | |
| What I checked on my partner's work | |
| Restored-baseline check and tolerance | |
| After-run evidence commit hash/link | |

The existing `docs/changed-input-record.md` and `config/locked_experiment.json` are a separate unrun reserve protocol and remain unchanged. Do not claim either record is complete. If this classroom record becomes your final required Locked Record, explicitly identify and link it in the validation document after genuine completion; preserve the old unrun protocol as such. Do not execute the separate reserve protocol merely to fill a second record.
