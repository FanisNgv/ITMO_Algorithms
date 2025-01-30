def merge(x: list, y: list):
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
        elif (x[i] < y[j]):
            sorted_array.append(x[i])
            i += 1
        elif (x[i] >= y[j]):
            sorted_array.append(y[j])
            j += 1
    
    return sorted_array

def merge_sort(array: list):
    if (len(array) == 1 or len(array) == 0):
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

matx = [[] for _ in range(n)]

for _ in range(m):
    operation = input().split()
    x = int(operation[0])-1
    y = int(operation[1])
    matx[x].append(y)

#print(matx)
print(n)
for i in range(n):
    matx[i] = merge_sort(matx[i])
    print(len(matx[i]), end=" ")
    for j in range(len(matx[i])):
        print(matx[i][j], end = ' ')
    print()
# matx = [ [ 0 for i in range(n) ] for j in range(n) ]


# for _ in range(m):
#     operation = input().split()
#     matx[int(operation[0])-1][int(operation[1])-1] = 1

# #print(matx)
# print(n)

# for i in range(n):
#     res = [0]
#     for j in range(n):
#         if matx[i][j] == 1:
#             res[0] += matx[i][j]
#             res.append(j+1)

#     for element in res:
#         print(element, end=" ")
#     print()