#!/usr/bin/python3
n = 97
while n < 123:
  n += 1
  if not n == 99 or 120:
    print("{}".format(chr(n)), end="")
  else:
    continue
