#!/usr/bin/python3
for n in range(100):
    if n < 10:
        single_digit = ("0" + n)
   else:
        continue
    if n < 99:
         print("{1}{0}, ".format(n, single_digit), end="")
    else:
        print("{} ".format(n), end="")
