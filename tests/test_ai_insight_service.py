import os

from backend.services.ai_insight_service import generate_vehicle_insight


def _no_api_key():
    os.environ.pop("OPENAI_API_KEY", None)


SAMPLE = {
    "vehicle": {"make": "Audi", "model": "A3", "year": 2019, "mileage": 128450},
    "diagnostics": {
        "status": "SERVICE_RECOMMENDED",
        "faults": [
            {
                "code": "P0420",
                "description": "Catalyst System Efficiency Below Threshold (Bank 1)",
                "system": "Emissions",
                "severity": "MEDIUM",
                "recommended_action": "Inspect catalytic converter",
            }
        ],
    },
    "health": {"health_score": 81, "risk_level": "MEDIUM"},
}


def test_insight_fallback_without_key():
    _no_api_key()
    result = generate_vehicle_insight(SAMPLE)
    assert result["generated_with"] == "rule-based-fallback"
    assert "Audi" in result["summary"]
    assert isinstance(result["recommendations"], list)
    assert len(result["recommendations"]) >= 1


def test_insight_handles_no_faults():
    _no_api_key()
    data = {
        "vehicle": {"make": "Tesla", "model": "Model 3", "year": 2021, "mileage": 84500},
        "diagnostics": {"status": "HEALTHY", "faults": []},
        "health": {"health_score": 95, "risk_level": "LOW"},
    }
    result = generate_vehicle_insight(data)
    assert result["generated_with"] == "rule-based-fallback"
    assert "No active fault codes" in result["summary"]


def test_insight_flags_high_severity():
    _no_api_key()
    data = {
        "vehicle": {"make": "Toyota", "model": "Prius", "year": 2018, "mileage": 142000},
        "diagnostics": {
            "status": "CRITICAL_ATTENTION_REQUIRED",
            "faults": [
                {"code": "P0300", "description": "Misfire", "system": "Engine",
                 "severity": "HIGH", "recommended_action": "Inspect ignition"}
            ],
        },
        "health": {"health_score": 60, "risk_level": "HIGH"},
    }
    result = generate_vehicle_insight(data)
    joined = " ".join(result["recommendations"])
    assert "P0300" in joined
