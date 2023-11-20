#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    If a ValueError message is found is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns: 
        it return True if value has been printed on stderror
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
