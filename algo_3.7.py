sizes = [int(size) for size in input().split()]
n, k = sizes[0], sizes[1]
arr_1 = [int(x) for x in input().split()]
arr_2 = [int(y) for y in input().split()]

log = []

def lower_bound_more(arr, element):
    l = 0
    r = len(arr) - 1
    while (r - l > 1):
        mid = (l + r)//2
        if checker_for_lower_more(arr, element, mid):
            r = mid
        else:
            l = mid
    return r

def checker_for_lower_more(arr, element, mid):
    if arr[mid] >= element:
        return True
    else:
        return False
    
def lower_bound_less(arr, element):
    l = 0
    r = len(arr) - 1
    while (r - l > 1):
        mid = (l + r)//2
        if checker_for_lower_less(arr, element, mid):
            r = mid
        else:
            l = mid
    return l

def checker_for_lower_less(arr, element, mid):
    if arr[mid] >= element:
        return True
    else:
        return False


for i in range(k):
    relevant_index_more = lower_bound_more(arr_1, arr_2[i])
    relevant_index_less = lower_bound_less(arr_1, arr_2[i])

    if (abs(arr_1[relevant_index_more] - arr_2[i]) >= abs(arr_1[relevant_index_less] - arr_2[i])):
        log.append(arr_1[relevant_index_less])
    else:
        log.append(arr_1[relevant_index_more])

for element in log:
    print(element)