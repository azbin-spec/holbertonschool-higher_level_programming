#!/usr/bin/python3
"""
6-square.py
Module containing class Square.
"""


class Square:
    """
    A class to define a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes an new square.

        Parameters:
        size (int): size of the square
        position (tuple): position of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """
        Gets the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
        value (tuple): position of the square
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for row in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for col in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print()
