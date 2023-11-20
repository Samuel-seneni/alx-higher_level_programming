#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ prints the first x elements of a list and only integers.
    mylist(list): the list element to print from
    x(int): The number of elements to be print
    Return: the number of element printed
    """
    res = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            res += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (res)
