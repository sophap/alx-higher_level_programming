#!/usr/bin/python3
from sys import argv
def print_args(argv):
    num_args = len(argv)
    print("{} argument{}{}".format(num_args, "s" if num_args != 1 else "", "." if num_args == 0 else ":"))
    for x, arg in enumerate(argv):
        print("{}: {}".format(x + 1, arg))

if __name__ == "__main__":
    print_args(sys.argv[1:])
