import Foundation

/// A maintenance reminder item derived from the prediction service.
struct MaintenanceReminder: Codable, Identifiable {
    var id: String { title }
    let title: String
    let urgency: String  // LOW | MEDIUM | HIGH
    let detail: String

    var isUrgent: Bool { urgency.uppercased() == "HIGH" }
}
