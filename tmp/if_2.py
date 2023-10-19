#!/usr/bin/python3
import sys

minus = 0
seifu = 0

for n in sys.argv[1:]:
    x = float(n)

    if x < 0.0:
        minus += 1
    else:
        seifu += 1

print("負:", minus)
print("非負", seifu)
