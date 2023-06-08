#!/usr/bin/python3
import hidden_4

for name in dir(hidden_4):
    if '__' not in name:
        print(name)
