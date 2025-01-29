num_of_elements = int(input())
numbers = input().split()
numbers = [int(element) for element in numbers]
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
        elif (x[i] < y[j]):
            sorted_array.append(x[i])
            i += 1
        elif (x[i] >= y[j]):
            sorted_array.append(y[j])
            # Потому что все оставшиеся элементы в иксе больше текущего игрека, их нужно посчитать!
            inversions_count += len(x) - i
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


merge_sort(numbers)
print(inversions_count)