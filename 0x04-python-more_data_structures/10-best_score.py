#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        mark = 0
        best = 0
        for x in a_dictionary:
            if a_dictionary[x] > mark:
                mark = a_dictionary[x]
                best = x
        return best
    return None
