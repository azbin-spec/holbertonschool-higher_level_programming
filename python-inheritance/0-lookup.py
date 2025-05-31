#!/usr/bin/python3

"""
this module have one function use to know the methode and attribute of a class
"""


def lookup(obj):
    """
    this function return the list of methode and attribute of a class given
    """
    return dir(obj)
