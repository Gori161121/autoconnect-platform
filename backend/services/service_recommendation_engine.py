"""
Service Recommendation Engine

Responsible for:
- Ranking service providers
- Matching vehicle issues with suitable service centers
- Generating service recommendations
"""


def calculate_provider_score(
    rating: float,
    distance_km: float,
    specialization_match: bool,
    estimated_price: float
) -> float:

    score = 0

    score += rating * 20

    if specialization_match:
        score += 25

    if distance_km <= 5:
        score += 20
    elif distance_km <= 15:
        score += 10

    if estimated_price <= 100:
        score += 15
    elif estimated_price <= 250:
        score += 8

    return round(score, 2)


def recommend_service_provider(providers: list) -> dict:

    if not providers:
        return {
            "provider": None,
            "reason": "No providers available"
        }

    ranked = sorted(
        providers,
        key=lambda provider: calculate_provider_score(
            provider["rating"],
            provider["distance_km"],
            provider["specialization_match"],
            provider["estimated_price"]
        ),
        reverse=True
    )

    best_provider = ranked[0]

    return {
        "provider": best_provider["name"],
        "score": calculate_provider_score(
            best_provider["rating"],
            best_provider["distance_km"],
            best_provider["specialization_match"],
            best_provider["estimated_price"]
        ),
        "reason": "Best match based on rating, distance, specialization and estimated price."
    }
