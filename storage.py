import argparse
import os
import tempfile
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
    if not os.path.exists(storage_path):
        open(storage_path, "w")
    with open(storage_path) as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)
        return None

