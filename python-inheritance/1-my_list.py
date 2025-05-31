#!/usr/bin/python3

"""
this module have one function use to know the methode and attribute of a class
"""


class MyList(list):
    """
    this function class is inheritance of the list class and have a methode
    to print sorted the list without modify the list
    """

    def print_sorted(self):
        """
        the function print the list in ascending order
        """
        print_list = self[:]
        print_list.sort()
        print(print_list)
