#!/usr/bin/python3

"""
this module have a function that look for the class of an object
"""


def is_same_class(obj, a_class):
    """
    the function return true if the class of the object given match
    to the type of the given class
    """
    if (type(obj) is a_class):
        return True
    return False
