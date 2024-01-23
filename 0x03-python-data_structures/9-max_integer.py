#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    else:
        copy = my_list.copy()
        copy.sort()
        return copy[-1]
