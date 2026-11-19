"""FIN 43900 Lab 13: five checkable mandate rules; standard library only."""

from math import isclose

# Editable inputs: dollars, business days, and percentage-point weights.
PORTFOLIO_SIZE = 100_000_000
QUARTERLY_DISTRIBUTION = 750_000
RESERVE_QUARTERS = 4
LIQUIDITY_WINDOW = 5
MIN_LIQUID_SHARE = 90
MAX_COMPANY_EXPOSURE = 8
EXEMPT_ISSUERS = {None, "U.S. Treasury", "diversified fund"}

# Holding: (issuer, business days to redeem, reserve eligible)
HOLDINGS = {
    "Cash": (None, 0, True),
    "Treasury bills": ("U.S. Treasury", 1, True),
    "Treasury 10-year note": ("U.S. Treasury", 1, True),
    "Global equity index fund": ("diversified fund", 2, False),
    "Investment-grade bond fund": ("diversified fund", 3, False),
    "Private real estate fund": ("diversified fund", 90, False),
    "Acme Corp bonds": ("Acme Corp", 4, False),
    "Acme Corp stock": ("Acme Corp", 1, False),
}
# Weights follow HOLDINGS order; include zero allocations explicitly.
CANDIDATES = {
    "A": [2, 2, 10, 60, 26, 0, 0, 0],
    "B": [1, 0, 0, 55, 20, 15, 5, 4],
    "C": [1, 1, 0, 70, 20, 0, 0, 8],
    "D": [0, 0, 100, 0, 0, 0, 0, 0],
    "E": [0, 0, 0, 60, 40, 0, 0, 0],  # Lab 14 benchmark.
}


def reserve_minimum():
    """Required reserve as a percentage of the portfolio."""
    return QUARTERLY_DISTRIBUTION * RESERVE_QUARTERS / PORTFOLIO_SIZE * 100


def evaluate(weights):
    """Return (label, measured percentage, passed) for each checkable rule."""
    if len(weights) != len(HOLDINGS):
        raise ValueError("Provide one weight for every permitted holding.")
    total = sum(weights)
    minimum = min(weights)
    reserve = 0
    liquid = 0
    companies = {}
    for (issuer, days, eligible), weight in zip(HOLDINGS.values(), weights):
        if eligible:
            reserve += weight
        if days <= LIQUIDITY_WINDOW:
            liquid += weight
        if issuer not in EXEMPT_ISSUERS:
            companies[issuer] = companies.get(issuer, 0) + weight
    largest = max(companies.values(), default=0)
    return [
        ("Weight total", total, isclose(total, 100, rel_tol=0, abs_tol=1e-9)),
        ("Minimum weight", minimum, minimum >= 0),
        ("Reserve", reserve, reserve >= reserve_minimum()),
        ("Five-day liquidity", liquid, liquid >= MIN_LIQUID_SHARE),
        ("Largest company", largest, largest <= MAX_COMPANY_EXPOSURE),
    ]


def main():
    print(f"Reserve minimum: {reserve_minimum():.1f}%")
    for name, weights in CANDIDATES.items():
        print(f"\nCandidate {name}")
        checks = evaluate(weights)
        for label, value, passed in checks:
            print(f"{label}: {value:.1f}% {'pass' if passed else 'FAIL'}")
        # S9 has no numerical interpretation until the CIO clarifies it.
        print("requires CIO clarification")
        failures = sum(not passed for _, _, passed in checks)
        print("passes every checkable rule" if failures == 0
              else f"fails {failures} rule(s)")


if __name__ == "__main__":
    main()
