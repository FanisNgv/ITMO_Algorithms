import heapq

def dijkstra(adj_matrix, start, end):
    n = len(adj_matrix)
    dist = [float('inf')] * n

    dist[start] = 0 # От текущей вершины до нее самой же
    heap = [(0, start)] # Используем кучу, храним расстояние и до куда идти 
    
    # Пока у нас есть куча
    while heap:
        cur_dist, u = heapq.heappop(heap)
        # Если дошли до нужной вершины
        if u == end:
            return cur_dist
        # Если текущее расстояние у нас больше, чем то, что у нас в массиве расстояний, то смысла что-то менять нет
        if cur_dist > dist[u]:
            continue
        
        for v in range(n):
            if adj_matrix[u][v] != -1:
                new_dist = dist[u]+adj_matrix[u][v]

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))
    
    return -1


inp = [int(x) for x in input().split()]

n = inp[0]
s = inp[1] - 1
f = inp[2] - 1

adj_matrix = []

for i in range(n):
    row = [int(x) for x in input().split()]
    adj_matrix.append(row)


print(dijkstra(adj_matrix, s, f))