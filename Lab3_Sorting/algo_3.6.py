n = int(input())
arr = [int(x) for x in input().split()]
k = int(input())
log = []

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

def lower_bound(arr, element):
    l = -1
    r = len(arr)
    while (r - l > 1):
        mid = (l + r)//2
        if checker_for_lower(arr, element, mid):
            r = mid
        else:
            l = mid
    return r

def upper_bound(arr, element):
    l = -1
    r = len(arr)
    while (r - l > 1):
        mid = (l + r)//2
        if checker_for_upper(arr, element, mid):
            r = mid
        else:
            l = mid
    return r
def checker_for_lower(arr, element, mid):
    if arr[mid] >= element:
        return True
    else:
        return False
    
def checker_for_upper(arr, element, mid):
    if arr[mid] > element:
        return True
    else:
        return False

arr = merge_sort(arr)

lower_bound(arr, 9)

for i in range(k):
    input_edges = [int(edge) for edge in input().split()]
    l_element, r_element = input_edges[0], input_edges[1]

    l_index = lower_bound(arr, l_element)
    r_index = upper_bound(arr, r_element)

    num_of_relevants = r_index - l_index
    log.append(num_of_relevants)

for element in log:
    print(element, end = ' ')
