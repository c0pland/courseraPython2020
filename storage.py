from argparse import ArgumentParser
from json import loads, dumps
from tempfile import gettempdir
from os import path, remove

STORAGE_PATH = path.join(gettempdir(), 'storage.data')


def get_data():
    if not path.exists(STORAGE_PATH):
        f = open(STORAGE_PATH, "w")
        f.close()
    with open(STORAGE_PATH, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return loads(raw_data)

        return {}


def write(key, value):
    data = get_data()

    if data and key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(STORAGE_PATH, 'w') as f:
        f.write(dumps(data))


def get(key):
    data = get_data()
    if data and key in data:
        return data.get(key)
    else:
        return None


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    parser.add_argument('--clear', action='store_true', help='Clear')

    args = parser.parse_args()

    if args.clear:
        remove(STORAGE_PATH)
    elif args.key and args.val:
        write(args.key, args.val)
    elif args.key:
        if path.exists(STORAGE_PATH):
            data = get_data()
            if args.key in data:
                res = ", ".join(get(args.key))
                print(res[:])
