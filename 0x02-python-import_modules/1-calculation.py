#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import add, sub, mul, div

sum = add(a, b)
diff = sub(a, b)
prod = mul(a, b)
quot = div(a, b)

print("{} + {} = {}".format(a, b, sum))
print("{} - {} = {}".format(a, b, diff))
print("{} * {} = {}".format(a, b, prod))
print("{} / {} = {}".format(a, b, quot))
