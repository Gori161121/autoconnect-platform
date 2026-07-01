// diagnostic_code_mapper.cpp
// Maps OBD-II diagnostic trouble codes (DTCs) to human-readable descriptions
// and a severity level. Mirrors the backend DTC knowledge base for the
// on-device (edge) layer.
//
// Build: g++ -std=c++17 diagnostic_code_mapper.cpp -o dtc_mapper
// Run:   ./dtc_mapper P0300 P0420 U0100

#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

struct DtcInfo {
    std::string description;
    std::string system;
    std::string severity;
};

static const std::unordered_map<std::string, DtcInfo>& dtcTable() {
    static const std::unordered_map<std::string, DtcInfo> table = {
        {"P0300", {"Random/Multiple Cylinder Misfire Detected", "Engine", "HIGH"}},
        {"P0301", {"Cylinder 1 Misfire Detected", "Engine", "HIGH"}},
        {"P0171", {"System Too Lean (Bank 1)", "Fuel", "MEDIUM"}},
        {"P0420", {"Catalyst System Efficiency Below Threshold", "Emissions", "MEDIUM"}},
        {"P0562", {"System Voltage Low", "Electrical", "HIGH"}},
        {"C0035", {"Left Front Wheel Speed Sensor Circuit", "Chassis", "MEDIUM"}},
        {"U0100", {"Lost Communication With ECM/PCM", "Network", "HIGH"}},
    };
    return table;
}

DtcInfo mapCode(const std::string& code) {
    const auto& table = dtcTable();
    auto it = table.find(code);
    if (it != table.end()) {
        return it->second;
    }
    return {"Unknown fault code - run full diagnostic scan", "Unknown", "UNKNOWN"};
}

int main(int argc, char* argv[]) {
    std::vector<std::string> codes;
    if (argc > 1) {
        for (int i = 1; i < argc; ++i) codes.emplace_back(argv[i]);
    } else {
        codes = {"P0300", "P0420", "U0100", "P9999"};
    }

    for (const auto& code : codes) {
        DtcInfo info = mapCode(code);
        std::cout << code << " | " << info.severity << " | "
                  << info.system << " | " << info.description << "\n";
    }
    return 0;
}
