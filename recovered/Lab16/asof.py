"""FIN 43900 Lab 16: point-in-time provenance gate; standard library only.

This project is for educational and research purposes only.
"""

# Editable inputs. Row IDs permanently identify original records.
DECISION_DATE = '2026-03-31'
TRAINING_TABLE = """row_id,ticker,month_measured,published_on,price
1,AAA,2026-01,2026-02-10,101.0
2,AAA,2026-02,2026-03-10,104.0
3,AAA,2026-03,2026-04-10,109.0
4,AAA,2026-02,2026-03-25,103.0
5,BBB,2026-01,2026-02-10,98.0
6,BBB,2026-02,2026-03-10,97.0
7,BBB,2026-02,2026-03-10,97.0
8,BBB,2026-03,2026-04-10,92.0
9,CCC,2026-01,2026-02-10,110.0
10,CCC,2026-02,2026-04-05,112.0
11,,2026-02,2026-03-10,99.0
12,CCC,2026-02,2026-03-10,111.0
"""

import csv
from datetime import date
from io import StringIO


def read_records(table=TRAINING_TABLE):
    records = list(csv.DictReader(StringIO(table)))
    for row in records:
        row['row_id'] = int(row['row_id'])
        row['price'] = float(row['price'])
    return records


def quarantine(records):
    """Rule 1: None, missing keys, empty strings and whitespace are blank."""
    return [dict(r) for r in records if r.get('ticker') and r['ticker'].strip()]


def deduplicate(records):
    """Rule 2: compare data fields; lowest original ID wins, not list order."""
    seen = set()
    kept = []
    for row in sorted(records, key=lambda r: r['row_id']):
        key = (row['ticker'], row['month_measured'], row['published_on'], row['price'])
        if key not in seen:
            seen.add(key)
            kept.append(dict(row))
    return kept


def latest_vintages(records):
    """Rule 4: latest publication per ticker/month; tied dates use lowest ID."""
    winners = {}
    for row in records:
        key = (row['ticker'], row['month_measured'])
        rank = (date.fromisoformat(row['published_on']), -row['row_id'])
        if key not in winners or rank > winners[key][0]:
            winners[key] = (rank, dict(row))
    return [winners[key][1] for key in sorted(winners)]


def asof_panel(records, decision_date):
    cutoff = date.fromisoformat(decision_date)
    current = list(records)
    funnel = []
    rules = (
        quarantine,
        deduplicate,
        lambda rows: [r for r in rows if date.fromisoformat(r['published_on']) <= cutoff],
        latest_vintages,
    )
    for rule in rules:
        kept = rule(current)
        kept_ids = {r['row_id'] for r in kept}
        removed = sorted(r['row_id'] for r in current if r['row_id'] not in kept_ids)
        funnel.append({'before': len(current), 'after': len(kept), 'removed': removed})
        current = kept
    return current, funnel


def naive_panel(records):
    # Start independently from ORIGINAL records. Reusing the as-of panel would
    # lose future releases/revisions and hide the very look-ahead bias we test.
    return latest_vintages(deduplicate(quarantine(records)))


def signals(panel):
    """Fund return: price change between last two available months, not annualized."""
    grouped = {}
    for row in panel:
        grouped.setdefault(row['ticker'], []).append(row)
    result = {}
    for ticker, rows in sorted(grouped.items()):
        rows = sorted(rows, key=lambda r: r['month_measured'])
        latest = rows[-1]
        value, reason = None, 'insufficient history'
        if len(rows) >= 2:
            previous = rows[-2]['price']
            if previous == 0:
                reason = 'previous price is zero'
            else:
                value = (latest['price'] / previous - 1) * 100
                reason = ''
        result[ticker] = {'month': latest['month_measured'], 'percent': value, 'reason': reason}
    return result


def format_signal(signal):
    if signal is None:
        return 'N/A (no available observations)'
    month = date.fromisoformat(signal['month'] + '-01').strftime('%B %Y')
    value = signal['percent']
    return (f'{value:+.2f}%, {month}' if value is not None
            else f"N/A ({signal['reason']}), {month}")


def main():
    records = read_records()
    panel, funnel = asof_panel(records, DECISION_DATE)
    naive = naive_panel(records)
    print(f'Decision date: {DECISION_DATE}\nROW FUNNEL')
    for number, step in enumerate(funnel, 1):
        print(f"Rule {number}: {step['before']} -> {step['after']}; "
              f"removed {len(step['removed'])}; original rows {step['removed']}")
    print('\nAS-OF PANEL\n row  ticker  month     published    price')
    for r in panel:
        print(f"{r['row_id']:4}  {r['ticker']:6}  {r['month_measured']}  "
              f"{r['published_on']}  {r['price']:7.1f}")
    actual, biased = signals(panel), signals(naive)
    print('\nSIGNALS (fund returns from price changes, %)')
    print(f"{'Ticker':8} {'AS-OF':30} NAIVE (includes later publications/revisions)")
    for ticker in sorted(set(actual) | set(biased)):
        print(f'{ticker:8} {format_signal(actual.get(ticker)):30} {format_signal(biased.get(ticker))}')


if __name__ == '__main__':
    main()
