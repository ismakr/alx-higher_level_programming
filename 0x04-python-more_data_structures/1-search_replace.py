#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    i = 0
    while i < len(my_list):
        if my_list[i] == search:
            my_list[i] = replace
        i += 1
    return new_list
