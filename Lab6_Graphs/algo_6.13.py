inp = [int(x) for x in input().split()]

n = inp[0]
m = inp[1]
k = inp[2]
s = inp[3] - 1

nodes = []

for _ in range(m):
    inp = [int(x) for x in input().split()]
    v = int(inp[0]) - 1
    u = int(inp[1]) - 1
    w = int(inp[2])
    nodes.append((v, u, w))



inf = float('inf')
# dp - от s до каждой вершины с количеством ребер k

dp = [[inf] * n for _ in range(k + 1)]
dp[0][s] = 0

for k in range(1, k+1):
    for v, u, w in nodes:

        if dp[k-1][v] != inf:
            dp[k][u] = min(dp[k][u], dp[k-1][v] + w)



for v in range(n):
    
    if dp[k][v] == inf:
        print(-1)
    else:
        print(dp[k][v])