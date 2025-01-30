# from sys import stdin
# import math
# import sys

# sys.setrecursionlimit(10**5)


# inversions_count = 0

# def merge(x: list, y: list):
#     global inversions_count
#     sorted_array = []
#     i = 0
#     j = 0

#     # Пока мы указателями можем перемещаться (хотя бы по одному из них, потому что нужно по обоим дойти до конца)
#     while (i < len(x) or j < len(y)):
#         # Проверяем, по какому из указателей элемент меньше
#         if (i == len(x)):
#             sorted_array.append(y[j])
#             j += 1
#         elif (j == len(y)):
#             sorted_array.append(x[i])
#             i += 1
#         elif x[i][0] < y[j][0]:
#             sorted_array.append(x[i])
#             i += 1
#         else:
#             sorted_array.append(y[j])
#             j += 1
    
#     return sorted_array

# def merge_sort(array: list):
#     if (len(array) == 1):
#         return array
#     first_half = []
#     second_half = []

#     if (len(array) % 2 == 0):
#         for i in range(int(len(array) / 2)):
#             first_half.append(array[i])
#         for j in range(int(len(array) / 2), len(array)):
#             second_half.append(array[j])
#     else:
#         for i in range(int(len(array) / 2)):
#             first_half.append(array[i])
#         for j in range(int(len(array) / 2), len(array)):
#             second_half.append(array[j])
    
#     x = merge_sort(first_half)
#     y = merge_sort(second_half)

#     return merge(x,y)





# n = int(input())

# nodes = []

# i = 0
# for _ in range(n):
#     inp = [int(x) for x in input().split()]
#     x = int(inp[0])
#     y = int(inp[1])
#     nodes.append((x, y))

# if n == 1:
#     print(0)
#     sys.exit()


# def distance(p1, p2):
#     return math.sqrt((p1[0]-p2[0])** 2 + (p1[1]-p2[1])** 2)

# edges = []
# for i in range(n):
#     for j in range(i + 1, n):
#         w = distance(nodes[i], nodes[j])
#         edges.append((w, i, j))

# edges = merge_sort(edges)

# matx = [[] for _ in range(n)]
# p = list(range(n))


# def find(v):
#     if p[v] == v:
#         return v
#     else:
#         return find(p[v])
    
# def union(u, v):
#     u = find(u)
#     v = find(v)

#     if u != v:
#         p[v] = u


# min_weight = 0
# for edge in edges:
#     w, u, v = edge
#     if find(u) != find(v):
#         union(u, v)
#         min_weight += w

# print(min_weight)






from sys import stdin
import math
import sys

sys.setrecursionlimit(10**5)


inversions_count = 0

def merge(x: list, y: list):
    global inversions_count
    sorted_array = []
    i = 0
    j = 0

    # Пока мы указателями можем перемещаться (хотя бы по одному из них, потому что нужно по обоим дойти до конца)
    while (i < len(x) or j < len(y)):
        # Проверяем, по какому из указателей элемент меньше
        if (i == len(x)):
            sorted_array.append(y[j])
            j += 1
        elif (j == len(y)):
            sorted_array.append(x[i])
            i += 1
        elif x[i][2] < y[j][2]:
            sorted_array.append(x[i])
            i += 1
        else:
            sorted_array.append(y[j])
            j += 1
    
    return sorted_array

def merge_sort(array: list):
    if (len(array) == 1):
        return array
    first_half = []
    second_half = []

    if (len(array) % 2 == 0):
        for i in range(int(len(array) / 2)):
            first_half.append(array[i])
        for j in range(int(len(array) / 2), len(array)):
            second_half.append(array[j])
    else:
        for i in range(int(len(array) / 2)):
            first_half.append(array[i])
        for j in range(int(len(array) / 2), len(array)):
            second_half.append(array[j])
    
    x = merge_sort(first_half)
    y = merge_sort(second_half)

    return merge(x,y)


inp = [int(x) for x in input().split()]
n = inp[0]
m = inp[1]

nodes = []

for _ in range(m):
    inp = [int(x) for x in input().split()]
    v = int(inp[0]) - 1
    u = int(inp[1]) - 1
    w = int(inp[2])
    nodes.append((v, u, w))

nodes = merge_sort(nodes)

p = list(range(n))
rank = [1]*n
 
def find(v):
    if p[v] != v:
        p[v] = find(p[v])
    return p[v]
    
def union(u, v):
    u = find(u)
    v = find(v)
 
    if u == v:
        return
    if rank[u] < rank[v]:
        p[u] = v
    else:
        p[v] = u
        if rank[u] == rank[v]:
            rank[u] += 1 


min_weight = 0

for node in nodes:
    u, v, w = node
    if find(u) != find(v):
        union(u, v)
        min_weight += w

print(min_weight)