#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    i = 0
    while i < len(my_string):
        if my_string[i] == 'c' or my_string[i] == 'C':
            i += 1
        new_string.append(my_string[i])
        i += 1
    return "".join(new_string)
