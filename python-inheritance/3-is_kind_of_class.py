#!/usr/bin/python3

"""
this module have a function that look for the class of an object
or if the object is an instance of a class that inherited from a givne class
"""


def is_kind_of_class(obj, a_class):
    """
    the function return true if the object is an instance
    if the object is an instance of a class that inherited from
    the given class
    """
    return isinstance(obj, a_class)
