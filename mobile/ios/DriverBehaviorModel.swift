import Foundation

/// Driver behaviour metrics and derived score.
struct DriverBehaviorModel: Codable {
    let hardBrakes: Int
    let rapidAccelerations: Int
    let overspeedEvents: Int
    let driverScore: Int
    let classification: String  // SAFE | MODERATE | RISKY

    enum CodingKeys: String, CodingKey {
        case hardBrakes = "hard_brakes"
        case rapidAccelerations = "rapid_accelerations"
        case overspeedEvents = "overspeed_events"
        case driverScore = "driver_score"
        case classification
    }
}
