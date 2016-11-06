#!/bin/python3
import sys

x1, v1, x2, v2 = input().strip().split(' ')
# unpacking
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

done = False

if v2 >= v1:
    print("NO")
else:
    i = 1
    if (x2 - x1) / (v1 - v2) == (x2 - x1) / (v1 - v2):
        while not done:
            if (x1 + i * v1 > x2 + i * v2):
                done = True
                print("NO")
            if (x1 + i * v1 == x2 + i * v2):
                done = True
                print("YES")
            i += 1
    else:
        print("NO")
