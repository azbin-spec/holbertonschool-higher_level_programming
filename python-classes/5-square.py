#!/usr/bin/python3
"""
5-square.py
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

    @property
    def size(self):
        """
        Gets the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        value (int): size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes the area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints the square.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
