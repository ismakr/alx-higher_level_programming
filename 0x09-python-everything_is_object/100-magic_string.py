#!/usr/bin/python3
def magic_string():
    magic_string.iter = getattr(magic_string, 'iter', 0) + 1
    li1 = ["BestSchool" for i in range(magic_string.iter)]
    return ", ".join(li1)
