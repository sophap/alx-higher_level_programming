#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is Noone:
        return 0
    sum = total = 0
    for (a, b) in my_list:
        sum += (a * b)
        total += b
    return sum / total
