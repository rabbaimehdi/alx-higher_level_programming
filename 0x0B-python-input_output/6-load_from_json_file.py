#!/usr/bin/python3
""" defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates a Python object"""
    with open(filename) as f:
        return json.load(f)
