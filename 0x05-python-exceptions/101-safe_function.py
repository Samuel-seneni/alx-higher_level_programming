#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as i:
        print("Exception: {}".format(i), file=sys.stderr)
        return None
    else:
        return res
