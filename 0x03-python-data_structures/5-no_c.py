#!/usr/bin/env python3
def no_c(my_string):
    new_str = list(my_string)
    i = 0
    while i < len(new_str):
        if new_str[i] == 'c' or new_str[i] == 'C':
            new_str.pop(i)
        else:
            i += 1
    result_str = ''.join(new_str)
    return result_str
