"""
Vehicle Valuation Service

Responsible for:
- Vehicle market value estimation
- Depreciation analysis
- Resale value prediction
"""


def estimate_vehicle_value(
    original_price: float,
    age_years: int,
    mileage: int,
    health_score: int
) -> float:

    value = original_price

    value *= max(
        0.25,
        (1 - (age_years * 0.08))
    )

    if mileage > 200000:
        value *= 0.8
    elif mileage > 120000:
        value *= 0.9

    value *= (health_score / 100)

    return round(value, 2)


def classify_vehicle_value(
    estimated_value: float,
    original_price: float
) -> str:

    ratio = estimated_value / original_price

    if ratio >= 0.7:
        return "HIGH_RESALE_VALUE"

    if ratio >= 0.4:
        return "MODERATE_RESALE_VALUE"

    return "LOW_RESALE_VALUE"


def build_vehicle_valuation_summary(
    original_price: float,
    age_years: int,
    mileage: int,
    health_score: int
):

    estimated_value = estimate_vehicle_value(
        original_price,
        age_years,
        mileage,
        health_score
    )

    return {
        "estimated_value": estimated_value,
        "classification":
            classify_vehicle_value(
                estimated_value,
                original_price
            )
    }
