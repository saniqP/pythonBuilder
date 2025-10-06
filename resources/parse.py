import json
import os

def parser(path):

    if os.path.exists(path):
        with open(path, "r") as f:
            build_file = json.load(f)

            return build_file

    else:
        return False


