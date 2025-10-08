import os

def create_venv(config, styles):

    icons = styles["icons"]
    colors = styles["colors"]

    """Создает виртуальное окружение для проекта"""

    print(f"{colors["BLUE"]}{icons["GEAR"]} Creating venv {colors["RESET"]} \n")

    if os.path.exists(config["venv_name"]):
        print(f"{colors["YELLOW"]}{icons["WARNING"]}{colors["RESET"]} {config["venv_name"]} already exists\n\n")
    result = os.system(f"python3 -m venv {config["venv_name"]}")

    if result != 0:
        print(f"{colors["RED"]}{icons["CROSS"]}{colors["RESET"]} Failed to create venv\n\n")
    else:
        print(f"{colors["GREEN"]}{icons["CHECK"]}{colors["RESET"]} Created venv\n\n")


def load_libs(config, styles):

    icons = styles["icons"]
    colors = styles["colors"]

    """Загружает библиотеки в виртуальное окружение"""

    print(f"{colors["BLUE"]}{icons["GEAR"]} Loading libs {colors["RESET"]}\n")

    try:
        for lib in config["libraries"]:

            lib = lib.strip()

            print(f"{colors["BLUE"]}{icons["GEAR"]} Installing {lib} {colors['RESET']}")

            try:
                os.system(f"{config['venv_name']}/bin/python3 -m pip install {lib} > /dev/null 2>&1")

                print(f"{colors["GREEN"]}{icons["CHECK"]}{colors["RESET"]} {lib} installed\n")
            except Exception:
                print(f"{colors["RED"]}{icons["CROSS"]}{colors["RESET"]} {lib} could not be installed\n")

        print(f"{colors["GREEN"]}{icons["CHECK"]}{colors["RESET"]} Libraries loaded \n\n")
    except Exception:
        print(f"{colors["RED"]}{icons["CROSS"]}{colors["RESET"]} Failed to load libraries \n\n")


def create_default_folders(config, styles):

    icons = styles["icons"]
    colors = styles["colors"]

    """Создаёт дефолтные директории"""

    print(f"{colors["BLUE"]}{icons["GEAR"]} Creating default folders {colors["RESET"]}\n")

    try:
        default_folder = config["default_folders"]

        if default_folder["enable"]:

            for folder in default_folder["folders"]:

                if os.path.exists(folder):
                    print(f"{colors["YELLOW"]}{icons["WARNING"]}{colors["RESET"]} Folder {folder} already exists")
                else:
                    os.mkdir(folder)
                    print(f"{colors["GREEN"]}{icons["CHECK"]}{colors["RESET"]} Created folder {folder}")

        print(f"{colors["GREEN"]}{icons["CHECK"]}{colors["RESET"]} Default folders created")

    except Exception:
        print(f"{colors["RED"]}{icons["CROSS"]}{colors["RESET"]} Failed to create default folders")


def create_start_file(config, styles):

    icons = styles["icons"]
    colors = styles["colors"]

    """Создаёт start_file"""

    print(f"{colors["BLUE"]}{icons["GEAR"]} Creating start file {colors["RESET"]}")

    start_file = config["start_file"]

    if start_file["enable"]:

        print(f"{colors["GREEN"]}{icons["CHECK"]}{colors["RESET"]} Start file created")

        try:
            with open("start.sh", "w") as file:
                file.write(f"""
                   #!/bin/bash
                   {config["venv_name"]}/bin/python3 {start_file["main_file"]}
                   """)

            print("Start file created")

        except Exception:
            print(f"{colors["RED"]}{icons["CROSS"]}{colors["RESET"]} Failed to create start file")