# Signal data card — student-selected CPI fallback

**Decision use:** This is a proposed research rule, not a Cedar-approved trading signal. For the frozen November 2, 2026 decision, it changes the analytical BIL floor from 3% entered in the config to 5% effective. The research candidate already holds 77.04% BIL, so the rule does not change its baseline weights. The committee recommendation remains **0% new capital** while client approval and other mandate evidence are unresolved.

| Field | Definition |
|---|---|
| Name | Inflation pressure / scholarship purchasing-power context |
| Status | Proposed by the agent; student chose to keep it for Project 2 on November 18, 2026. Lab 17 did not select a Project 2 series; the student reported checking three source values and the calculation on November 19. Cedar approval remains pending. |
| Series | CPIAUCSL |
| Primary producer / distributor | U.S. Bureau of Labor Statistics / Federal Reserve Bank of St. Louis |
| Source | [Frozen ALFRED CSV](https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=CPIAUCSL&vintage_date=2026-11-01) |
| Series documentation | [FRED CPIAUCSL series](https://fred.stlouisfed.org/series/CPIAUCSL) |
| Frequency / units | Monthly; CPI index, 1982-1984 = 100, seasonally adjusted |
| Observation date | The measurement month, labeled on its first day; not a publication date |
| Decision date | Frozen educational decision 2026-11-02; not a claim of actual trading |
| Availability boundary | Snapshot dated 2026-11-01, the calendar day before the decision |
| Original release date | Not inferred from observation date; exact original publication timestamp is not stored in this CSV |
| Availability evidence | The value is present in the authentic historical ALFRED snapshot by the cutoff; presence proves by-cutoff availability, not an intraday release time |
| Vintage policy | Use the exact prior-calendar-day vintage. Never substitute today's revised data for a missing vintage |
| Revision handling | Retain the version in the snapshot, including revisions already available at cutoff; raw file and hash retained |
| Transformation | Latest available index / same-month prior-year index - 1; missing counterpart makes signal Not Known |
| Portfolio use | Proposed analytical rule: inflation >3% raises BIL floor to max(client reserve floor,5%). Does not lower the client minimum or replace the 2.5% forward-CPI illustration |
| Rationale | Higher observed inflation motivates a temporary larger near-term scholarship reserve; this is a policy hypothesis, not an optimized trading predictor |
| Missing policy | Quarantine missing/wrong/corrupt vintages; stop deployment. No interpolation or invented release lag |
| Freshness | Signal older than 100 calendar days is unavailable under a disclosed analyst rule |
| Known limits | SA CPI is revisable; monthly observation dates are not release dates; the student-reported three-value check does not prove original intraday release time or that this policy improves returns |

[Raw vintage CSV](../data/raw/signals/CPIAUCSL_2026-11-01.csv) and its [metadata](../data/raw/signals/CPIAUCSL_2026-11-01.meta.json) retain the source, requested vintage, actual retrieval timestamp and SHA-256. The file was retrieved on November 16, **after** the November 2 educational decision date. ALFRED recovers what the historical November 1 vintage contained; the later download is not evidence that this project existed on November 1. See [ALFRED methodology](https://alfred.stlouisfed.org/help).

The student-reported three-value and calculation check is recorded below. The student has chosen to keep the proposed series for this coursework model. Other mandate evidence remains incomplete, so Lab 17's cautious quarantine is preserved at the deployment-approval level. The app can evaluate the analytical scenario without asserting Cedar approved it.

Final audit: an independent download from the same historical ALFRED URL matched all 957 stored rows and the complete file hash. See the [source audit](../outputs/audit-signal-source.json). This is agent verification, distinct from the student's reported spot-check. The [signal code](../src/signal.py) requires the exact HTTPS source hostname, matching series/vintage query and checksum; it quarantines missing/nonfinite/nonpositive latest or prior-year data instead of silently selecting an older value.

## Baseline calculation and decision effect

| Step | Frozen baseline evidence | Meaning |
|---|---|---|
| Latest available CPI observation | September 2026 = **336.298** | The observation month is not the publication date. |
| Same-month prior-year CPI | September 2025 = **324.245** | Makes the comparison year over year. |
| Historical inflation reading | `336.298 / 324.245 - 1 = 0.037173`, about **3.72%** | Above the proposed 3% trigger. |
| Reserve calculation | `max(3% entered BIL minimum, $600,000 / $20 million annual scholarship reserve) = 3%`; proposed signal then raises it to **5%** | The 5% is an analytical floor, not Cedar's approved reserve policy. |
| Portfolio and decision | **77.04% BIL / 22.96% VT**; testable constraints Pass, full mandate Not Known, deployment Reject and **0% new capital** | The candidate is already well above 5% BIL. Passing a numerical screen does not authorize investment. |

These figures are in the [saved baseline](../outputs/results.json), [mandate configuration](../config/mandate.json), and the app's **Point-in-time signal** and **Executive dashboard** tabs. The separate **2.50% illustrative CPI assumption** sets the `2.50% + 3.00% = 5.50%` nominal return hurdle; the historical **3.72%** reading does not replace that input. The raw vintage has a missing October 2025 observation. The app preserves that as a gap in the history chart; it uses the available September observations for this year-over-year calculation.

## Student-reported source check — November 19, 2026

The student reported opening the ALFRED source linked above and finding all three observations used for a spot check: 2025-09-01 = 324.245, 2026-08-01 = 334.131, and 2026-09-01 = 336.298. The student independently calculated `336.298 / 324.245 - 1 = 0.037173` (approximately **3.7173%** year over year). This agrees with the app's rounded 3.72% inflation-pressure reading. This is the student's reported check in conversation; no screenshot or separate signed check record was supplied. It verifies the displayed historical observation values and arithmetic, not Cedar approval of the proposed signal policy or the original intraday release time.

## What still needs a committee decision

Cedar would need to approve or reject the CPI trigger, the 5% analytical floor, and whether BIL can count toward its scholarship reserve. The student's arithmetic check supports the displayed CPI reading; it does **not** show that this rule improves investment outcomes. The baseline allocation is unchanged by the rule, so that result cannot establish its benefit. A comparison using the same prices and dates with the rule turned off would help evaluate the policy before adoption. Cedar's risk limit, actual holdings, and trading costs also remain unresolved; see the [decision memo](decision-memo.md).
