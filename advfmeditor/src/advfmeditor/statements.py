import json
import os
from types import SimpleNamespace
from .core import Statement

def generator(filename: str):
    resources_dir = os.path.join(os.path.dirname(__file__), 'resources')
    json_file_path = os.path.join(resources_dir, filename)
    with open(json_file_path, 'r') as file:
        statements = json.load(file,  object_hook=lambda d: SimpleNamespace(**d))
        for statement in statements:
            yield statement
    