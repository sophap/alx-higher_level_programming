#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv)
    sum = 0

    if argv_len <= 1:
        pass
    elif argv_len == 2:
        sum += int(sys.argv[1])
    else:
        for x in range(1, argv_len):
            sum += int(sys.argv[x])
    print("{}".format(sum))
