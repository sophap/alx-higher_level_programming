#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv[1:])
    print("{:d} argument{}{}".format(num_args,
        "s" if num_args != 1 else "",
        "." if num_args == 0 else ":"))
    for x, args in enumerate(sys.argv[1:]):
        print("{}: {}".format(x + 1, args))
