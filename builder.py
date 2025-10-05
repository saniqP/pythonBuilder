from resources.parse import parse_build
import os
import subprocess

def check_build():
    for file_name in os.listdir():
        if file_name == "pythonBuild.jsonc":
            return True
            break
    else:
        return False
if check_build():
    print("Parsing pythonBuild")

    try:
        libs, other_data = parse_build("pythonBuild.jsonc")

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

else:
    print("pythonBuild is missing")

