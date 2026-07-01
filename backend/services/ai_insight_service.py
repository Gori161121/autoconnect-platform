"""
AI Insight Service

Explains a vehicle's diagnostics and health in plain, owner-friendly language.
Uses OpenAI (gpt-4o-mini) when OPENAI_API_KEY is set, otherwise a rule-based
fallback so the endpoint works without an API key.
"""

import os
import json


def _rule_based_insight(data: dict) -> dict:
    vehicle = data.get("vehicle", {})
    diagnostics = data.get("diagnostics", {})
    health = data.get("health", {})

    faults = diagnostics.get("faults", [])
    status = diagnostics.get("status", "UNKNOWN")
    risk = health.get("risk_level", "UNKNOWN")
    score = health.get("health_score", "n/a")

    name = f"{vehicle.get('year', '')} {vehicle.get('make', '')} {vehicle.get('model', '')}".strip()
    mileage = vehicle.get("mileage", 0)

    if faults:
        fault_sentences = "; ".join(
            f"{f.get('code')} — {f.get('description')} ({f.get('severity')})"
            for f in faults
        )
    else:
        fault_sentences = "No active fault codes."

    recommendations = []
    for f in faults:
        if f.get("severity") == "HIGH":
            recommendations.append(
                f"{f.get('code')}: {f.get('recommended_action', 'Service soon')} — address promptly."
            )
        elif f.get("severity") == "MEDIUM":
            recommendations.append(
                f"{f.get('code')}: {f.get('recommended_action', 'Schedule a check')}."
            )
    if risk in ("HIGH", "CRITICAL"):
        recommendations.append("Overall health is a concern — book a full inspection.")
    if not recommendations:
        recommendations.append("No urgent action. Keep up regular maintenance.")

    summary = (
        f"Your {name} ({mileage:,} km) has a health score of {score} "
        f"({risk} risk). Diagnostic status: {status}. {fault_sentences}"
    )

    return {
        "summary": summary,
        "recommendations": recommendations,
        "generated_with": "rule-based-fallback",
    }


def _openai_insight(data: dict) -> dict:
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    prompt = (
        "You are a car diagnostics assistant. Explain this vehicle's condition "
        "to a non-technical owner. Return JSON with keys 'summary' (2-3 sentences, "
        "plain language) and 'recommendations' (array of 2-4 short actions).\n\n"
        f"{json.dumps(data)}"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.4,
    )

    result = json.loads(response.choices[0].message.content)
    result["generated_with"] = "openai"
    return result


def generate_vehicle_insight(data: dict) -> dict:
    """Return a plain-language insight. Uses OpenAI if configured, else fallback."""
    if os.getenv("OPENAI_API_KEY"):
        try:
            return _openai_insight(data)
        except Exception:
            return _rule_based_insight(data)
    return _rule_based_insight(data)
