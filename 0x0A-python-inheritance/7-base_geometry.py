#!/usr/bin/python3
"""
Base Geometry Class
"""


class BaseGeometry:
    """class that improves geometry with integer validator"""
    def area(self):
        """raises an exception with message area() not implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
