import Foundation

/// A single diagnostic trouble code (DTC) result.
struct VehicleDiagnosticModel: Codable, Identifiable {
    var id: String { code }
    let code: String
    let description: String
    let system: String
    let severity: String  // HIGH | MEDIUM | LOW | UNKNOWN
    let recommendedAction: String

    enum CodingKeys: String, CodingKey {
        case code, description, system, severity
        case recommendedAction = "recommended_action"
    }

    var isCritical: Bool { severity.uppercased() == "HIGH" }
}
