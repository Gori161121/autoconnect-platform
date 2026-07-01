import Foundation

/// Minimal async HTTP client for the AutoConnect Vehicle Intelligence API.
struct AutoConnectApiClient {
    let baseURL: URL

    init(baseURL: String) {
        self.baseURL = URL(string: baseURL)!
    }

    enum ApiError: Error {
        case badStatus(Int)
        case invalidURL
    }

    /// Perform a GET request and decode the JSON body into `T`.
    func get<T: Decodable>(_ path: String, as type: T.Type) async throws -> T {
        guard let url = URL(string: path, relativeTo: baseURL) else {
            throw ApiError.invalidURL
        }
        var request = URLRequest(url: url)
        request.setValue("application/json", forHTTPHeaderField: "Accept")

        let (data, response) = try await URLSession.shared.data(for: request)
        if let http = response as? HTTPURLResponse, http.statusCode >= 400 {
            throw ApiError.badStatus(http.statusCode)
        }
        return try JSONDecoder().decode(T.self, from: data)
    }

    func fetchVehicles() async throws -> [VehicleStatusModel] {
        try await get("vehicles", as: [VehicleStatusModel].self)
    }

    func fetchDiagnostics(vehicleId: Int) async throws -> [VehicleDiagnosticModel] {
        struct DiagnosticsResponse: Decodable { let faults: [VehicleDiagnosticModel] }
        let result = try await get("vehicles/\(vehicleId)/diagnostics",
                                   as: DiagnosticsResponse.self)
        return result.faults
    }
}
