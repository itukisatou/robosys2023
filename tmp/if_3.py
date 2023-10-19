#!/usr/bin/python3
import sys

minus = 0
zero = 0
plus = 0

for n in sys.argv[1:]:
    x = float(n)

    if x < 0.0:
        minus += 1
    elif x == 0.0:
        zero += 1
    else:
        plus += 1

print("負:", minus)
print("ゼロ:", zero)
print("正:", plus)
