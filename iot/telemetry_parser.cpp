// telemetry_parser.cpp
// Parses raw OBD-II telemetry frames ("key=value;key=value;...") emitted by the
// device into structured fields for upload to the backend.
//
// Build: g++ -std=c++17 telemetry_parser.cpp -o telemetry_parser
// Run:   ./telemetry_parser "rpm=2200;speed_kmh=64;coolant_temp_c=92;dtc=P0420"

#include <iostream>
#include <map>
#include <sstream>
#include <string>

std::map<std::string, std::string> parseFrame(const std::string& frame) {
    std::map<std::string, std::string> fields;
    std::stringstream ss(frame);
    std::string pair;

    while (std::getline(ss, pair, ';')) {
        if (pair.empty()) continue;
        auto eq = pair.find('=');
        if (eq == std::string::npos) continue;
        std::string key = pair.substr(0, eq);
        std::string value = pair.substr(eq + 1);
        fields[key] = value;
    }
    return fields;
}

int main(int argc, char* argv[]) {
    std::string frame = (argc > 1)
        ? argv[1]
        : "rpm=2200;speed_kmh=64;coolant_temp_c=92;dtc=P0420";

    auto fields = parseFrame(frame);
    std::cout << "Parsed " << fields.size() << " fields:\n";
    for (const auto& [key, value] : fields) {
        std::cout << "  " << key << " -> " << value << "\n";
    }
    return 0;
}
