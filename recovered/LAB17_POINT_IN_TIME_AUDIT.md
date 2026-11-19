# Lab 17 - Point-in-Time Audit

**Decision question:** Was each number available when I would have traded on it, and may Project 2 use it?

I developed an interactive dashboard to compare current FRED observations with historical ALFRED vintages. My central finding is that a recent observation and a revision to an older observation are different events: both can introduce look-ahead bias if I use today's data in a historical decision.

## Verified results

Live downloads on **October 29, 2026** reproduced all five lab checkpoints. The table uses observations from January 1, 2020 onward; monthly dates identify measurement months, not publication dates. The benchmark values are test assertions, not hardcoded dashboard outputs.

| Series | Requested vintage | Last vintage observation | Vintage value | Current last observation/value | Later observations | Changed matching dates | Result |
|---|---|---|---:|---|---:|---:|---|
| [BAA](https://fred.stlouisfed.org/series/BAA) | 2026-10-05 | 2026-09-01 | 6.47 | 2026-09-01 / 6.47 | 0 | 0 | Pass |
| [FEDFUNDS](https://fred.stlouisfed.org/series/FEDFUNDS) | 2026-10-05 | 2026-09-01 | 3.75 | 2026-09-01 / 3.75 | 0 | 0 | Pass |
| [DGS10](https://fred.stlouisfed.org/series/DGS10) | 2026-10-05 | 2026-10-02 | 5.28 | 2026-10-28 / 5.05 | 17 | 0 | Pass |
| [MORTGAGE30US](https://fred.stlouisfed.org/series/MORTGAGE30US) | 2026-10-05 | 2026-10-01 | 7.28 | 2026-10-29 / 7.24 | 4 | 0 | Pass |
| [PAYEMS](https://fred.stlouisfed.org/series/PAYEMS) | 2025-01-15 | 2024-12-01 | 159,536 | 2026-09-01 / 159,044 | 21 | 59 | Pass |

The four rate series are measured in percent; PAYEMS is measured in thousands of jobs. December 2024 PAYEMS was **159,536** in the January 15, 2025 vintage and **158,316** in the current download, a downward revision of **1,220 thousand jobs**. Of the 60 matched observation dates, 59 changed; the 21 later observations are counted separately. This result demonstrates why a fixed publication lag alone cannot remove revision bias.

The app passed checks for missing values, duplicate dates, malformed responses, invalid series IDs, empty vintages, caching, and matched-date revision counts. Live Streamlit interaction tests reproduced the benchmarks and preserved valid comparisons when an invalid series was entered. Additional tests checked the observation filters, combined-chart normalization, and history-range controls. Python 3.13.15, pandas 3.0.6, and Streamlit 1.66.0 were used.

## Changes I made to the app

I changed the original long page into separate series tabs, with Chart and Data & revisions views, plus Combined chart, Compare, and About tabs. I refined the header, spacing, cards, and colors to make the dashboard easier to read while keeping its controls simple.

The combined chart compares several series at once using either current or vintage data. Original units preserve the economic meaning of the values; Index = 100 compares relative movement from the first shared observation date with nonzero values. It does not represent investment returns, and the app does not fill missing dates to force different frequencies to match.

I also changed the observation tables to show all observations by default, with filters for revised and newly available values. A zero-revision result now leaves the history visible instead of producing an empty revisions-only view. Rate revisions appear in basis points; other series retain their source units. CSV exports and a revision-magnitude chart make the results easier to inspect.

Finally, I added one-, five-, and ten-year ranges, a Since 2020 option, and All history. These controls load earlier observations that cannot be revealed simply by dragging a chart filtered to a later start date. Date presets and the PAYEMS example provide quick comparisons without changing the underlying data.

## Data provenance and audit scope

| Field | Finding |
|---|---|
| Audited series | BAA, FEDFUNDS, DGS10, MORTGAGE30US, and PAYEMS |
| Sources | Federal Reserve Bank of St. Louis FRED current-data downloads and ALFRED historical-vintage downloads; series links appear in the validation table. |
| Measures and frequencies | BAA: monthly Moody's Baa corporate bond yield; FEDFUNDS: monthly effective federal funds rate; DGS10: daily 10-year Treasury constant maturity rate; MORTGAGE30US: weekly 30-year fixed mortgage rate; PAYEMS: monthly total nonfarm payroll employment. |
| Units | Percent for the four rates; thousands of jobs for PAYEMS. |
| Download date | October 29, 2026. |
| Availability | Observation dates are not release dates. ALFRED supplies the historical snapshot; the latest observation's age does not establish publication lag. |
| Revisions | No changed matched values in the four October 5 rate comparisons; 59 changed matched values in the January 15, 2025 PAYEMS comparison. These results apply to the tested windows. |
| Leakage risk | Using an observation before publication or replacing its historical estimate with a later revision. |

These are automated source-download checks. A separately selected Project 2 series was not documented in the available project materials, so this audit does not establish its publication lag, its September 30 versus October 29 comparison, or three manually checked source-page values. The benchmark evidence is not represented as a completed selected-series data card.

[ALFRED Help](https://alfred.stlouisfed.org/help) explains that release dates may come from the original source, a data provider, or the date first available in FRED. It also states that new observations and revisions are generally added within one business day of release. I therefore distinguish the date of a historical snapshot from proof of availability at a particular intraday trading time.

## How the code prevents leakage

`download_current` and `download_vintage` make separate cached requests. The vintage cache includes both the series ID and cutoff date, so a different cutoff cannot silently reuse the wrong snapshot. Each successful download retains its UTC timestamp; the caches expire after one hour.

The parser treats `.` as missing, checks the returned series and dates, rejects duplicate observations, and sorts valid values. `download_vintage` sends the cutoff to ALFRED and excludes observation dates beyond it. ALFRED establishes historical availability; filtering today's file by observation date would not recreate that information.

`compare` joins only matching observation dates before counting changed values. A difference greater than 0.000000001 in source units counts as a revision. Later observations and newly available dates are reported separately. A failed vintage stays unavailable rather than being replaced by current data.

## Project 2 decision

My decision is **QUARANTINE** for an undocumented Project 2 macroeconomic input. Cedar Scholarship Foundation's CPI + 3% objective does not by itself identify a FRED series or establish when its values were available.

My admission rule uses the ALFRED vintage from **the calendar day before each trade**, retains only observations present in that snapshot, and records the series ID, cutoff, download timestamp, and values. An unavailable vintage or uncertain release history excludes the signal from that decision. This is a rule for the backtest; the dashboard provides the comparison rather than executing a trading strategy.

The decision changes to **ADMIT** when the series' identity and release history are documented, source-value checks support the data, and the historical decision process enforces that rule. Today's revised history can make a signal appear more timely and accurate than it was, likely overstating apparent forecasting skill. The direction and size of the return distortion depend on the allocation rule; a downward data revision does not automatically imply an upward return bias.

## Sources and disclosure

- [ALFRED methodology and release-date conventions](https://alfred.stlouisfed.org/help).
- [Current PAYEMS CSV](https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS) and [January 15, 2025 PAYEMS vintage](https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=PAYEMS&vintage_date=2025-01-15).
- [Lab 17 reference](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-10/lab-17-point-in-time.md).

This is an individual submission. OpenAI Codex assisted with drafting, implementation, source retrieval, and automated testing. This project is for educational and research purposes only, not investment advice.

## Complete executable source - `asof_app.py`

```python
"""FIN 439 Lab 17: interactive point-in-time economic data audit."""
from datetime import date, datetime, timezone
from io import StringIO
import argparse
import json
import re
from urllib.request import urlopen

import pandas as pd
import streamlit as st

NAMES = {
    "BAA": "Moody's Seasoned Baa Corporate Bond Yield",
    "FEDFUNDS": "Effective Federal Funds Rate",
    "DGS10": "10-Year Treasury Constant Maturity Rate",
    "MORTGAGE30US": "30-Year Fixed Rate Mortgage Average",
}


def series_id(value):
    value = value.strip().upper()
    if not re.fullmatch(r"[A-Z0-9_]{1,80}", value):
        raise ValueError("Enter one FRED series ID using letters, digits or underscores.")
    return value


def parse_csv(text, sid):
    frame = pd.read_csv(StringIO(text), na_values=["."])
    if len(frame.columns) != 2 or str(frame.columns[0]).lower() not in (
        "date", "observation_date"
    ):
        raise ValueError("Expected a two-column FRED/ALFRED CSV.")
    if not (frame.columns[1] == sid or frame.columns[1].startswith(sid + "_")):
        raise ValueError("Returned series does not match requested ID.")
    frame.columns = ["date", "value"]
    frame["date"] = pd.to_datetime(frame["date"], errors="raise")
    frame["value"] = pd.to_numeric(frame["value"], errors="raise")
    frame = frame.dropna(subset=["value"])
    if frame["date"].isna().any() or frame["date"].duplicated().any():
        raise ValueError("Missing or duplicated observation dates.")
    if frame["value"].isin([float("inf"), -float("inf")]).any():
        raise ValueError("Nonfinite observation value.")
    return frame.set_index("date").sort_index()


def fetch(url, sid):
    # One HTTP request; no fallback to today's data for a failed vintage.
    with urlopen(url, timeout=20) as response:
        frame = parse_csv(response.read().decode("utf-8-sig"), sid)
    return frame, datetime.now(timezone.utc).isoformat()


@st.cache_data(ttl=3600, show_spinner=False)
def download_current(sid):
    sid = series_id(sid)
    return fetch(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}", sid)


@st.cache_data(ttl=3600, show_spinner=False)
def download_vintage(sid, vintage):
    sid = series_id(sid)
    vintage = date.fromisoformat(str(vintage))
    if vintage > date.today():
        raise ValueError("Vintage cannot be in the future.")
    frame, stamp = fetch(
        f"https://alfred.stlouisfed.org/graph/alfredgraph.csv?id={sid}"
        f"&vintage_date={vintage.isoformat()}", sid
    )
    # Observation dates alone cannot establish availability; ALFRED does that.
    return frame.loc[frame.index <= pd.Timestamp(vintage)], stamp


def latest(frame):
    if frame.empty:
        return None, None
    return frame.index[-1].date().isoformat(), float(frame.iloc[-1]["value"])


def compare(current, vintage, start):
    current = current.loc[current.index >= pd.Timestamp(start)]
    vintage = vintage.loc[vintage.index >= pd.Timestamp(start)]
    cd, cv = latest(current)
    vd, vv = latest(vintage)
    matched = vintage.join(current, how="inner", lsuffix="_v", rsuffix="_c")
    changed = int(((matched.value_v - matched.value_c).abs() > 1e-9).sum())
    return {
        "Vintage last date": vd, "Vintage last value": vv,
        "Current last date": cd, "Current last value": cv,
        "Later observations": int((current.index > pd.Timestamp(vd)).sum()) if vd else None,
        "Changed matching dates": changed,
        "Newly available dates": int((~current.index.isin(vintage.index)).sum()),
        "Matched dates": len(matched),
    }


def revision_table(current, vintage, start, sid):
    matched = vintage.join(current, how="inner", lsuffix="_v", rsuffix="_c")
    matched = matched.loc[matched.index >= pd.Timestamp(start)].copy()
    difference = matched.value_c - matched.value_v
    matched = matched.loc[difference.abs() > 1e-9].copy()
    label = "Revision (basis points)" if sid in NAMES else "Revision (source units)"
    matched[label] = difference.loc[matched.index] * (100 if sid in NAMES else 1)
    return matched.rename(columns={"value_v": "Vintage value", "value_c": "Current value"})


def show_series(current, old, start, vintage, sid):
    """Display only downloaded values; never fill missing vintage observations."""
    window = pd.Timestamp(start)
    current = current.loc[current.index >= window] if current is not None else None
    old = old.loc[old.index >= window] if old is not None else None
    unit = "Percent" if sid in NAMES else "Thousands of jobs" if sid == "PAYEMS" else "Source units (see FRED page)"
    st.caption(f"Units: {unit} · [Series definition and source](https://fred.stlouisfed.org/series/{sid})")
    if current is not None and old is not None:
        summary = compare(current, old, start)
        columns = st.columns(4)
        for column, label, key in (
            (columns[0], "Latest current value", "Current last value"),
            (columns[1], "Latest vintage value", "Vintage last value"),
        ):
            value = summary[key]
            column.metric(label, "Unavailable" if value is None else f"{value:,.4f}".rstrip("0").rstrip(".") + ("%" if sid in NAMES else ""))
        columns[0].caption(f"Observed: {summary['Current last date'] or 'Unavailable'}")
        columns[1].caption(f"Observed: {summary['Vintage last date'] or 'Unavailable'} · As of {vintage}")
        columns[2].metric("New observations", summary["Newly available dates"])
        columns[3].metric("Revised observations", summary["Changed matching dates"])
    chart_tab, data_tab = st.tabs(["Chart", "Data & revisions"])
    with chart_tab:
        chart_parts = []
        if current is not None:
            chart_parts.append(current.rename(columns={"value": "Current"}))
        if old is not None:
            chart_parts.append(old.rename(columns={"value": f"Known on {vintage}"}))
        if chart_parts:
            chart = pd.concat(chart_parts, axis=1).sort_index()
            if chart.empty:
                st.info("No observations in this window.")
            else:
                st.line_chart(chart, x_label="Observation date", y_label=unit,
                              color=["#3478A4", "#BD8850"][:len(chart.columns)])
                st.caption("Hover to inspect values. Identical histories overlap; the vintage line stops at its last available observation.")
    with data_tab:
        if current is not None and old is not None:
            revisions = revision_table(current, old, start, sid)
            st.markdown("#### Observation explorer")
            table = old.join(current, how="outer", lsuffix="_v", rsuffix="_c")
            matched = table.value_v.notna() & table.value_c.notna()
            changed = matched & ((table.value_c - table.value_v).abs() > 1e-9)
            table["Status"] = "Unchanged"
            table.loc[changed, "Status"] = "Revised"
            table.loc[table.value_v.isna(), "Status"] = "Newly available"
            table.loc[table.value_c.isna(), "Status"] = "Vintage only"
            difference_label = "Revision (basis points)" if sid in NAMES else "Revision (source units)"
            table[difference_label] = (table.value_c - table.value_v) * (100 if sid in NAMES else 1)
            table = table.rename(columns={"value_v": "Vintage value", "value_c": "Current value"})
            choice = st.radio("Show observations", ["All observations", "Revised only", "Newly available"],
                              horizontal=True, key=f"filter_{sid}")
            filtered = table if choice == "All observations" else table.loc[
                table.Status == ("Revised" if choice == "Revised only" else "Newly available")]
            if revisions.empty:
                st.info("No revisions detected for this date and window. Unchanged observations are shown in All observations. "
                        "Try the Payroll revisions demo to see an actual revision history.")
            st.caption("Difference = current minus vintage on matched dates only. Blank differences mean no matching pair. "
                       + ("Rate differences are in basis points (1 percentage point = 100 bp)." if sid in NAMES else "Differences retain source units."))
            if filtered.empty:
                st.info("No observations match this filter. Choose All observations or an earlier vintage.")
            else:
                st.dataframe(filtered.sort_index(ascending=False).rename_axis("Observation date"),
                             width="stretch", height=300)
            st.download_button("Download displayed observations", filtered.to_csv().encode("utf-8"),
                               file_name=f"{sid}_{vintage}_audit.csv", mime="text/csv", key=f"csv_{sid}")
            if not revisions.empty:
                with st.expander("Revision magnitude over time"):
                    st.bar_chart(revisions[[difference_label]], color="#BD8850", y_label=difference_label)
        if current is None or old is None:
            st.info("Both downloads are needed for an observation comparison.")



def combined_data(frames, start, normalize=False):
    """Align observation dates without interpolation or forward filling."""
    parts = {sid: frame.loc[frame.index >= pd.Timestamp(start), "value"]
             for sid, frame in frames.items() if frame is not None}
    if not parts:
        return pd.DataFrame(), None
    data = pd.concat(parts, axis=1).sort_index().dropna(how="all")
    base = None
    if normalize and not data.empty:
        common = data.dropna()
        common = common.loc[(common != 0).all(axis=1)]
        if common.empty:
            raise ValueError("No shared observation date with nonzero values. Use original units or select series with matching dates.")
        base = common.index[0]
        data = data.loc[base:].div(common.iloc[0]).mul(100)
    return data, base


def main():
    st.set_page_config(page_title="Point-in-Time Audit", layout="wide")
    st.html("""<style>
    .block-container {max-width: 1380px; padding-top: 1.6rem; padding-bottom: 2rem;}
    .pit-header {padding: 26px 30px; margin-bottom: 18px; border-radius: 10px;
        background: #13283d; border-left: 4px solid #61a5ba; color: #fff;}
    .pit-header .eyebrow {color: #b9d2e3; font-size: .69rem; letter-spacing: .16em;
        font-weight: 600; margin-bottom: 10px;}
    .pit-header h1 {color: #fff !important; font-size: clamp(1.8rem, 3vw, 2.35rem);
        font-weight: 600; letter-spacing: -.035em; padding: 0; line-height: 1.2;}
    .pit-header p {color: #d2dfeb !important; margin: 9px 0 0; font-size: .91rem;}
    [data-testid="stMetric"] {border: 1px solid rgba(128,128,128,.24);
        border-radius: 8px; padding: 15px 18px; box-shadow: 0 2px 6px rgba(0,0,0,.025);}
    [data-testid="stMetricValue"] {font-size: 1.85rem; font-weight: 600;
        font-variant-numeric: tabular-nums; letter-spacing: -.035em;}
    [data-testid="stMetricLabel"] {font-size: .8rem;}
    [data-baseweb="tab-list"] {gap: 4px; padding: 3px 0 8px;}
    button[data-baseweb="tab"] {font-size: .88rem; padding: 9px 16px; border-radius: 6px;}
    button[data-baseweb="tab"][aria-selected="true"] {background: #24485f; color: #fff !important;}
    button[data-baseweb="tab"][aria-selected="true"] p {color: #fff !important;}
    [data-testid="stSidebar"] {border-right: 1px solid rgba(128,128,128,.18);}
    [data-testid="stSidebar"] button {border-radius: 6px; font-size: .85rem;}
    [data-testid="stDataFrame"] {border-radius: 8px; overflow: hidden;}
    h2, h3 {letter-spacing: -.025em;}
    @media (max-width: 700px) {.pit-header {padding: 20px;}}
    </style>
    <div class="pit-header">
      <div class="eyebrow">ECONOMIC RESEARCH / FIN 439</div>
      <h1>Point-in-Time Audit</h1>
      <p>Compare economic series, inspect revisions, and evaluate historical availability.</p>
    </div>""")
    for key, value in {"chosen_series": list(NAMES), "extra_series": "",
                       "start_date": date(2020, 1, 1), "vintage_date": date.today()}.items():
        st.session_state.setdefault(key, value)
    def preset(cutoff, payroll=False):
        st.session_state["vintage_date"] = cutoff
        if payroll:
            st.session_state["chosen_series"] = []
            st.session_state["extra_series"] = "PAYEMS"
            st.session_state["start_date"] = date(2020, 1, 1)
        elif st.session_state.get("start_date", date(2020, 1, 1)) > cutoff:
            st.session_state["start_date"] = cutoff
    def history_range(years=None, since_2020=False):
        cutoff = st.session_state.get("vintage_date") or date.today()
        anchor = min(cutoff, date.today())
        st.session_state["start_date"] = (
            min(date(2020, 1, 1), anchor) if since_2020 else
            (pd.Timestamp(anchor) - pd.DateOffset(years=years)).date()
            if years is not None else date(1776, 1, 1)
        )
    st.markdown("**Chart history**")
    range_columns = st.columns(5)
    for column, label, years in zip(range_columns[:3], ["1 year", "5 years", "10 years"], [1, 5, 10]):
        column.button(label, on_click=history_range, args=(years,), width="stretch")
    range_columns[3].button("Since 2020", on_click=history_range,
                            kwargs={"since_2020": True}, width="stretch")
    range_columns[4].button("All history", on_click=history_range, width="stretch", type="primary")
    st.caption("Load earlier observations with these buttons. Dragging a chart only explores its loaded window. "
               "Year ranges start before the selected vintage; All history uses each series' earliest available data.")
    st.sidebar.markdown("### Analysis controls")
    with st.sidebar.expander("Date presets & examples"):
        st.sidebar.button("Today", on_click=preset, args=(date.today(),), width="stretch")
        st.sidebar.button("Previous month-end", on_click=preset,
                          args=((date.today().replace(day=1) - pd.Timedelta(days=1)),), width="stretch")
        st.sidebar.button("October 5 lab checkpoint", on_click=preset, args=(date(2026, 10, 5),), width="stretch")
        st.sidebar.button("Payroll revisions demo", on_click=preset,
                          args=(date(2025, 1, 15), True), width="stretch")
    st.caption(f"FRED and ALFRED, Federal Reserve Bank of St. Louis · "
               f"Access date: {date.today()} · Built with AI help · "
               "Learning demonstration, not investment advice. Actual download times appear below.")
    selected = st.sidebar.multiselect(
        "FRED series", list(NAMES), key="chosen_series",
        format_func=lambda sid: f"{sid} — {NAMES[sid]}",
    )
    extra = st.sidebar.text_input("Optional FRED series ID", placeholder="Your selected series ID", key="extra_series")
    start = st.sidebar.date_input("Custom history start", value=None, key="start_date",
                                  min_value=date(1776, 1, 1), max_value=date.today())
    vintage = st.sidebar.date_input("Vintage date", value=None, key="vintage_date",
                                    min_value=date(1776, 1, 1), max_value=date.today())
    if start is None or vintage is None:
        st.error("Choose both a start date and a vintage date.")
        return
    if start > vintage:
        st.error("Start date must be on or before the vintage date.")
        return
    if extra.strip():
        try:
            selected = list(dict.fromkeys(selected + [series_id(extra)]))
        except ValueError as error:
            st.error(str(error))
    if not selected:
        st.info("Select a series or type an ID.")
        return
    st.caption(f"Observation window: {start} onward  |  Vintage: {vintage}")
    tabs = st.tabs(selected + ["Combined chart", "Compare", "About"])
    rows = []
    downloaded = {}
    for sid, tab in zip(selected, tabs):
        with tab:
            st.subheader(NAMES.get(sid, "Total Nonfarm Payrolls" if sid == "PAYEMS" else sid))
            current = old = None
            timestamps = []
            for kind, loader in (
                ("Current", lambda: download_current(sid)),
                ("Vintage", lambda: download_vintage(sid, vintage)),
            ):
                try:
                    frame, stamp = loader()
                    timestamps.append(f"{kind}: {stamp}")
                    if kind == "Current":
                        current = frame
                    else:
                        old = frame
                except Exception as error:
                    st.error(f"{sid} {kind.lower()} unavailable: {type(error).__name__}: {error}")
            downloaded[sid] = {"Current": current, "Vintage": old}
            show_series(current, old, start, vintage, sid)
            with st.expander("Download details"):
                for stamp in timestamps:
                    st.caption(stamp)
                st.caption("UTC timestamps. Downloads are cached for up to one hour.")
            row = {"Series": f"https://fred.stlouisfed.org/series/{sid}"}
            if current is not None and old is not None:
                row.update(compare(current, old, start))
                row["Status"] = "Compared"
            else:
                row["Status"] = "Unavailable; comparison not performed"
            rows.append(row)
    with tabs[-3]:
        st.subheader("Cross-series comparison")
        chosen = st.multiselect("Series to overlay", selected, default=selected,
                                key="overlay_series")
        left, right = st.columns(2)
        with left:
            snapshot = st.radio("Data snapshot", ["Current", "Vintage"], horizontal=True)
        with right:
            scale = st.radio("Chart scale", ["Original units", "Index = 100"], horizontal=True)
        unavailable = [sid for sid in chosen if downloaded[sid][snapshot] is None]
        if unavailable:
            st.warning("Download unavailable: " + ", ".join(unavailable))
        if not chosen:
            st.info("Choose two or more series to compare, or one to inspect.")
        else:
            try:
                data, base = combined_data(
                    {sid: downloaded[sid][snapshot] for sid in chosen}, start,
                    normalize=scale == "Index = 100")
                if data.empty:
                    st.info("No downloaded observations in this window.")
                else:
                    if scale == "Original units" and not all(sid in NAMES for sid in data.columns):
                        st.warning("These series may use different units. Use Index = 100 to compare relative movement.")
                    label = "Index (base = 100)" if base is not None else (
                        "Percent" if all(sid in NAMES for sid in data.columns) else "Source units")
                    st.line_chart(data, x_label="Observation date", y_label=label, height=440,
                                  color=["#3478A4", "#BD8850", "#56988A", "#8774A4", "#A65E6C"][:len(data.columns)])
                    st.caption(f"{snapshot} data" + (f" as known on {vintage}" if snapshot == "Vintage" else "")
                               + ". Each color represents a series; hover to inspect values.")
                    if base is not None:
                        st.caption(f"Common base observation: {base.date()}. Each value / its own base value × 100. "
                                   "This is relative movement in the series, not investment performance.")
                    st.caption("Dates are aligned without filling missing values. Frequencies and publication lags may differ.")
                    with st.expander("Chart data"):
                        st.dataframe(data.sort_index(ascending=False), width="stretch")
                        st.download_button("Download combined chart data", data.to_csv().encode("utf-8"),
                                           "combined_series.csv", "text/csv")
            except ValueError as error:
                st.info(str(error))
    with tabs[-2]:
        st.subheader("Current versus vintage")
        st.dataframe(pd.DataFrame(rows), hide_index=True, column_config={
            "Series": st.column_config.LinkColumn("Series ID", display_text=r".*/series/(.*)")
        })
    with tabs[-1]:
        st.subheader("Reading this dashboard")
        st.write("Counts and latest values use the selected observation window. Later observations "
                 "follow the last vintage observation; newly available dates also include filled historical gaps. "
                 "Missing values are excluded. Revisions compare matching observation dates only.")
        st.write("A vintage is a calendar-date snapshot, not an intraday publication timestamp. "
                 "Observation age is not publication lag. Failed vintages are never replaced with current data.")
        st.markdown("Source: [FRED](https://fred.stlouisfed.org/) and "
                    "[ALFRED](https://alfred.stlouisfed.org/), Federal Reserve Bank of St. Louis, "
                    "and the original series providers.")
        st.write("Built with AI assistance (OpenAI Codex). This project is for educational and "
                 "research purposes only; not investment advice.")



def live_checks(selected=None):
    """Reproducible audit; expected values are tests, never dashboard outputs."""
    passed = True
    checks = [
        ("BAA", "2026-10-05", "2026-09-01", 6.47),
        ("FEDFUNDS", "2026-10-05", "2026-09-01", 3.75),
        ("DGS10", "2026-10-05", "2026-10-02", 5.28),
        ("MORTGAGE30US", "2026-10-05", "2026-10-01", 7.28),
        ("PAYEMS", "2025-01-15", "2024-12-01", 159536),
    ]
    for sid, vintage, expected_date, expected_value in checks:
        try:
            current, stamp = download_current(sid)
            old, old_stamp = download_vintage(sid, vintage)
            summary = compare(current, old, "2020-01-01")
            ok = latest(old) == (expected_date, expected_value)
            if sid == "PAYEMS":
                revised = float(current.loc[expected_date, "value"])
                summary["Current December 2024"] = revised
                ok = ok and revised < expected_value and summary["Changed matching dates"] > 0
            passed = passed and ok
            print(json.dumps(dict(series=sid, vintage=vintage, passed=ok,
                                  downloaded=stamp, vintage_downloaded=old_stamp, **summary)))
        except Exception as error:
            passed = False
            print(f"FAIL {sid}: {type(error).__name__}: {error}")
    if selected:
        sid = series_id(selected)
        today = date.today()
        prior = today.replace(day=1) - pd.Timedelta(days=1)
        try:
            current, stamp = download_current(sid)
            for cutoff in (prior, today):
                old, old_stamp = download_vintage(sid, cutoff)
                print(json.dumps(dict(series=sid, vintage=str(cutoff), downloaded=stamp,
                                      vintage_downloaded=old_stamp,
                                      **compare(current, old, "2020-01-01"))))
        except Exception as error:
            passed = False
            print(f"FAIL selected series: {error}")
    else:
        print("Benchmark audit only; no additional Project 2 series was specified.")
    return passed


if __name__ == "__main__":
    import sys
    if "--validate" in sys.argv:
        parser = argparse.ArgumentParser()
        parser.add_argument("--validate", action="store_true")
        parser.add_argument("--series")
        args = parser.parse_args()
        raise SystemExit(0 if live_checks(args.series) else 1)
    main()
```
