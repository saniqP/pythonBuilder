import json

def parse_build(path):
    with open(path, "r") as f:
        build = json.load(f)

        libraries = []

        other_data = {}

        for lib, in_project in build["libraries"].items():
            if in_project:
                libraries.append(lib)

        other_data["venv_name"] = build["venv_name"]
        other_data["main"] = build["main"]

    return libraries, other_data


