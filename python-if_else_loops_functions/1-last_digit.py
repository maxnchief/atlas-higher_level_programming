#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = str(number)
last = int(s[-1])
print(f"Last digit of {number} is {last}")