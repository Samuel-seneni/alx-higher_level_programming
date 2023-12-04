#!/usr/bin/python3
""" Defines a class and inherited class checking function"""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance or inherited instance of a class

    args:
        obj (any): the object of the class to check
        a_class (type): the class to match with type of object

    Returns:
        if the object is an instance of a class that inherited return True,
        Otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
