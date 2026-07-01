package com.autoconnect.android;

/** A single diagnostic trouble code (DTC) result. */
public class VehicleDiagnosticModel {
    public String code;
    public String description;
    public String system;
    public String severity; // HIGH | MEDIUM | LOW | UNKNOWN
    public String recommendedAction;

    public VehicleDiagnosticModel(String code, String description, String system,
                                  String severity, String recommendedAction) {
        this.code = code;
        this.description = description;
        this.system = system;
        this.severity = severity;
        this.recommendedAction = recommendedAction;
    }

    public boolean isCritical() {
        return "HIGH".equalsIgnoreCase(severity);
    }
}
