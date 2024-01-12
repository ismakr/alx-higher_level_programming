#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        li = [(i, j) for i, j in a_dictionary.items()]
        return max(li)[0]
    else:
        return None
