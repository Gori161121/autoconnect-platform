import Foundation

struct AutoConnectApiClient {

    let baseUrl: String

    func vehicleHealthEndpoint(vehicleId: Int) -> String {
        return "\(baseUrl)/vehicles/\(vehicleId)/health"
    }

    func diagnosticsEndpoint(vehicleId: Int) -> String {
        return "\(baseUrl)/vehicles/\(vehicleId)/diagnostics"
    }

    func intelligenceReportEndpoint(vehicleId: Int) -> String {
        return "\(baseUrl)/vehicles/\(vehicleId)/intelligence-report"
    }
}
