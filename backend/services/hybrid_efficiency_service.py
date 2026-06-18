"""
Hybrid Efficiency Service

Responsible for:
- Hybrid fuel/electric efficiency analysis
- Energy balance scoring
- Hybrid driving mode evaluation
"""


def calculate_hybrid_efficiency_score(
    fuel_consumption_l_100km: float,
    electric_range_km: int,
    battery_usage_percent: int
) -> int:

    score = 100

    if fuel_consumption_l_100km > 7:
        score -= 20
    elif fuel_consumption_l_100km > 5:
        score -= 10

    if electric_range_km < 30:
        score -= 15

    if battery_usage_percent < 30:
        score -= 10

    return max(score, 0)


def classify_hybrid_efficiency(score: int) -> str:

    if score >= 85:
        return "EFFICIENT"

    if score >= 65:
        return "AVERAGE"

    return "INEFFICIENT"


def build_hybrid_efficiency_summary(
    fuel_consumption_l_100km: float,
    electric_range_km: int,
    battery_usage_percent: int
) -> dict:

    score = calculate_hybrid_efficiency_score(
        fuel_consumption_l_100km,
        electric_range_km,
        battery_usage_percent
    )

    return {
        "hybrid_efficiency_score": score,
        "classification": classify_hybrid_efficiency(score),
        "fuel_consumption_l_100km": fuel_consumption_l_100km,
        "electric_range_km": electric_range_km,
        "battery_usage_percent": battery_usage_percent
    }
