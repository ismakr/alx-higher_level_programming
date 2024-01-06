#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    i = 0
    while i < len(my_string):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_string.extend(my_string[i])
        i += 1
    return "".join(new_string)
