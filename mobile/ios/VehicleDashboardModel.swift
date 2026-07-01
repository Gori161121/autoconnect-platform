import Foundation

/// Aggregated data model backing the main dashboard screen.
struct VehicleDashboardModel {
    let status: VehicleStatusModel
    let healthScore: Int
    let riskLevel: String  // LOW | MEDIUM | HIGH
    let diagnostics: [VehicleDiagnosticModel]
    let driverBehavior: DriverBehaviorModel?
    let reminders: [MaintenanceReminder]

    var needsAttention: Bool {
        if riskLevel.uppercased() == "HIGH" { return true }
        return diagnostics.contains { $0.isCritical }
    }
}
