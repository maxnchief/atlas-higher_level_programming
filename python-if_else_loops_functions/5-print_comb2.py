#!/usr/bin/python3
for n in range(100):
    s = str(n)
    if n < 10:
        single_digit = ("0")
    elif n >= 10:
        single_digit = ("")
    else:
        pass
    if n < 99:
        print("{1}{0}, ".format(n, single_digit), end="")
    else:
        print("{}\n".format(n), end="")
