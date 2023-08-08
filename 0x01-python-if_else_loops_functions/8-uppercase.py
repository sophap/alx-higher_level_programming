#!/usr/bin/python3
def uppercase(s):
    for str in s:
        if ord(str) >= 97 and ord(str) <= 122:
            str = chr(ord(str) - 32)
        print("{}".format(str), end='')
    print()
