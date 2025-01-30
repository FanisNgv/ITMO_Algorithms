

inp = [int(x) for x in input().split()]
n = inp[0]
k = inp[1]
profit_array = [0]*n
input_values = list(map(int, input().split()))
for i in range(1, n - 1):
    profit_array[i] = input_values[i - 1]

# print(profit_array)

dp = [float('inf')] * n
path = [0] * n

# БАЗА
dp[0] = profit_array[0]

for i in range(1, n):
    min = i - 1
    for j in range(max(0, i - k), i):
        if dp[min] < dp[j]:
            min = j
    
    dp[i] = dp[min] + profit_array[i]
    path[i] = min

print(max(dp[-1], dp[-2]))


cur = n - 1
temp = [cur + 1]
while cur != 0:
    cur = path[cur]
    temp.append(cur+1)

answ = temp[::-1]

print(len(answ)-1)

print(' '.join(map(str, answ)))


