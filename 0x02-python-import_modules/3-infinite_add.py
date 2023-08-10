#!/usr/bin/python3
import sys
def add(argv):
    sum = 0
    for arg in argv:
        sum += int(arg)
    return sum
if __name__ == "__main__":
    result = add(sys.argv[1:])
    print(result)
