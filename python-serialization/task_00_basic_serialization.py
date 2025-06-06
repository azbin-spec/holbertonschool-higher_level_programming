#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Args:
        data (dict): A Python dictionary with data.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w+', encoding="utf-8") as file:
        json.dump(data, file)
    pass

def load_and_deserialize(filename):
    """
    Deserializes a JSON file to recreate a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized JSON data.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data
