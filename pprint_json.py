import json
import sys
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file_handler:
        try:
            return json.load(file_handler)
        except json.decoder.JSONDecodeError:
            return None


def pretty_print_json(parsed_json_file):
    print(json.dumps(parsed_json_file, indent=4))


if __name__ == '__main__':
    path_to_json_file = sys.argv[1]
    pretty_print_json(load_data(path_to_json_file))
