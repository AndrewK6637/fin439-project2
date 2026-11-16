"""FIN 43900 Lab 15 dashboard. All portfolio arithmetic lives in portfolio.py."""
from pathlib import Path
from io import BytesIO
import hashlib
import pandas as pd
import streamlit as st
import portfolio as p

HERE = Path(__file__).resolve().parent
st.set_page_config(page_title="Portfolio Stability Decision", layout="wide")
st.title("Portfolio Stability Decision")
st.caption("Built with AI help, a learning demonstration, not investment advice.")
mode = st.sidebar.selectbox("Input data", ["Meridian training inputs", "Cedar prices.csv", "Upload CSV"])
cedar = mode == "Cedar prices.csv"
objective = st.sidebar.number_input("Annual objective (%)", value=5.5 if cedar else 6.5,
                                    step=0.1, key=f"objective_{mode}") / 100
reserve = st.sidebar.number_input("Minimum reserve (%)", min_value=0.0, max_value=100.0,
                                  value=3.0, step=1.0) / 100
upload = st.sidebar.file_uploader("Monthly adjusted-close CSV", type=["csv"])
last36 = st.sidebar.toggle("Use last 36 monthly returns", disabled=mode == "Meridian training inputs")
st.sidebar.caption("CSV: Date, then 1–6 asset columns; one positive adjusted close per calendar month.")


def show_result(title, result, names):
    st.subheader(title)
    if result is None:
        st.error("No feasible portfolio exists on the 5-percentage-point grid for these inputs.")
        return
    st.dataframe(pd.DataFrame({"Asset": names, "Weight (%)": [w * 100 for w in result["weights"]]}),
                 hide_index=True, width="stretch")
    st.metric("Expected return", f'{result["expected_return"]:.2%}')
    st.metric("Annual volatility", f'{result["volatility"]:.2%}')
    st.metric("Reserve-eligible weight", f'{result["reserve_weight"]:.2%}')


try:
    if mode == "Meridian training inputs":
        original = p.SLEEVES.copy()
        correlations = p.CORRELATIONS
        defaults = p.RESERVE_ELIGIBLE
        identity = "meridian"
        baseline = p.optimize_portfolio(original, correlations, p.OBJECTIVE_RETURN, 0.03, defaults)
        baseline_label = "Original optimized baseline (6.5% / 3%)"
        st.info("Course training inputs. Edit equity expected return from 8.0% to 7.0% to test stability.")
    else:
        if mode == "Upload CSV" and upload is None:
            st.info("Upload a monthly adjusted-close CSV to begin.")
            st.stop()
        data = (HERE / "prices.csv").read_bytes() if cedar else upload.getvalue()
        identity = hashlib.sha256(data).hexdigest()[:12] + str(last36)
        estimates = p.estimate_prices(BytesIO(data), last36)
        original, correlations = estimates["sleeves"], estimates["correlations"]
        defaults = {"BIL"} if cedar else set()
        st.info(f'Historical estimates, not forecasts. {estimates["months"]} returns: '
                f'{estimates["start"]} through {estimates["end"]}. Sample standard deviation; arithmetic annualization.')
        if cedar:
            st.warning("Cedar mandate: CPI + 3% after costs. 5.5% is an illustrative nominal hurdle using the prior lab's 2.5% CPI estimate; no additional cost input was supplied. BIL is a course reserve proxy. Turnover compliance requires current holdings and trading history.")
        baseline_label = "All-month unedited estimate baseline"
        all_months = p.estimate_prices(BytesIO(data))
    st.subheader("Editable annual return estimates and reserve eligibility")
    edited, eligible = {}, set()
    for name, (mean, vol) in original.items():
        left, right = st.columns([3, 2])
        with left:
            value = st.number_input(f"{name} expected return (%)", value=mean * 100,
                                   step=0.1, format="%.3f", key=f"return_{identity}_{name}")
        with right:
            if st.checkbox(f"{name} reserve eligible", value=name in defaults,
                           key=f"reserve_{mode}_{name}"):
                eligible.add(name)
        edited[name] = (value / 100, vol)
    if mode != "Meridian training inputs":
        baseline = p.optimize_portfolio(all_months["sleeves"], all_months["correlations"],
                                        objective, reserve, eligible)
    result = p.optimize_portfolio(edited, correlations, objective, reserve, eligible)
    left, right = st.columns(2)
    with left:
        show_result(baseline_label, baseline, list(original))
    with right:
        show_result("Optimal portfolio — current inputs", result, list(original))
    if baseline is not None and result is not None:
        st.metric("Largest absolute weight change", f'{p.largest_weight_change(baseline["weights"], result["weights"]):.2f} percentage points')
        st.caption("Baseline metrics use baseline estimates; current metrics use edited estimates. This is an allocation sensitivity comparison.")
    else:
        st.caption("Weight-change comparison unavailable when either optimization is infeasible.")
    with st.expander("Risk inputs and method"):
        st.dataframe(pd.DataFrame(correlations, index=list(original), columns=list(original)))
        st.write("Search every long-only allocation totaling 100% in 5-point steps. Retain portfolios meeting the objective and reserve minimum; select the lowest volatility. A 3% reserve minimum therefore requires at least 5% on this grid.")
        st.write("The Meridian original Lab 14 policy benchmark is 40% IG / 60% equity; it differs from the optimized baseline above and fails the reserve rule.")
except (ValueError, TypeError, pd.errors.ParserError, UnicodeDecodeError) as error:
    st.error(f"Cannot calculate portfolio: {error}")
