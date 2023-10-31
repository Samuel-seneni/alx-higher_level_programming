#!/usr/bin/python
def uppercase(str):

    """Print a string in uppercase."""
    for i in str:
        if ord("a") <= ord(i) <= ord("Z"):
            i = chr(ord(i) - 32)
        print("{:S}".format(i), end="")
    print()
