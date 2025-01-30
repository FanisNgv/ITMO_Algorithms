n, x, y = [int(inp) for inp in input().split()]
    
l = -1
r = n*min(x, y)
n -= 1

while r - l > 1:
    mid = (l + r)//2
    res = (mid // x + mid // y)
    if res >= n:
        r = mid
    else:
        l = mid    

total_minutes = r + min(x, y)
print(total_minutes)
