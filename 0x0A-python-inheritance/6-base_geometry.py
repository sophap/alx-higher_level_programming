#!/usr/bin/python3
"""
empty geometry class
"""


class BaseGeometry:
    """Improves geometry class"""
    def area(self):
        """function raises an exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
