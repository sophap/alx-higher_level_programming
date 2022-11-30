#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
x = num[-1]

if x == '0':
    print(f"Last digit of {num} is {x} and is 0")
else:
    if number > 0:
        if int(x) > 5:
            print("Last digit of {num} is {x} and is greater than 5")
        elif int(x) < 6 and x != 0:
            print("Last digit of {num} is {x} and is less than 6 and not 0")
    else:
        print("Last digit of {num} is -{x} and is less than 6 and not 0")
