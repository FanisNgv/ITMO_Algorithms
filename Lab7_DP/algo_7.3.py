n = int(input())
arr = [int(x) for x in input().split()]

dp = [1] * n
path = [-1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            path[i] = j


max_index = dp.index(max(dp))
res = []

while max_index != -1:
    res.append(arr[max_index])
    max_index = path[max_index]

res = res[::-1]

print(len(res))
print(' '.join(map(str, res)))
