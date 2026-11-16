"""Download Yahoo monthly Adj Close data for the Lab 14 fund universe.

Saves original responses and a validated JSON table for CSV export.
61 monthly price observations allow 60 monthly returns (five years).
"""
from datetime import datetime, timezone
import calendar
import json
import math
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

TICKERS = ["BIL", "IEF", "LQD", "VT"]
START = datetime(2021, 9, 1, tzinfo=timezone.utc)
END = datetime(2026, 10, 1, tzinfo=timezone.utc)  # Exclusive; omit incomplete October.
HERE = Path(__file__).resolve().parent


def main():
    raw = HERE / "sources"
    raw.mkdir(exist_ok=True)
    series = {}
    sources = []
    for ticker in TICKERS:
        query = urlencode({"period1": int(START.timestamp()), "period2": int(END.timestamp()),
                           "interval": "1mo", "includeAdjustedClose": "true"})
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?{query}"
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(request, timeout=30) as response:
            data = json.load(response)
        if data["chart"]["error"]:
            raise ValueError(data["chart"]["error"])
        result = data["chart"]["result"][0]
        adjusted = result["indicators"]["adjclose"][0]["adjclose"]
        assert len(adjusted) == len(result["timestamp"])
        values = {}
        for timestamp, price in zip(result["timestamp"], adjusted):
            date = datetime.fromtimestamp(timestamp, timezone.utc)
            if not START <= date < END:
                continue
            key = date.strftime("%Y-%m")
            if key in values or price is None or not math.isfinite(price) or price <= 0:
                raise ValueError(f"{ticker}: missing, duplicate or invalid price in {key}")
            values[key] = price
        expected = [f"{year}-{month:02d}" for year in range(2021, 2027)
                    for month in range(1, 13) if "2021-09" <= f"{year}-{month:02d}" <= "2026-09"]
        if sorted(values) != expected:
            raise ValueError(f"{ticker}: expected 61 consecutive months; got {len(values)}")
        series[ticker] = values
        (raw / f"{ticker}_monthly.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
        sources.append({"ticker": ticker, "url": url,
                        "downloaded_at_utc": datetime.now(timezone.utc).isoformat(),
                        "field": "indicators.adjclose[0].adjclose", "observations": len(values)})
        print(f"{ticker}: {len(values)} monthly Adj Close observations validated")
    rows = [["Date"] + TICKERS]
    for key in sorted(series[TICKERS[0]]):
        year, month = map(int, key.split("-"))
        date = f"{key}-{calendar.monthrange(year, month)[1]:02d}"
        rows.append([date] + [series[ticker][key] for ticker in TICKERS])
    (raw / "prices_table.json").write_text(json.dumps(rows), encoding="utf-8")
    (raw / "download_metadata.json").write_text(json.dumps(sources, indent=2), encoding="utf-8")
    print("Saved validated table: 2021-09-30 to 2026-09-30; month-end labels.")


if __name__ == "__main__":
    main()
