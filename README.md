# AutoConnect — Connected Vehicle Intelligence Platform

![CI](https://github.com/Gori161121/autoconnect-platform/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.11-blue)

AutoConnect turns raw vehicle telemetry (OBD-II) into useful intelligence:
diagnostics, a composite health score, maintenance prediction, driver-behaviour
analytics, ownership cost, and a plain-language AI explanation of what's wrong
and what to do about it.

It's not a booking app or a mechanic finder — the focus is understanding the
vehicle. Inspired by ideas from Tesla App, FIXD and Carly, built as an original
prototype.

```
OBD-II telemetry → DTC decode → health score → risk + prediction → AI insight
```

## Features

- **Diagnostics** driven by a real SAE DTC knowledge base (45 codes: P/C/B/U)
- **Vehicle health score** — composite of diagnostic, maintenance and mileage scores
- **Maintenance prediction** with urgency levels
- **Driver-behaviour** scoring and **insurance-risk** estimation
- **EV battery** and **hybrid efficiency** analysis (per powertrain type)
- **Ownership cost** analytics
- **AI insight** — explains a vehicle's condition in plain language (OpenAI, with a rule-based fallback so it runs without a key)
- **Streamlit dashboard** for a visual view of any vehicle
- **IoT edge (C++)** — OBD device simulator, telemetry parser, DTC mapper
- **Mobile clients** — Android (Java) and iOS (Swift) models + API client
- Tests (pytest) running in CI

## Running it

**Backend (SQLite-free, no setup — data is in-memory for the prototype):**

```bash
cd backend
pip install -r requirements.txt
uvicorn backend.main:app --reload   # run from the repo root
```

API at `http://localhost:8000`, interactive docs at `http://localhost:8000/docs`.

**With Docker:**

```bash
docker compose up --build
```

**Dashboard:**

```bash
pip install -r dashboard/requirements.txt
streamlit run dashboard/app.py       # reads API_URL (default localhost:8000)
```

**IoT edge tools (C++):**

```bash
g++ -std=c++17 iot/obd_device_simulator.cpp -o obd_sim && ./obd_sim 5
g++ -std=c++17 iot/diagnostic_code_mapper.cpp -o dtc && ./dtc P0300 P0420
```

## API

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/health` | Health check |
| GET | `/vehicles` | List fleet |
| GET | `/vehicles/{id}` | Vehicle detail |
| GET | `/vehicles/{id}/health` | Composite health score |
| GET | `/vehicles/{id}/diagnostics` | Decoded fault codes + status |
| GET | `/vehicles/{id}/maintenance-prediction` | Maintenance urgency |
| GET | `/vehicles/{id}/ev-battery` | EV battery summary (EV only) |
| GET | `/vehicles/{id}/hybrid-efficiency` | Hybrid efficiency (hybrid only) |
| GET | `/vehicles/{id}/driver-behavior` | Driver score |
| GET | `/vehicles/{id}/insurance-risk` | Insurance risk estimate |
| GET | `/vehicles/{id}/valuation` | Estimated value |
| GET | `/vehicles/{id}/intelligence-report` | Combined report |
| GET | `/vehicles/{id}/ai-insight` | Plain-language AI insight |
| GET | `/services/recommendations` | Ranked service providers |
| GET | `/ownership/cost-summary` | Ownership cost breakdown |
| GET | `/legacy/*` | Isolated legacy marketplace layer |

Example — `/vehicles/1/ai-insight`:

```json
{
  "summary": "Your 2019 Audi A3 (128,450 km) has a health score of 81 (MEDIUM risk). Diagnostic status: SERVICE_RECOMMENDED. P0420 — Catalyst System Efficiency Below Threshold (MEDIUM)",
  "recommendations": ["P0420: Inspect catalytic converter."],
  "generated_with": "rule-based-fallback"
}
```

## Project layout

```
backend/services/   diagnostics, health, maintenance, driver, EV, hybrid,
                    valuation, insurance, ownership, intelligence engine, AI insight
data/               dtc_codes.json (SAE knowledge base), vehicle & scenario payloads
iot/                C++ edge: OBD simulator, telemetry parser, DTC mapper
mobile/android/     Java models + API client
mobile/ios/         Swift models + API client
dashboard/          Streamlit app
tests/              pytest
```

## Tests

```bash
cd backend && PYTHONPATH=.. pytest -q    # or: PYTHONPATH=. pytest from repo root
```

## Roadmap

- Persist telemetry to PostgreSQL (schema in `database/`)
- Live OBD ingestion from the C++ edge simulator
- SwiftUI / Jetpack Compose UI on top of the mobile clients
- Deploy a public demo

## License

MIT — see [LICENSE](LICENSE).
