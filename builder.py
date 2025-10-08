from resources.reader import reader
from resources.functions import *
import os

def icons_and_colors():

    return {
        "colors": {
            "RED": "\033[91m",
            "GREEN": "\033[92m",
            "YELLOW": "\033[93m",
            "BLUE": "\033[94m",
            "MAGENTA": "\033[95m",
            "CYAN": "\033[96m",
            "WHITE": "\033[97m",
            "RESET": "\033[0m",
            "BOLD": "\033[1m"
        },

        "icons": {
            "ROCKET": '異',
            "CHECK": '',
            "CROSS": '',
            "WARNING": '',
            "FOLDER": '',
            "BOOK": '',
            "GEAR": '',
            "SNAKE": '󱔎',
            "PACKAGE": '',
            "HAMMER": '',
            "PARTY": '',
            "HOURGLASS": '',
            "TERMINAL": '',
            "CODE": '',
            "PLAY": '',
            "SERVER": ''
        }
    }

config = reader("pythonBuild.jsonc")

if config is not None:

    styles = icons_and_colors()

    def main():
        print(f"{styles["colors"]["CYAN"]}{styles["icons"]["ROCKET"]}{styles["colors"]["RESET"]} Building project\n\n")


        create_venv(config, styles)

        load_libs(config, styles)

        create_default_folders(config, styles)

        create_start_file(config, styles)



    if __name__ == "__main__":
        main()


else:
    print("No found pythonBuild.jsonc")




