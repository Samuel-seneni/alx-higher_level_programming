#!/usr/bin/python3
"""Definition of a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): To check the object
        a_class (type): The class to match the type of object to.
    Returns:
        If object is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
