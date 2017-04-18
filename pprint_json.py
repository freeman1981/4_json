import json
import sys


def load_data(filepath):
    with open(filepath) as fp:
        data = json.load(fp)
    return data


def pretty_print_json(data):
    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    path = sys.argv[1]
    try:
        pretty_print_json(load_data(path))
    except Exception as e:
        print(e)
