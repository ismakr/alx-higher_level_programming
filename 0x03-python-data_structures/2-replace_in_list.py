#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    i = 0
    while i < idx:
        if i >= len(my_list):
            return None
        i += 1
    my_list[i] = element
    return my_list
