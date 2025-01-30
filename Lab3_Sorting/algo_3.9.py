import math
import sys

eps = 0.0000001
number = float(input())

l = -1
r = number

res = sys.maxsize

while abs(res-number) > eps:
    mid = (l + r)/2
    res = (mid**2 + math.sqrt(mid))
    if res - number >= eps:
        r = mid
    else:
        l = mid

print(round(r, 6))
