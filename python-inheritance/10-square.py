#!/usr/bin/python3
"""
this module have a class of square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this class is a child of Rectangle and represente square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
