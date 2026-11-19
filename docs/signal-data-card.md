# Signal data card - student-selected fallback

| Field | Definition |
|---|---|
| Name | Inflation pressure / scholarship purchasing-power context |
| Status | Proposed by the agent; student chose to keep it for Project 2 on November 18, 2026. Lab 17 did not select a Project 2 series; the student reported checking three source values and the calculation on November 19. Cedar approval remains pending. |
| Series | CPIAUCSL |
| Primary producer / distributor | U.S. Bureau of Labor Statistics / Federal Reserve Bank of St. Louis |
| Source | https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=CPIAUCSL&vintage_date=2026-11-01 |
| Series documentation | https://fred.stlouisfed.org/series/CPIAUCSL |
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

`data/raw/signals/CPIAUCSL_2026-11-01.meta.json` retains source, requested vintage, actual retrieval timestamp and SHA-256. Downloading it now is not a claim that the project existed at that historical date. ALFRED is specifically used to recover the historical vintage. See [ALFRED methodology](https://alfred.stlouisfed.org/help).

The student-reported three-value and calculation check is recorded below. The student has chosen to keep the proposed series for this coursework model. Other mandate evidence remains incomplete, so Lab 17's cautious quarantine is preserved at the deployment-approval level. The app can evaluate the analytical scenario without asserting Cedar approved it.

Final audit: an independent download from the same historical ALFRED URL matched all 957 stored observations and the complete file hash. See `outputs/audit-signal-source.json`. This is agent verification, not the required student's source check. The gate now requires exact HTTPS source hostname, matching series/vintage query and checksum; it quarantines missing/nonfinite/nonpositive latest or prior-year data instead of silently selecting an older value.

## Student-reported source check — November 19, 2026

The student reported opening the ALFRED source linked above and finding all three observations used for a spot check: 2025-09-01 = 324.245, 2026-08-01 = 334.131, and 2026-09-01 = 336.298. The student independently calculated `336.298 / 324.245 - 1 = 0.037173` (approximately **3.7173%** year over year). This agrees with the app's rounded 3.72% inflation-pressure reading. This is the student's reported check in conversation; no screenshot or separate signed check record was supplied. It verifies the displayed historical observation values and arithmetic, not Cedar approval of the proposed signal policy or the original intraday release time.
