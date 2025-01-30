inp = [int(x) for x in input().split()]
n = inp[0]
m = inp[1]

coin_matrix = []
dp = [[float('-inf')] * m for _ in range(n)]
for i in range(n):
    row = [int(x) for x in input().split()]
    coin_matrix.append(row)

# БАЗА!
dp[0][0] = coin_matrix[0][0]

for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + coin_matrix[i][j]



print(dp[-1][-1])

i = n-1
j = m-1
path = []

# Пока не дойдем до исходной точки
while i!=0 or j!=0:
    # Тут проверим, каков был путь в предыдущем шаге
    if dp[i-1][j] == dp[i][j] - coin_matrix[i][j]:
        i -= 1
        path.append('D')
    else:
        j-= 1
        path.append('R')


answ = path[::-1]
print(''.join(map(str, answ)))

