#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    highest = 0
    name = None
    for key in a_dictionary.keys():
        if a_dictionary[key] > highest:
            highest = a_dictionary[key]
            name = key
    return name
