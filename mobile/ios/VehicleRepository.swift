import Foundation

/// Repository layer that isolates networking from the UI (SwiftUI views).
struct VehicleRepository {
    let apiClient: AutoConnectApiClient

    init(apiClient: AutoConnectApiClient) {
        self.apiClient = apiClient
    }

    func loadVehicles() async -> [VehicleStatusModel] {
        (try? await apiClient.fetchVehicles()) ?? []
    }

    func loadDiagnostics(vehicleId: Int) async -> [VehicleDiagnosticModel] {
        (try? await apiClient.fetchDiagnostics(vehicleId: vehicleId)) ?? []
    }
}
