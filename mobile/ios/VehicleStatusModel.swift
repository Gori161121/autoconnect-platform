import Foundation

/// Overall status of a vehicle shown on the dashboard.
struct VehicleStatusModel: Codable, Identifiable {
    let id: Int
    let vin: String
    let make: String
    let model: String
    let year: Int
    let mileage: Int
    let vehicleType: String  // ICE | EV | HYBRID

    enum CodingKeys: String, CodingKey {
        case id, vin, make, model, year, mileage
        case vehicleType = "vehicle_type"
    }

    var displayName: String { "\(year) \(make) \(model)" }
}
