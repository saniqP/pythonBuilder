import json

def reader(path):
    try:
        with open(path, "r") as f:
            build_file = json.load(f)

            return build_file
    except FileNotFoundError:
        return None



