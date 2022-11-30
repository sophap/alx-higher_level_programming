#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 0:
    x = -1 * (-num % 10)
else:
    x = num % 10

if x > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, x))
elif x < 6 and x != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(num,x))
elif x == 0:
    print("Last digit of {} is {} and is 0".format(num, x))
