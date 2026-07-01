package com.autoconnect.android;

import java.util.List;

/** Aggregated data model backing the main dashboard screen. */
public class VehicleDashboardModel {
    public VehicleStatusModel status;
    public int healthScore;          // 0-100
    public String riskLevel;         // LOW | MEDIUM | HIGH
    public List<VehicleDiagnosticModel> diagnostics;
    public DriverBehaviorModel driverBehavior;
    public List<MaintenanceReminder> reminders;

    public VehicleDashboardModel(VehicleStatusModel status, int healthScore,
                                 String riskLevel,
                                 List<VehicleDiagnosticModel> diagnostics,
                                 DriverBehaviorModel driverBehavior,
                                 List<MaintenanceReminder> reminders) {
        this.status = status;
        this.healthScore = healthScore;
        this.riskLevel = riskLevel;
        this.diagnostics = diagnostics;
        this.driverBehavior = driverBehavior;
        this.reminders = reminders;
    }

    public boolean needsAttention() {
        if ("HIGH".equalsIgnoreCase(riskLevel)) return true;
        for (VehicleDiagnosticModel d : diagnostics) {
            if (d.isCritical()) return true;
        }
        return false;
    }
}
