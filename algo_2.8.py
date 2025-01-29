stack_of_numbers = []

math_expression = input().split()

for i in range(len(math_expression)):
    if (math_expression[i] == '+'):
        a = stack_of_numbers.pop()
        b = stack_of_numbers.pop()
        stack_of_numbers.append(a+b)
    elif (math_expression[i] == '-'):
        a = stack_of_numbers.pop()
        b = stack_of_numbers.pop()
        stack_of_numbers.append(b - a)
    elif (math_expression[i] == '*'):
        a = stack_of_numbers.pop()
        b = stack_of_numbers.pop()
        stack_of_numbers.append(a * b)
    else:
        stack_of_numbers.append(int(math_expression[i]))

print(stack_of_numbers.pop())

