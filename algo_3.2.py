auxiliary_array = [0] * (100+1)
num_of_elements = int(input())
input_array = [int(num) for num in input().split()]

for i in range(len(input_array)):
    auxiliary_array[input_array[i]] += 1

for i in range(len(auxiliary_array)):
    if (auxiliary_array[i] != 0):
        print((str(i)+' ')*auxiliary_array[i], end='')
