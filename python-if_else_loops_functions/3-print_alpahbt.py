#!/usr/bin/python3
n = 97
while n < 123:
  n += 1
  if not n == 101 or 113:
    print("{}".format(chr(n)), end="")
  else:
    continue
