#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10 if number >= 0 else -(-number % 10)

print(f"Last digit of {number} is {last} and is ", end="")

if last > 5:
    print("greater then 5")
elif last == 0:
    print("0")
else:
    print("less then 6 and not 0")
