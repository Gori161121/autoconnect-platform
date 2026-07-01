"""AutoConnect — Vehicle Intelligence dashboard.

Reads from the FastAPI backend and visualises fleet health, diagnostics,
driver behaviour and the AI-generated insight for a selected vehicle.

Run:  streamlit run dashboard/app.py
Env:  API_URL (default http://localhost:8000)
"""
from __future__ import annotations

import os

import httpx
import pandas as pd
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="AutoConnect", page_icon="🚗", layout="wide")


@st.cache_data(ttl=30)
def get(path: str):
    r = httpx.get(f"{API_URL}{path}", timeout=15)
    r.raise_for_status()
    return r.json()


st.title("🚗 AutoConnect — Vehicle Intelligence")
st.caption("Diagnostics · Health · Driver behaviour · AI insight")

try:
    vehicles = get("/vehicles")
except Exception as exc:  # noqa: BLE001
    st.error(f"Cannot reach the API at {API_URL}. Is the backend running?\n\n{exc}")
    st.stop()

labels = {f"{v['year']} {v['make']} {v['model']} ({v['vehicle_type']})": v["id"] for v in vehicles}
choice = st.sidebar.selectbox("Select vehicle", list(labels.keys()))
vehicle_id = labels[choice]

health = get(f"/vehicles/{vehicle_id}/health")
diagnostics = get(f"/vehicles/{vehicle_id}/diagnostics")
driver = get(f"/vehicles/{vehicle_id}/driver-behavior")
insight = get(f"/vehicles/{vehicle_id}/ai-insight")

c1, c2, c3 = st.columns(3)
c1.metric("Health score", health.get("health_score", "—"))
c2.metric("Risk level", health.get("risk_level", "—"))
c3.metric("Diagnostic status", diagnostics.get("status", "—"))

st.divider()
st.subheader("🤖 AI Insight")
st.write(insight.get("summary", ""))
for rec in insight.get("recommendations", []):
    st.markdown(f"- {rec}")
st.caption(f"Generated with: {insight.get('generated_with', 'n/a')}")

st.divider()
left, right = st.columns(2)

with left:
    st.subheader("Diagnostics")
    faults = diagnostics.get("faults", [])
    if faults:
        st.dataframe(pd.DataFrame(faults), use_container_width=True, hide_index=True)
    else:
        st.success("No active fault codes.")

with right:
    st.subheader("Driver behaviour")
    st.metric("Driver score", driver.get("driver_score", "—"))
    st.write(f"Classification: **{driver.get('classification', 'n/a')}**")
    st.json({
        "hard_brakes": driver.get("hard_brakes"),
        "rapid_accelerations": driver.get("rapid_accelerations"),
        "overspeed_events": driver.get("overspeed_events"),
    })
