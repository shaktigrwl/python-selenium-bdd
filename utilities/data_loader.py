import json


def load_json(key, file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return data.get(key, {})
