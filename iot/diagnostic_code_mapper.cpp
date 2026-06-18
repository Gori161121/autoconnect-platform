#include <iostream>
#include <map>
#include <string>

struct DiagnosticInfo {
    std::string system;
    std::string severity;
    std::string description;
};

std::map<std::string, DiagnosticInfo> diagnosticDatabase = {
    {
        "P0420",
        {
            "Emissions",
            "MEDIUM",
            "Catalyst system efficiency below threshold"
        }
    },
    {
        "P0300",
        {
            "Engine",
            "HIGH",
            "Random or multiple cylinder misfire detected"
        }
    },
    {
        "P0562",
        {
            "Electrical",
            "HIGH",
            "System voltage low"
        }
    }
};

DiagnosticInfo mapDiagnosticCode(const std::string& code) {
    if (diagnosticDatabase.find(code) != diagnosticDatabase.end()) {
        return diagnosticDatabase[code];
    }

    return {
        "Unknown",
        "UNKNOWN",
        "Diagnostic code is not available in local database"
    };
}

int main() {
    std::string faultCode = "P0420";

    DiagnosticInfo info = mapDiagnosticCode(faultCode);

    std::cout << "Fault Code: " << faultCode << std::endl;
    std::cout << "System: " << info.system << std::endl;
    std::cout << "Severity: " << info.severity << std::endl;
    std::cout << "Description: " << info.description << std::endl;

    return 0;
}
