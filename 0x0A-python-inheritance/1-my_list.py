#!/usr/bin/python3
""" Definition of inherited list"""


class MyList(list):
     """print implemented sorted for the built-in list class."""

     def print_sorted(self):
         """Print a list in sorted ascending order."""
         print(sorted(self))
