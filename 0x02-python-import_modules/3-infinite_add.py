#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    res = 0

    for i, v in enumerate(argv[1:]):
        res += int(v)

    print(res)
