import json
import sys
import os


def load_data(filepath):
    data = json.load(filepath)
    return data


def pretty_print_json(data):
    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    path = sys.argv[1]
    try:
        is_exists = os.path.exists(path)
    except Exception as e:
        print(e)
    else:
        try:
            pretty_print_json(load_data(path))
        except Exception as e:
            print(e)
