n = int(input())

adj_matrix = []

for i in range(n):
    row = [int(x) for x in input().split()]
    adj_matrix.append(row)



# d = [[float('inf')] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             d[i][j] = 0  # Расстояние от вершины до самой себя равно 0
#         elif adj_matrix[i][j] != 0:
#             d[i][j] = adj_matrix[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][k] + adj_matrix[k][j] < adj_matrix[i][j]:
                adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]

for row in adj_matrix:
    print(" ".join(map(str, row)))