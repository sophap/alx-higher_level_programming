#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    result = 0
    weight = 0
    for score, weig in my_list:
        result += score * weig
        weight += weig
    weightedave = result / weight
    return weightedave
