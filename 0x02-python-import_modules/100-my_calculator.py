#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    msg = ["Usage: ./100-my_calculator.py <a> <operator> <b>",
           "Unknown operator. Available operators: +, -, * and /"]
    op = {'+': add, '-': sub, '*': mul, '/': div}

    if len(argv) != 4 or argv[2] not in list(op.keys()):
        print(msg[0] if len(argv) != 4 else msg[1])
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print(f"{a} {argv[2]} {b} = {op[argv[2]](a, b)}")
