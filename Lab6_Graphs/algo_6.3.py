# import sys
# from sys import stdin

# sys.setrecursionlimit(2*10**5)

# inp = list(map(int, input().split()))
# n = inp[0] # количество вершин
# m = inp[1] # количество операций

# ancestors = list(map(int, sys.stdin.readline().strip().split()))

#  # нулевой элемент - это то, кто является предком для второй вершины и т.д.

# matx = [[] for _ in range(n)]

# for i in range(n-1):
#     x = ancestors[i] - 1
#     y = i + 2
#     matx[x].append(y)


# #print(matx)

# visited_nodes = [[0, 0] for _ in range(n)] # первое - посещена или нет, второе - когда зашли, третье - когда вышли
# time_count = 0

# # def dfs(v, time_count):
# #     stack = []
# #     stack.append((v, 0))

# #     while stack:
# #         v, neighbor_index = stack.pop()

# #         if neighbor_index == 0:
# #             time_count += 1
# #             visited_nodes[v - 1][0] = time_count
# #         if neighbor_index < len(matx[v - 1]):
# #             neighbor = matx[v - 1][neighbor_index]
# #             stack.append((v, neighbor_index + 1))

# #             if not visited_nodes[neighbor - 1][0]:
# #                 stack.append((neighbor, 0))
# #         else:
# #             time_count += 1
# #             visited_nodes[v - 1][1] = time_count

# #     return time_count

# def dfs(v):
#     global time_count
#     time_count += 1
#     visited_nodes[v - 1][0] = time_count
#     for neighbor in matx[v - 1]:
#         if visited_nodes[neighbor - 1][0] == 0:
#             dfs(neighbor)

#     time_count += 1
#     visited_nodes[v - 1][1] = time_count
        
# dfs(1)
# #print(visited_nodes)

# for operation in stdin:
#     operation = operation.split()
#     a, b = int(operation[0])-1, int(operation[1])-1
#     a_in, a_out = visited_nodes[a]
#     b_in, b_out = visited_nodes[b]
 
#     if a_in <= b_in <= b_out <= a_out:
#         print(1)
#     else:
#         print(0)

import sys

inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]

ancestors = list(map(int, sys.stdin.readline().strip().split()))

matx = [[] for _ in range(n)]

for i in range(n-1):
    parent = ancestors[i]-1
    child = i + 2
    matx[parent].append(child)

time_in_out = [[0, 0] for _ in range(n)]

time_count = 0

def dfs(v):
    global time_count
    time_count += 1
    time_in_out[v - 1][0] = time_count

    for neighbor in matx[v - 1]:
        if time_in_out[neighbor - 1][0] == 0:
            dfs(neighbor)

    time_count += 1
    time_in_out[v - 1][1] = time_count

dfs(1)

for operation in sys.stdin:
    operation = operation.split()
    a, b = int(operation[0])-1, int(operation[1])-1
    a_in, a_out = time_in_out[a]
    b_in, b_out = time_in_out[b]
 
    if a_in <= b_in <= b_out <= a_out:
        print(1)
    else:
        print(0)