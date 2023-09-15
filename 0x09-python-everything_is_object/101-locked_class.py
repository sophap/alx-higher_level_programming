#!/usr/bin/python3
"""
This is the module docstring. It provides an overview of the module's purpose.
"""


class LockedClass:
    """
    This is the docstring for the LockedClass.
    It explains the purpose of the class and how it works.
    """

    def __setattr__(self, attr, value):
        if attr != 'first_name':
            raise AttributeError("'LockedClass' object \
has no attribute '{}'".format(attr))
    
    def __getattribute__(self, attr):
        if attr == '__dict__':
            raise AttributeError("'LockedClass' object has no attribute '__dict__'")
        return super().__getattribute__(attr)
