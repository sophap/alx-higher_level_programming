#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv) - 1

    if argv_len == 0:
        print("{} arguments.".format(argv_len))
    elif argv_len == 1:
        print("{} argument:".format(argv_len))
        print("{}: {}".format(argv_len, sys.argv[1]))
    else:
        print("{} arguments:".format(argv_len))
        for x in range(1, argv_len + 1):
            print("{}: {}".format(x, sys.argv[x]))
