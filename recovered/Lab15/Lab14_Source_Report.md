# Lab 14 — Portfolio Baselines

## D — Question and conclusion

**What does each simple portfolio earn and risk — and does any of them meet the Meridian mandate?**

None meets both the 6.50% expected-return objective and every checkable allocation constraint. The benchmark clears the return objective but has no eligible reserves. Equal weight and inverse volatility satisfy the checkable allocation constraints but fall short of the return objective. S9 still requires CIO clarification; these calculations do not certify full IPS compliance.

## R — Inputs and assumptions

All returns, volatilities, and correlations below are course-authored annual training values, not market forecasts. Rates are stored as decimals in Python. CPI of **2.5% is a labelled estimate**, making Meridian's simplified nominal return objective 2.5% + 4.0% = **6.5%**. No additional cost assumption was supplied, so no separate cost deduction is invented. A one-period expected return does not establish achievement of the mandate's net rolling-five-year objective.

| Sleeve | Expected return | Volatility | Meridian reserve eligible? |
|---|---:|---:|---|
| Treasury bills | 3.5% | 0.5% | Yes |
| Treasury 10-year note | 4.3% | 7.0% | Yes |
| Investment-grade bond fund | 5.0% | 6.0% | No |
| Global equity index fund | 8.0% | 16.0% | No |

| Correlation | Bills | 10-year | IG bonds | Equity |
|---|---:|---:|---:|---:|
| Bills | 1.00 | 0.10 | 0.05 | 0.00 |
| 10-year | 0.10 | 1.00 | 0.80 | -0.10 |
| IG bonds | 0.05 | 0.80 | 1.00 | 0.25 |
| Equity | 0.00 | -0.10 | 0.25 | 1.00 |

## I — Files and commands

From the course workspace:

```powershell
cd Lab14
python portfolio.py
python mandate.py
python verify_lab14.py
```

`portfolio.py` uses only the Python standard library. Inputs are editable at the top. Each calculation has its own reusable function, and importing the file does not run the program. It constructs covariance from correlations and volatilities, computes full-precision results, then rounds only the displayed output.

`mandate.py` is a self-contained copy of the Lab 13 checker with candidate E added. The original `../Lab13/mandate.py` also includes E. Its holding order differs from the risk engine: the checker lists equity before IG bonds. E is therefore `[0, 0, 0, 60, 40, 0, 0, 0]` in the checker's percentage-point units.

The original Lab 13 rerun produced: A passes every checkable rule; B fails reserve, liquidity, and company exposure; C fails reserve; D passes every checkable rule. All print `requires CIO clarification`.

## V — Known-answer results

All numeric results below were reproduced by executing the engine. Weights and reserve shares are percentages; return and volatility are annual percentages.

| Portfolio | Bills / 10-year / IG / equity | Return | Volatility | Reserve eligible | Meets 6.5%? |
|---|---|---:|---:|---:|---|
| Benchmark | 0.0 / 0.0 / 40.0 / 60.0 | 6.80% | 10.46% | 0.0% | Yes |
| Equal weight | 25.0 / 25.0 / 25.0 / 25.0 | 5.20% | 5.21% | 50.0% | No |
| Inverse volatility | 84.3 / 6.0 / 7.0 / 2.6 | 3.77% | 1.05% | 90.3% | No |

Inverse-volatility displayed weights sum to 99.9% because of one-decimal rounding; the underlying weights sum to 100%.

Executed checks are recorded in [verification.txt](verification.txt):

- Every displayed field matches the supplied known answer.
- A temporary copy with both IG–equity correlations changed from 0.25 to 0.50 produces **11.00%** benchmark volatility. Expected return stays 6.80%.
- A temporary copy with correlations of 1.30 exits with a nonzero status and a clear out-of-range message, before printing portfolio results.
- Changing only one correlation cell is rejected as asymmetric.
- The delivered source retains 0.25 in both cells; the final normal run matches the original output.
- All three allocations were mapped by sleeve name into the mandate checker. Only the benchmark fails an allocation rule: reserve.

