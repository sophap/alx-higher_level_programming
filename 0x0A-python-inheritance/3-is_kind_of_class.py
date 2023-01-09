#!/usr/bin/python3
"""
Program that checks if a class is the same object or inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Function returns true if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the desired class: otherwise false
    """
    return isinstance(obj, a_class)
