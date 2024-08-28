#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string1 = f"Last digit of {number}"
s = str(number)
if number < 0:
    last = int('-' + s[-1])
else:
    last = int(s[-1])
string2 = f" is {last}"
if number < 0:
    print(string1 + string2 + " and is less than 6 and not 0")
elif last != 0 and last < 6:
    print(string1 + string2 + " and is less than 6 and not 0")
elif last == 0:
    print(string1 + string2 + " and is 0")
else:
    print(string1 + string2 + " and is greater than 5")
