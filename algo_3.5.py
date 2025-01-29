n = int(input())
arr = []

def siftUp(arr, index):
    while((arr[index] > arr[int((index-1)/2)]) and index > 0):
        arr[index], arr[int((index - 1)/2)] = arr[int((index-1)/2)], arr[index]
        index = int((index - 1)/2)

def siftDown(arr):
    index = 0
    
    while 2*index + 1 < len(arr):
        left_child = 2*index + 1
        right_child = 2*index + 2

        '''
        largest = left_child

        if right_child < len(arr) and arr[right_child] > arr[left_child]:
            largest = right_child

        if arr[index] >= arr[largest]:
            break

        arr[index], arr[largest] = arr[largest], arr[index]
        index = largest
        '''

        if arr[index] < arr[left_child]:
            if ((2*index + 2) < len(arr)) and arr[right_child] > arr[left_child]:
                arr[index], arr[right_child] = arr[right_child], arr[index]
                index = right_child
            else:
                arr[index], arr[left_child] = arr[left_child], arr[index]
                index = left_child
                
        elif ((2*index + 2) < len(arr)) and arr[right_child] > arr[left_child]:
                arr[index], arr[right_child] = arr[right_child], arr[index]
                index = right_child    
        else:
            break


for i in range(n):
    operation = [int(element) for element in input().split()]

    if operation[0] == 0:
        arr.append(operation[1])
        siftUp(arr, len(arr) - 1)
    elif operation[0] == 1:
        print(arr[0])
        arr[0], arr[-1] = arr[-1], arr[0]
        arr.pop()
        siftDown(arr)


