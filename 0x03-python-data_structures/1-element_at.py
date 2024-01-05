#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    i = 0
    while i <= idx:
        if i >= len(my_list):
            return None
        i += 1
    return my_list[i]
