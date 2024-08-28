#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = str(number)
last = int(s[-1])
print(f"Last digit of {number} is {last}")
if last != 0 and last < 6:
    print(f"and is less than 6 and not 0")
elif last = 0:
    print(f"and is 0")
else: 
    print(f"and is greater than 5")
    