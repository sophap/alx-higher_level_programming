#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
    print("{:d} {} {:d} = {:d}".format(a, operator, b, result))
