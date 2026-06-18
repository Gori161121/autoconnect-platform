# Diagnostics Rules

## Purpose

This document defines how AutoConnect interprets vehicle diagnostic data and converts raw signals into actionable vehicle intelligence.

---

## Vehicle Types

AutoConnect supports multiple vehicle categories:

- ICE vehicles
- Hybrid vehicles
- Electric vehicles

---

## ICE Vehicle Rules

Relevant signals:

- RPM
- engine temperature
- battery voltage
- check engine status
- OBD fault codes

Risk indicators:

- active check engine status
- high engine temperature
- low battery voltage
- high-severity diagnostic codes

---

## EV Vehicle Rules

Relevant signals:

- battery health
- state of charge
- estimated range
- battery temperature
- charging cycles

Risk indicators:

- battery health below target
- high battery temperature
- high charging cycle count
- reduced estimated range

---

## Hybrid Vehicle Rules

Relevant signals:

- fuel consumption
- electric range
- battery usage
- engine temperature

Risk indicators:

- high fuel consumption
- low electric range
- inefficient battery usage
- high engine temperature

---

## Diagnostic Severity

Severity levels:

- LOW
- MEDIUM
- HIGH
- UNKNOWN

---

## Decision Logic

Diagnostic events are used by:

- Vehicle Health Service
- Maintenance Prediction Service
- Insurance Risk Service
- Vehicle Intelligence Engine

---

## End Goal

Transform vehicle signals into understandable diagnostics, risks, and maintenance recommendations.
