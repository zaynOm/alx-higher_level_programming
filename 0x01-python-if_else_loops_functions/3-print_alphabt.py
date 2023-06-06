#!/usr/bin/python3
for i in range(26):
    if chr(i + 97) not in "eq":
        print('{}'.format(chr(i + 97)), end='')