These are automated tests of this submission's code. A partner's independent swap-and-break exercise has not been represented as completed.

### Candidate E: the client's benchmark

```text
Candidate E
Weight total: 100.0% pass
Minimum weight: 0.0% pass
Reserve: 0.0% FAIL
Five-day liquidity: 100.0% pass
Largest company: 0.0% pass
requires CIO clarification
fails 1 rule(s)
```

Meridian requires four quarterly distributions of $750,000, or $3 million. On a $100 million portfolio, the reserve minimum is **3.0%**. The benchmark holds no bills or 10-year notes, so its reserve is **$0**, a **$3 million shortfall**. A policy benchmark can be a useful performance comparator even when it is not itself an admissible implementation portfolio.

## Diversification — Learn on your own

Diversification combines exposures whose returns do not move perfectly together. With positive weights, a correlation below +1 reduces the covariance term relative to perfectly positively correlated assets, lowering portfolio variance. It does not eliminate market risk or guarantee positive returns.

For two assets:

\[
E[R_p]=w_1\mu_1+w_2\mu_2
\]

\[
\sigma_p=\sqrt{w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2\rho_{12}\sigma_1\sigma_2}.
\]

The benchmark's expected return is:

\[
0.40(0.05)+0.60(0.08)=0.068=6.80\%.
\]

Using decimal volatilities, its variance is:

\[
(0.40)^2(0.06)^2+(0.60)^2(0.16)^2+
2(0.40)(0.60)(0.25)(0.06)(0.16)
=0.000576+0.009216+0.001152=0.010944.
\]

\[
\sigma_p=\sqrt{0.010944}=0.1046136\approx\mathbf{10.46\%}.
\]

At correlation +1, volatility would be 0.40(6%) + 0.60(16%) = **12.00%**. The actual correlation of 0.25 reduces risk to 10.46%. This benchmark is less volatile than equity alone (16%), but **not less volatile than IG bonds alone (6%)**. Combining two risky assets can produce volatility below both, but correlation below +1 alone does not ensure that outcome for every weight combination.

For example, using the same supplied IG–equity correlation, 95% IG and 5% equity gives variance 0.003541, or volatility of approximately **5.95%**, below both standalone volatilities. This illustration is not one of the three required baselines.

With IG–equity correlation changed to 0.50:

\[
\sigma_p=\sqrt{0.000576+0.009216+0.002304}
=\sqrt{0.012096}\approx\mathbf{11.00\%}.
\]

## Reflect — Draft for independent review

**Why inverse volatility piles into bills:** The unscaled inverse volatilities are 200 for bills, approximately 14.2857 for the 10-year note, 16.6667 for IG bonds, and 6.25 for equities. Dividing each by their total of approximately 237.2024 gives bills about 84.3% of the portfolio. Its 0.5% volatility is much smaller than the other sleeves'. This weighting rule uses standalone volatility only; it neither targets 6.5% nor accounts for correlations when selecting weights. It is not necessarily the minimum-variance portfolio and does not imply equal contributions to total portfolio risk.

**Which baseline to show the CIO first:** I would start with the benchmark because it is Meridian's own policy reference. It establishes a familiar 6.80% expected-return and 10.46% volatility comparison while exposing the reserve conflict immediately. I would then show equal weight and inverse volatility to demonstrate the cost of reducing risk in these examples: both miss the return objective. The next step is to search for a mix meeting the reserve and return requirements, rather than adopt any baseline unchanged.

## Before Thursday — Cedar fund universe

This universe implements the four roles in the proposed Cedar Scholarship Foundation mandate from Lab 13. These are course research proxies, not personal investment recommendations.

