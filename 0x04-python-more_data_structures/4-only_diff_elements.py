#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = set()
    for x in set_1:
        if x not in set_2:
            diff.add(x)
    for x in set_2:
        if x not in set_1:
            diff.add(x)
    return diff
