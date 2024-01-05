#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0:
        return new_list
    i = 0
    while i < idx:
        if i >= len(new_list):
            return new_list
        i += 1
    new_list[i] = element
    return new_list
