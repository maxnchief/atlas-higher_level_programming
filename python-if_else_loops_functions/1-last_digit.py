#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = str(number)
last = int(s[-1])
spot = "hello"
if number < 0:
    result = spot.replace ("hello", "and is less than 6 and not 0")
elif last != 0 and last < 6:
    result = spot.replace ("hello", "and is less than 6 and not 0")
elif last == 0:
    result = spot.replace ("hello", "and is 0")
else: 
    result = spot.replace ("hello", "and is greater than 5")
print(f"Last digit of {number} is {last} {result}")