| Ticker | Fund name | Role in Cedar | Price source | Download date |
|---|---|---|---|---|
| BIL | State Street SPDR Bloomberg 1-3 Month T-Bill ETF | Cash / short-term Treasury reserve proxy | [Yahoo monthly history](https://finance.yahoo.com/quote/BIL/history/?frequency=1mo) | 2026-10-20 |
| IEF | iShares 7-10 Year Treasury Bond ETF | Government bonds; not Cedar reserve eligible | [Yahoo monthly history](https://finance.yahoo.com/quote/IEF/history/?frequency=1mo) | 2026-10-20 |
| LQD | iShares iBoxx $ Investment Grade Corporate Bond ETF | Diversified investment-grade corporate fixed income | [Yahoo monthly history](https://finance.yahoo.com/quote/LQD/history/?frequency=1mo) | 2026-10-20 |
| VT | Vanguard Total World Stock ETF | Broad global equity growth exposure | [Yahoo monthly history](https://finance.yahoo.com/quote/VT/history/?frequency=1mo) | 2026-10-20 |

Fund identities and investment roles were checked against issuer pages: [State Street BIL](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-bloomberg-1-3-month-t-bill-etf-bil), [iShares IEF](https://www.ishares.com/us/products/239456/ishares-7-10-year-treasury-bond-etf), [iShares LQD](https://www.ishares.com/us/products/239566/lqd-ishares-iboxx-investment-grade-corporate-bond-etf), and [Vanguard VT](https://advisors.vanguard.com/investments/products/vt/vanguard-total-world-stock-etfp).

**Mandate mapping assumption:** For the course's fund-based app, BIL stands in for short-term Treasury bills, consistent with the lab instruction. Cedar's original wording specifies cash or bills maturing within twelve months; an ETF share itself has no maturity. Explicitly carry the course proxy assumption into Thursday's model. IEF is not a Cedar reserve asset, even though the separate Meridian training mandate makes its 10-year Treasury sleeve eligible. LQD tracks U.S.-dollar investment-grade corporate bonds; that does not imply every issuer is U.S.-domiciled. Cedar's use of "U.S. investment-grade bond funds" is interpreted here as U.S. bond-market exposure, not an issuer-domicile restriction.

### Price file and provenance

[prices.csv](prices.csv) contains `Date,BIL,IEF,LQD,VT`, oldest month first. It has **61 monthly adjusted closing prices per ticker**, September 2021 through September 2026, permitting **60 monthly returns** from October 2021 through September 2026. October 2026 is excluded because it is incomplete on the download date.

Yahoo's history web pages were unavailable through the web tool, so data were retrieved from Yahoo's chart endpoint with `interval=1mo` and the explicit `adjclose` field. These are Yahoo monthly adjusted prices, not unadjusted Close or synthetic prices. The CSV labels each monthly observation with its calendar month-end; a weekend month-end label does not claim that a trade occurred that day. All four series have identical complete month coverage, finite positive prices, and no duplicated months or missing values. Values retain source precision.

The original JSON responses and exact request URLs/download timestamps are preserved in `sources/`; see [download_metadata.json](sources/download_metadata.json). Adjusted prices incorporate Yahoo's corporate-action adjustments, including distributions, and can be revised by the provider. Monthly returns can be calculated as `AdjClose_t / AdjClose_(t-1) - 1`. No historical price estimates replace the lab's training inputs in `portfolio.py`.

## Code understanding and completion status

The risk calculation is in `portfolio_variance()` and `portfolio_volatility()`. Open those functions for the required no-AI partner explanation. The interactive quiz has been asked in chat; the student's answer and follow-up explanation remain pending. No student answer, partner conversation, or independent reflection is fabricated here.

- Completed: Lab 13 rerun, risk engine, all known-answer values, changed-correlation test, invalid/asymmetric rejection, restored inputs, candidate E mandate run, draft learning/reflection sections, fund universe, and five-year price data.
- Student activity still required: answer the code quiz, review/adapt the reflection, explain the code without AI, and perform the partner swap-and-break.
- GitHub checkout pending: this workspace has no Git repository or configured remote. A destination repository was requested in chat. No files have been published and no GitHub links are claimed.

Upload this folder's report, `portfolio.py`, `mandate.py`, `verify_lab14.py`, `verification.txt`, and `prices.csv` for checkout; retaining `sources/` preserves data provenance. Use the resulting GitHub file URLs for the submission.
