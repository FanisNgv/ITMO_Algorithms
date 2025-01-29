stack = []
stack_of_mins = []
log = []

operations_num = int(input())

for i in range(operations_num):
    current_operation = input().split()

    if current_operation[0] == '1':
        elem_to_append = int(current_operation[1])
        stack.append(elem_to_append)
        
        if (len(stack_of_mins) == 0):
            stack_of_mins.append(elem_to_append)

        elif(elem_to_append <= stack_of_mins[-1]):
            stack_of_mins.append(elem_to_append)

    elif current_operation[0] == '2':
        if stack[-1] == stack_of_mins[-1]:
            stack_of_mins.pop()
        stack.pop()
    
    elif current_operation[0] == '3':
        log.append(stack_of_mins[-1])

for element in log:
    print(element)
