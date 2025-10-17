#ifndef PARSER
#define PARSER

#include <fstream>
#include "json.hpp"
#include <filesystem>
#include <string>

using json = nlohmann::json;

json parse(std::string path) {
    std::ifstream build_config(path);
    json config = json::parse(build_config);

    return config;
}

bool check(std::string path) {
    
    if (std::filesystem::exists(path)) {
        return true;
    }

    else {
        return false;
    }
}

#endif