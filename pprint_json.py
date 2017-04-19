import json
import sys


def load_data(file_path):
    with open(file_path) as fp:
        parsed_json_file = json.load(fp)
    return parsed_json_file


def pretty_print_json(parsed_json_file):
    print(json.dumps(parsed_json_file, indent=4))


if __name__ == '__main__':
    path_to_json_file = sys.argv[1]
    try:
        pretty_print_json(load_data(path_to_json_file))
    except Exception as e:
        print(e)
