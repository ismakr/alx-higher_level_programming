#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    li = [(i, j) for i, j in a_dictionary.items()]
    return max(li)[0]
