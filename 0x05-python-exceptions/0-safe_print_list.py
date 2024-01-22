#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        m_len = 0
        for n in my_list:
            m_len += 1
        i = 0
        while i < x and i < m_len:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        print("")
        return i
    except (RuntimeError, TypeError, NameError):
        pass
