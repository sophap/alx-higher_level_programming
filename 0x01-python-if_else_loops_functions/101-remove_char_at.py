#!/usr/bin/python3
def remove_char_at(str, n):
    ptr = ""
    for x in range(len(str)):
        if x != n:
            ptr += str[x]
    return (ptr)
