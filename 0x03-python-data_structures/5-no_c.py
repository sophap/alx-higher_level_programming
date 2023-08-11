#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for str in my_string:
        if str != 'c' and str != 'C':
            new += str
    return new
