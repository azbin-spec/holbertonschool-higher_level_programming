#!/usr/bin/python3
"""
2-square.py
Module containing class Square.
"""


class Square:
    """
    A class to define a square.
    """
    def __init__(self, size=0):
        """
        Initializes an new square.

        Parameters:
        size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
