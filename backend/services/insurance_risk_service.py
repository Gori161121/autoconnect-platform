"""
Insurance Risk Service

Responsible for:
- Insurance risk scoring
- Driver insurance classification
- Premium estimation support
"""


def calculate_insurance_risk_score(
    driver_score: int,
    active_fault_codes: int,
    accident_count: int
) -> int:

    score = 100

    score -= (100 - driver_score)

    score -= active_fault_codes * 8

    score -= accident_count * 15

    return max(score, 0)


def classify_insurance_risk(
    score: int
) -> str:

    if score >= 85:
        return "LOW_RISK"

    if score >= 60:
        return "MEDIUM_RISK"

    return "HIGH_RISK"


def estimate_insurance_multiplier(
    score: int
) -> float:

    if score >= 85:
        return 0.9

    if score >= 60:
        return 1.0

    return 1.3


def build_insurance_risk_summary(
    driver_score: int,
    active_fault_codes: int,
    accident_count: int
):

    score = calculate_insurance_risk_score(
        driver_score,
        active_fault_codes,
        accident_count
    )

    return {
        "insurance_risk_score": score,
        "classification":
            classify_insurance_risk(score),
        "premium_multiplier":
            estimate_insurance_multiplier(score)
    }
