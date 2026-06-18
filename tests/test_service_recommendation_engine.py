from backend.services.service_recommendation_engine import (
    calculate_provider_score,
    recommend_service_provider
)


def test_provider_score():
    score = calculate_provider_score(
        rating=4.8,
        distance_km=4,
        specialization_match=True,
        estimated_price=180
    )

    assert score > 0


def test_recommend_service_provider():
    providers = [
        {
            "name": "AutoFix Service",
            "rating": 4.8,
            "distance_km": 4,
            "specialization_match": True,
            "estimated_price": 180
        },
        {
            "name": "Basic Garage",
            "rating": 3.8,
            "distance_km": 20,
            "specialization_match": False,
            "estimated_price": 300
        }
    ]

    result = recommend_service_provider(providers)

    assert result["provider"] == "AutoFix Service"
