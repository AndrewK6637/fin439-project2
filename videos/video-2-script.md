# Video 2: Code walkthrough

Target 4:30; maximum 5:00. Script is not a transcript. Keep terminal and editor ready; do not run the locked experiment during recording.

OpenAI Codex helped recover coursework, develop and test the application, and draft this script.

I am responsible for the analysis and final decision. This is educational work, not investment advice.

## 0:00-0:30 | Disclosures and map

[Read the disclosures. Show the project tree.]

The application separates data, finance calculations, signal timing and presentation. The dashboard calls the same workflow as the report generator, so the memo and application use the same calculations.

## 0:30-1:10 | Inputs and provenance

[Show `config/mandate.json`; `src/data.py`: `load_prices`, `monthly_returns`, `estimates`.]

The configuration preserves the four recovered funds and marks assumptions that still need approval. The loader rejects duplicate dates and invalid prices. It inserts missing months before calculating returns, then drops incomplete common observations without forward filling. Arithmetic monthly means and sample covariance are annualized by twelve. This is an estimate, not a promised return.

## 1:10-2:00 | Portfolio engine

[Show `src/engine.py`: `equal_weight`, `inverse_volatility`, `metrics`, `optimize`, `rules`.]

Equal weight assigns one quarter to each fund. The transparent second baseline divides inverse individual volatility by its total. The constrained model minimizes portfolio variance, which is weights transpose times covariance times weights, subject to the configured rules. SLSQP must report success, and the independent rule check must find no testable failure. Unknown mandate evidence remains unknown. A numerical failure does not become a successful portfolio merely because its weights look reasonable.

## 2:00-2:40 | Vintage boundary

[Show `src/signal.py`: `evaluate_signal`, `effective_reserve`; then the signal data card.]

The signal uses an ALFRED snapshot from the calendar day before the decision date. The code checks vintage identity, hash, dates, missing observations and freshness. Year-over-year CPI compares the latest available observation with the same month a year earlier. This is a proposed replacement for the quarantined signal, not a recovered student approval. It changes the feasible reserve floor, although the default optimum already exceeds that floor.

## 2:40-3:20 | Robustness and decisions

[Show `src/workflow.py`: `stress_cases`, `stop_decision`, `run`.]

The ordinary stresses change a return estimate, shorten the estimation window, increase transaction costs and tighten the largest fund weight. Trading costs distinguish one-way turnover from two-sided traded notional. Actual client trades are unavailable, so scenario costs are not presented as known client costs. Invalid evidence, infeasibility or excessive instability stops the process. Missing approval evidence blocks deployment even when all numerical stresses succeed.

## 3:20-4:05 | Validation

[Show `tests/test_engine.py`, `tests/test_app.py`, and `outputs/pytest-results.txt`.]

Tests include manually checkable variance and return answers, zero and invalid inputs, infeasible constraints, annualization, missing months, timing boundaries and application interactions. The holdout trains only on the earlier period, but its prices came from a later adjusted snapshot. That limitation is displayed instead of calling it a fully point-in-time trading backtest.

## 4:05-4:30 | Locked record and reproducibility

[Show `docs/changed-input-record.md` and README commands.]

The locked experiment requires my own AI-off prediction and a genuine GitHub commit before an AI-off run. That run has not occurred. The gate was tested only to reject blank prediction fields. A new user can install the pinned dependencies, run pytest and launch Streamlit from the README.
