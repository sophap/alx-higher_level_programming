#!/usr/bin/python3
def no_c(my_string):
    for x in range(len(my_string) - 2):
        if my_string[x] == 'c' or my_string[x] == 'C':
            my_string = my_string[:x] + "" + my_string[x + 1:]
    return my_string
