# IoT / OBD Device Layer

This directory contains prototype C++ components for the vehicle telemetry layer.

## Purpose

The IoT layer simulates how a connected vehicle device can collect and process technical vehicle data before sending it to the backend platform.

## Components

### obd_device_simulator.cpp

Simulates basic OBD/vehicle telemetry output.

### telemetry_parser.cpp

Analyzes telemetry values and detects basic alerts such as:

- high engine temperature
- low battery voltage
- active check engine status

### diagnostic_code_mapper.cpp

Maps diagnostic fault codes to system category, severity and description.

## Role in the Platform

```text
Vehicle
   ↓
OBD / IoT Device
   ↓
Telemetry Processing
   ↓
Backend Intelligence Layer
   ↓
Mobile Application
