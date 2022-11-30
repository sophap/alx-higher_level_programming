#!/usr/bin/python3
for x in range(0, 9):
    for y in range(1, 10):
        if y < x:
            pass
        elif y == x:
            pass
        elif x == 8 and y == 9:
            print(89)
        else:
            print("{}{}, ".format(x, y), end='')
