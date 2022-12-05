#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for x in range(len(my_list)):
        if idx < 0:
            return my_list
        if idx > len(my_list):
            return my_list
        elif idx == x:
            my_list[idx] = element
            return my_list
