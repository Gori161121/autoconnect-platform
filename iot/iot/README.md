# IoT / OBD Device Layer

This directory contains prototype C++ components for the vehicle telemetry layer.

The purpose of this layer is not to implement a production OBD-II device.  
It exists to show how AutoConnect separates low-level vehicle signal collection from backend intelligence services.

---

## Role in AutoConnect

```text
Vehicle
   ↓
OBD / IoT Device
   ↓
Telemetry Parsing
   ↓
Diagnostic Preprocessing
   ↓
Backend Vehicle Intelligence Engine
   ↓
Mobile Application
```

---

## Components

### `obd_device_simulator.cpp`

Simulates telemetry output from a connected vehicle device.

Example signals:

- VIN
- mileage
- RPM
- engine temperature
- battery voltage
- check engine status
- fault code

---

### `telemetry_parser.cpp`

Analyzes raw telemetry values and detects basic alerts.

Detected alerts:

- engine temperature critical
- battery voltage low
- check engine active

---

### `diagnostic_code_mapper.cpp`

Maps diagnostic fault codes to:

- vehicle system
- severity
- description

This mirrors the backend diagnostics logic at a simplified device-simulation level.

---

## Why C++?

C++ is used here because embedded and automotive device layers commonly require low-level control, efficient memory usage, and direct interaction with hardware or telemetry streams.

In this prototype, C++ represents the device-side simulation layer, while Python represents the backend intelligence layer.

---

## Current Limitations

This is a simulation layer only.

It does not currently implement:

- real CAN bus communication
- real OBD-II protocol frames
- Bluetooth / BLE communication
- serial port communication
- physical hardware integration

These are future engineering directions.

---

## Future Improvements

Possible extensions:

- CAN frame parser
- serial port telemetry reader
- BLE device communication mock
- real-time telemetry stream simulator
- DTC mapping shared with backend knowledge base
