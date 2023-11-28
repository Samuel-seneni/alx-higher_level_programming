#!/usr/bin/python3
"""Defines a class locked"""


class LockedClass:
    """prevents the user from instantiating new classlocked 
    attributes, except if the new instance attribute is called first_name.
    """

    __slots__ = ["first_name"]
