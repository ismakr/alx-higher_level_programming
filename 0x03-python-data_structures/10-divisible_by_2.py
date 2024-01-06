#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in my_list:
        if i == 0 or i % 2 == 0:
            new_list[my_list.index(i)] = True
        else:
            new_list[my_list.index(i)] = False
    return new_list
