import json

def load_json(file_path):
    """Load a json file."""
    with open(file_path, "r") as file:
        return json.load(file)
