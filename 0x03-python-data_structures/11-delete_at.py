#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    i = 0
    while i < len(my_list):
        if idx == i:
            del my_list[i]
        i += 1
    return my_list
