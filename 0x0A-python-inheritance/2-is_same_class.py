#!/usr/bin/python3
"""
Module that checks if an object is exactly of the same class
"""


def is_same_class(obj, a_class):
    """
    function that checks if the object type is the same as a_class
    """
    if type(obj) == a_class:
        return True
    return False
