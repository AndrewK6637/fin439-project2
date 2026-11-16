"""Lab 14 portfolio baselines. Standard library only; rates are decimals."""

import math
import sys

# Editable annual course-authored training inputs, not market estimates.
# name: (expected return, volatility)
okayhow SLEEVES = {
    "Treasury bills": (0.035, 0.005),
    "Treasury 10-year note": (0.043, 0.070),
    "Investment-grade bond fund": (0.050, 0.060),
    "Global equity index fund": (0.080, 0.160),
}
# Rows and columns follow SLEEVES order.
CORRELATIONS = [
    [1.00, 0.10, 0.05, 0.00],
    [0.10, 1.00, 0.80, -0.10],
    [0.05, 0.80, 1.00, 1.30],
    [0.00, -0.10, 1.30, 1.00],
]
OBJECTIVE_RETURN = 0.065  # Estimated CPI 2.5% + mandate objective 4%.
RESERVE_ELIGIBLE = {"Treasury bills", "Treasury 10-year note"}
BENCHMARK = {"Investment-grade bond fund": 0.40,
             "Global equity index fund": 0.60}


def validate_inputs(sleeves, correlations, objective):
    """Reject malformed inputs before printing any portfolio results."""
    n = len(sleeves)
    if not n or len(correlations) != n or any(len(row) != n for row in correlations):
        raise ValueError("Correlation table must have one row and column per sleeve.")
    if not math.isfinite(objective):
        raise ValueError("Objective return must be finite.")
    for name, (expected, volatility) in sleeves.items():
        if not math.isfinite(expected) or not math.isfinite(volatility) or volatility <= 0:
            raise ValueError(f"{name}: return must be finite and volatility positive and finite.")
    for i in range(n):
        for j in range(n):
            rho = correlations[i][j]
            if not math.isfinite(rho) or not -1 <= rho <= 1:
                raise ValueError(f"Correlation [{i + 1},{j + 1}] must be between -1 and 1; got {rho}.")
            if not math.isclose(rho, correlations[j][i], rel_tol=0, abs_tol=1e-12):
                raise ValueError(f"Correlation table is not symmetric at [{i + 1},{j + 1}].")
        if not math.isclose(correlations[i][i], 1, rel_tol=0, abs_tol=1e-12):
            raise ValueError("Each diagonal correlation must equal 1.")


def covariance_matrix(sleeves, correlations):
    """Cov(i,j) = correlation(i,j) * sigma(i) * sigma(j)."""
    validate_inputs(sleeves, correlations, 0)
    volatilities = [values[1] for values in sleeves.values()]
    return [[correlations[i][j] * volatilities[i] * volatilities[j]
             for j in range(len(sleeves))] for i in range(len(sleeves))]


def equal_weights(sleeves):
    return [1 / len(sleeves)] * len(sleeves)


def inverse_volatility_weights(sleeves):
    inverse = [1 / values[1] for values in sleeves.values()]
    total = sum(inverse)
    return [value / total for value in inverse]


def define_portfolios(sleeves):
    if not BENCHMARK.keys() <= sleeves.keys():
        raise ValueError("Benchmark holdings must be present in SLEEVES.")
    return {
        "Benchmark": [BENCHMARK.get(name, 0) for name in sleeves],
        "Equal weight": equal_weights(sleeves),
        "Inverse volatility": inverse_volatility_weights(sleeves),
    }


def validate_weights(weights, count):
    if len(weights) != count or any(not math.isfinite(w) or w < 0 for w in weights):
        raise ValueError("Provide one finite, nonnegative weight per sleeve.")
    if not math.isclose(sum(weights), 1, rel_tol=0, abs_tol=1e-12):
        raise ValueError("Portfolio weights must sum to 100%.")


def expected_return(weights, sleeves):
    validate_weights(weights, len(sleeves))
    return sum(weight * values[0] for weight, values in zip(weights, sleeves.values()))


def portfolio_variance(weights, covariance):
    validate_weights(weights, len(covariance))
    if any(len(row) != len(weights) for row in covariance):
        raise ValueError("Covariance matrix dimensions must match weights.")
    variance = 0.0
    for i in range(len(weights)):
        for j in range(len(weights)):
            variance += weights[i] * weights[j] * covariance[i][j]
    return variance


def portfolio_volatility(weights, covariance):
    variance = portfolio_variance(weights, covariance)
    if not math.isfinite(variance) or variance < -1e-12:
        raise ValueError("Invalid portfolio variance; check the covariance inputs.")
    return math.sqrt(max(variance, 0.0))


def reserve_weight(weights, sleeves, eligible):
    validate_weights(weights, len(sleeves))
    return sum(weight for name, weight in zip(sleeves, weights) if name in eligible)


def meets_objective(expected, objective):
    return expected >= objective or math.isclose(expected, objective, rel_tol=0, abs_tol=1e-12)


def main():
    validate_inputs(SLEEVES, CORRELATIONS, OBJECTIVE_RETURN)
    covariance = covariance_matrix(SLEEVES, CORRELATIONS)
    print(f"Annual course training inputs; objective: {OBJECTIVE_RETURN:.2%}.")
    print("Weights in order: " + " / ".join(SLEEVES))
    print("Portfolio | Weights (%) | Return | Volatility | Reserve-eligible | Meets objective?")
    for name, weights in define_portfolios(SLEEVES).items():
        expected = expected_return(weights, SLEEVES)
        volatility = portfolio_volatility(weights, covariance)
        reserve = reserve_weight(weights, SLEEVES, RESERVE_ELIGIBLE)
        formatted = " / ".join(f"{w * 100:.1f}" for w in weights)
        verdict = "yes" if meets_objective(expected, OBJECTIVE_RETURN) else "no"
        print(f"{name} | {formatted} | {expected:.2%} | {volatility:.2%} | {reserve:.1%} | {verdict}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Cannot run portfolio engine: {error}", file=sys.stderr)
        sys.exit(1)
