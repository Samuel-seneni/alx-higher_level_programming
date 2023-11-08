#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    result = 0
    for x in new:
        result += x
    return result
