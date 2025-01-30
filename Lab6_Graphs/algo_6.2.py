inp = [int(x) for x in input().split()]
n = inp[0]
m = inp[1]

matx = [[] for _ in range(n)]

for _ in range(m):
    operation = input().split()
    x = int(operation[0])-1
    y = int(operation[1])

    if y not in matx[x]:
        matx[x].append(y)
    if x + 1 not in matx[y - 1]:
        matx[y - 1].append(x + 1)

visited_nodes = [0 for _ in range(n)]

# Обход только по связному графу, до других компонент мы не дойдем
def dfs(v, p, color):
    stack = []
    stack.append((v, p))

    while stack:
        v, p = stack.pop()
        if visited_nodes[v - 1] == 0:
            visited_nodes[v - 1] = color
            for neighbor in matx[v - 1]:
                if neighbor != p and not visited_nodes[neighbor - 1]:
                    stack.append((neighbor, v))

    # visited_nodes[v-1] = color
    # for neighbor in matx[v-1]:
    #     if (neighbor != p and not visited_nodes[neighbor-1]):
    #         dfs(neighbor, v, color)

color = 1

for i in range(n):
    if visited_nodes[i] == 0:
        dfs(i+1, -1, color)
        color += 1

for element in visited_nodes:
    print(element, end = ' ')
