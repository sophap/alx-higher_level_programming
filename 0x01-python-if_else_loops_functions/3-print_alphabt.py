#!/usr/bin/python3
for alph in range(ord('a'), ord('z') + 1):
    if chr(alph) != 'q' and chr(alph) != 'e':
        print("{}".format(chr(alph)), end="")
