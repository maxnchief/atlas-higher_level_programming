#!/usr/bin/python3
n = 96
while n < 122:
    n += 1
    if n == 101 or n == 113:
        pass
    else:
        print("{}".format(chr(n)), end="")
