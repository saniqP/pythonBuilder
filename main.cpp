#include <cstdlib>
#include <exception>
#include <filesystem>
#include <fstream>
#include <ostream>
#include <iostream>
#include <string>
#include "resources/libs/parser.hpp"
#include <map>

using json = nlohmann::json;

std::map<std::string,std::map<std::string,std::string>> iconsAndColors(){

    return {
        {"icons", {
            {"ROCKET", "異 "},
            {"CHECK", " "},
            {"CROSS", " "},
            {"WARNING", " "},
            {"FOLDER", " "},
            {"BOOK", " "},
            {"GEAR", " "},
            {"SNAKE", "󱔎 "},
            {"PACKAGE", " "},
            {"HAMMER", " "},
            {"PARTY", " "},
            {"HOURGLASS", " "},
            {"TERMINAL", " "},
            {"CODE", " "},
            {"PLAY", ""},
            {"SERVER", " "}
            }
        },

        {"colors", {
            {"RED", "\033[91m"},
            {"GREEN", "\033[92m"},
            {"YELLOW", "\033[93m"},
            {"BLUE", "\033[94m"},
            {"MAGENTA", "\033[95m"},
            {"CYAN", "\033[96m"},
            {"WHITE", "\033[97m"},
            {"RESET", "\033[0m"},
            {"BOLD", "\033[1m"}
            }
        }

    };
}


void createVenv(json config, std::map<std::string,std::map<std::string,std::string>> styles){

    try {
        std::cout << styles["colors"]["BLUE"] << styles["icons"]["GEAR"] << styles["colors"]["GREEN"] << "Start to creating venv" << styles["colors"]["RESET"] << std::endl;

        if (!check(config["venv_name"].get<std::string>())) {

            std::string command;

            if (config.contains("python3.14") && config["python3.14"]["enable"]) {

                json python314 = config["python3.14"];

                std::string install;

                if (python314["package_manager"].get<std::string>() != "yay" &&
                    python314["package_manager"].get<std::string>() != "paru") {

                    install = "sudo " + python314["package_manager"].get<std::string>() + " install python3.14";
                }

                else {
                    install = python314["package_manager"].get<std::string>() + " -S python314";
                }

                int result = system(install.c_str());

                if (result != 0) {
                    std::cout << styles["colors"]["RED"] << styles["icons"]["CROSS"] << "Failed to install python3.14" << styles["colors"]["RESET"] << std::endl;
                    command = "python3 -m venv " + config["venv_name"].get<std::string>();
                }
                else {
                    system("clear");
                    std::cout << styles["colors"]["GREEN"] << styles["icons"]["CHECK"] << "Python3.14 installed" << styles["colors"]["RESET"] << std::endl;
                    command = "python3.14 -m venv " + config["venv_name"].get<std::string>();
                }

            }
            else {
                command = "python3 -m venv " + config["venv_name"].get<std::string>();
            }
            system(command.c_str());

            std::cout << styles["colors"]["GREEN"] << styles["icons"]["CHECK"] << "Venv created" << styles["colors"]["RESET"] << std::endl;
        }

        else {
            std::cout << styles["colors"]["YELLOW"] << styles["icons"]["WARNING"] << "Warning! " << config["venv_name"].get<std::string>() << " already exists" << styles["colors"]["RESET"] << std::endl;
        }
    }

    catch(std::exception) {
        std::cout << styles["colors"]["RED"] << styles["icons"]["CROSS"] << "Failed to create venv" << styles["colors"]["RESET"] << std::endl;
    }
}

void loadLibs(json config, std::map<std::string,std::map<std::string,std::string>> styles){
    if (config.contains("libraries")) {
        for (json lib : config["libraries"]) {
            std::string command = config["venv_name"].get<std::string>() + "/bin/python3 -m " + "pip install " + lib.get<std::string>() + " > /dev/null 2>&1";

            try {

                std::cout << styles["colors"]["BLUE"] << styles["icons"]["GEAR"] << styles["colors"]["GREEN"] << "Installing " << lib.get<std::string>() << styles["colors"]["RESET"] << std::endl;

                system(command.c_str());

                std::cout << styles["colors"]["GREEN"] << styles["icons"]["CHECK"] << lib.get<std::string>() << " installed \n" << styles["colors"]["RESET"] << std::endl;
            }

            catch(std::exception) {
                std::cout << styles["colors"]["RED"] << styles["icons"]["CROSS"] << "Failed to install \n" << lib.get<std::string>() << styles["colors"]["RESET"] << std::endl;
            }
        }
    }

}

void createDefaultFolders(json config, std::map<std::string,std::map<std::string,std::string>> styles) {

    if (config.contains("default_folders")) {
        json defaultFolder = config["default_folders"];

        try {
            if (defaultFolder["enable"]) {

                std::cout << styles["colors"]["BLUE"] << styles["icons"]["GEAR"] << styles["colors"]["GREEN"] << "Creating default folders \n" << styles["colors"]["RESET"] << std::endl;

                for (json folder : defaultFolder["folders"]) {

                    if (check(folder.get<std::string>())) {
                        std::cout << styles["colors"]["YELLOW"] << styles["icons"]["WARNING"] << "Warning! Folder " << folder.get<std::string>() << " areaty exists" << styles["colors"]["RESET"] << std::endl;
                    }

                    else {

                        std::filesystem::create_directory(folder);

                        std::cout << styles["colors"]["GREEN"] << styles["icons"]["CHECK"] << folder.get<std::string>() << " created" << styles["colors"]["RESET"] << std::endl;

                    }
                }
            }

            std::cout << styles["colors"]["GREEN"] << styles["icons"]["CHECK"] << "All folders created" << styles["colors"]["RESET"] << std::endl;
        }

        catch(std::exception) {
            std::cout << styles["colors"]["RED"] << styles["icons"]["CROSS"] << "Failed to creating folders" << styles["colors"]["RESET"] << std::endl;
        }
    }

}

void createStartFile(json config, std::map<std::string,std::map<std::string,std::string>> styles) {
    if (config.contains("start_file")) {
        json startFile = config["start_file"];

        try {
            if (startFile["enable"]) {

                std::cout << styles["colors"]["BLUE"] << styles["icons"]["GEAR"] << styles["colors"]["GREEN"] << "Creating start file" << styles["colors"]["RESET"] << std::endl;

                std::fstream startFIleInSystem("start.sh");
                if (startFIleInSystem.is_open()) {
                    startFIleInSystem << "#/bin/bash\n" << config["venv_name"] << "/bin/python3 " << startFile["main_file"] << std::endl;
                    startFIleInSystem.close();
                }

            }

            std::cout << styles["colors"]["GREEN"] << styles["icons"]["CHECK"] << "Start file created" << styles["colors"]["RESET"] << std::endl;
        }

        catch(std::exception) {
            std::cout << styles["colors"]["RED"] << styles["icons"]["CROSS"] << "Failed to create start file" << styles["colors"]["RESET"] << std::endl;
        }
    }
}


int main() {

    std::string pythonBuildFileName = "pythonBuild.jsonc";

    std::map<std::string,std::map<std::string,std::string>> styles = iconsAndColors();

    if (check(pythonBuildFileName)) {

        json config = parse(pythonBuildFileName);

        createVenv(config, styles);
        std::cout << "\n\n" <<std::endl;
        loadLibs(config, styles);
        std::cout << "\n\n" <<std::endl;
        createDefaultFolders(config, styles);
        std::cout << "\n\n" <<std::endl;
        createStartFile(config, styles);
    }

    else {
        std::cout << "pythonBuild.jsonc not found" << std::endl;
    }
}



