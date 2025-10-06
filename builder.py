from resources.parse import parser
import os
import subprocess

build = parser("pythonBuild.jsonc")

if build == False:
    print("Build failed")
else:
    try:

        print("Parsing pythonBuild")

        if build["venv_name"] in os.listdir():
            for lib_key, lib_value in build["libraries"].items():
                if lib_value:
                    os.system(f"{build['venv_name']}/bin/python3 -m pip install {lib_key}")
        else:
            os.system(f"python3 -m venv {build['venv_name']}")

            for lib_key, lib_value in build["libraries"].items():
                if lib_value:
                    os.system(f"{build['venv_name']}/bin/python3 -m pip install {lib_key}")

            path = subprocess.run("pwd", capture_output=True, text=True)

            with open("start", "w") as file:
                file.write(f"""
                #!/bin/bash
                cd {path.stdout.strip()}
                source .venv/bin/activate
                python3 {build["main"]}
                """)


    except Exception as e:
        print("Error parsing build.jsonc")





