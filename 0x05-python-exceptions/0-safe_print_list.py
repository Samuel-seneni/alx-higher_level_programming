#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    my_list: list to be printed from.
    x: the integer to be printed
    return:the number of element printed
    """

    res = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            res += 1
        except IndexError:
            break
        print("")
        return (res)
