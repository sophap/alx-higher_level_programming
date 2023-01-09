#!/usr/bin/python3
"""
Program checks if an object is inherited from a class
"""


def inherits_from(obj, a_class):
    """
    Function that returns true if an object is an instance
    of a class that inherited directly or indirectly
    from a specified class: otherwise false
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
