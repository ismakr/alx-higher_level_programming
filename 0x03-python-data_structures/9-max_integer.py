#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = 0
    big = 0
    while i < len(my_list):
        if big > my_list[i]:
            i += 1
        else:
            big = my_list[i]
        i += 1
    return big
