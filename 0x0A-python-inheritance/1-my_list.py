#!/usr/bin/python3
"""
Module of inherited list
"""


class MyList(list):
    """Mylist"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
