#!/usr/bin/python3
def uniq_add(my_list=[]):
    values = set()
    result = 0
    for x in my_list:
        if x not in values:
            values.add(x)
            result += x
    return result
