import sys
sys.setrecursionlimit(10001)

def dfs1(v, visited, order:list, matx):
    visited[v] = True

    for u in matx[v]:
        if not visited[u]:
            dfs1(u, visited, order, matx)

    order.append(v)

def dfs2(v, num, visited, component_num, reverse_matx):
    visited[v] = True
    component_num[v] = num

    for u in reverse_matx[v]:
        if not visited[u]:
            dfs2(u, num, visited, component_num, reverse_matx)

def main():
    inp = [int(x) for x in input().split()]
    n = inp[0]
    m = inp[1]
    mapping = {}
    current_number = 0
    names = [input() for _ in range(n)]


    for name in names:
        mapping[f"-{name}"] = current_number
        current_number += 1
        mapping[f"+{name}"] = current_number
        current_number += 1


    matx = [[] for _ in range(2 * n)]
    reversed_matx = [[] for _ in range(2 * n)]

    for _ in range(m):
        inp = input().split()
        frm = mapping[inp[0]]
        to = mapping[inp[2]]
        matx[frm].append(to)
        reversed_matx[to].append(frm)



    visited = [False] * (2 * n)
    order = []


    for i in range(2 * n):
        if not visited[i]:
            dfs1(i, visited, order, matx)

    visited = [False] * (2 * n)
    component_num = [0] * (2 * n)
    num_components = 0


    for v in reversed(order):
        if not visited[v]:
            dfs2(v, num_components, visited, component_num, reversed_matx)
            
            num_components += 1
            
    for i in range(0, 2 * n, 2):
        if component_num[i] == component_num[i + 1]:
            print(-1)
            return

    condensed_matx = [[] for _ in range(num_components)]
    for v in range(2 * n):
        for u in matx[v]:
            if component_num[v] != component_num[u]:
                condensed_matx[component_num[v]].append(component_num[u])



    assignment = [False] *(2 * n)

    for v in reversed(order):
        if not assignment[v]:
            assignment[v] = True
        if v%2 == 0:
            assignment[v + 1] = False
        else:
            assignment[v - 1] = False        
    
    result = []

    for i in range(0, 2 * n, 2):
        if assignment[i + 1]:
            result.append(names[i//2])




    print(len(result))
    for name in result:
        print(name)

if __name__ == "__main__":
    main()