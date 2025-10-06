from resources.parse import parse_build
import os
import subprocess





def check_build(venv_name):
    for dir in os.listdir():
        if dir == venv_name:
            return f"VENV|{dir}"
            break
    else:
        if "pythonBuild.jsonc" in os.listdir():
            return "BUILD|pythonBuild.jsonc"
        else:
            return "None|notpythonBuild.jsonc"


try:
    libs, other_data = parse_build("pythonBuild.jsonc")
    check = check_build(other_data["venv_name"])


    if check.startswith("BUILD"):
        print("Parsing pythonBuild")

        try:

            os.system(f"python3 -m venv {other_data['venv_name']}")

            for lib in libs:
                os.system(f"{other_data['venv_name']}/bin/python3 -m pip install {lib}")

            path = subprocess.run("pwd", capture_output=True, text=True)

            with open("start", "w") as file:
                file.write(f"""
                #!/bin/bash
                cd {path.stdout.strip()}
                source .venv/bin/activate
                python3 {other_data["main"]}
                """)

        except Exception as e:
            print(e)

    elif check.startswith("None"):
        print("pythonBuild is missing or the virtual environment is already in your project")

    elif check.startswith("VENV"):
        venv_dir = check.split("|")[-1]

        for lib in libs:
            os.system(f"{venv_dir}/bin/python3 -m pip install {lib}")
except Exception as e:
    print("Error parsing build.jsonc")





