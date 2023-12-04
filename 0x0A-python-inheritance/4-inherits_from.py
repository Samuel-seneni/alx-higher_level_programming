#!/usr/bin/python3
""" Definition of an inherited class checking function """


def inherits_from(obj, a_class):
    """checks if an object is inherited from a class.

    args:
        obj (any): object of the class to check.
        a_class (type): the class marching the object.
    Returns:
        if the object is an instance of a class that inherited
        is True, otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
