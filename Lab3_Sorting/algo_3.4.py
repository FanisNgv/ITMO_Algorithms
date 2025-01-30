'''
Если 2i⩽n, то a[i]⩽a[2i]
Если 2i+1⩽n, то a[i]⩽a[2i+1]
'''

num_of_elements = int(input())
array_of_elements = [int(x) for x in input().split()]
is_heap = True

for i in range(len(array_of_elements)//2):
    if(num_of_elements % 2 != 0 and (array_of_elements[i] >= array_of_elements[2*i + 1] or array_of_elements[i] >= array_of_elements[2*i +2])):
        is_heap = False
        print("NO")
        break
    elif (array_of_elements[i] >= array_of_elements[2*i + 1]):
        is_heap = False
        print("NO")
        break
if (is_heap):
    print("YES")
