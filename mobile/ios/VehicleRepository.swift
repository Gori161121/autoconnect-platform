import Foundation

struct VehicleRepository {

    let apiClient: AutoConnectApiClient

    func fetchVehicleHealth(vehicleId: Int) -> String {
        return apiClient.vehicleHealthEndpoint(vehicleId: vehicleId)
    }

    func fetchVehicleDiagnostics(vehicleId: Int) -> String {
        return apiClient.diagnosticsEndpoint(vehicleId: vehicleId)
    }

    func fetchVehicleIntelligenceReport(vehicleId: Int) -> String {
        return apiClient.intelligenceReportEndpoint(vehicleId: vehicleId)
    }
}
