from backend.services.hybrid_efficiency_service import (
    calculate_hybrid_efficiency_score,
    classify_hybrid_efficiency,
    build_hybrid_efficiency_summary
)


def test_hybrid_efficiency_score():
    result = calculate_hybrid_efficiency_score(
        fuel_consumption_l_100km=4.8,
        electric_range_km=45,
        battery_usage_percent=70
    )

    assert result == 100


def test_hybrid_efficiency_classification():
    assert classify_hybrid_efficiency(90) == "EFFICIENT"
    assert classify_hybrid_efficiency(70) == "AVERAGE"
    assert classify_hybrid_efficiency(50) == "INEFFICIENT"


def test_hybrid_efficiency_summary():
    result = build_hybrid_efficiency_summary(
        fuel_consumption_l_100km=6.2,
        electric_range_km=25,
        battery_usage_percent=40
    )

    assert result["classification"] == "AVERAGE"
