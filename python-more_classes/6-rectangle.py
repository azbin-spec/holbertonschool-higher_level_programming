#!/usr/bin/python3
"""
0-rectangle.py
Module containing class Rectangle.
"""


class Rectangle:
    """
    A class to define a rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        type(self).number_of_instances += 1

        self.__width = width
        self.__height = height

    def __del__(self):
        type(self).number_of_instances -= 1

        print("Bye rectangle...")

    def __str__(self):
        result = ""
        if self.__height != 0 and self.__width != 0:
            for row in range(self.__height):
                for col in range(self.__width):
                    result += '#'
                if row + 1 != self.__height:
                    result += '\n'

        return result

    def __repr__(self):
        width = self.__width
        height = self.__height
        return "Rectangle({}, {})".format(width, height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height
