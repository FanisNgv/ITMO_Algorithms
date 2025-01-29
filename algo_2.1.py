
input_str = input()

stack = []

for i in range(len(input_str)):
    try:
        if input_str[i] == '[' or input_str[i] == '{' or input_str[i] == '(':
            stack.append(input_str[i])
        elif input_str[i] == ']' and stack[-1] == '[':
            stack.pop()
        elif input_str[i] == '}' and stack[-1] == '{':
            stack.pop()
        elif input_str[i] == ')' and stack[-1] == '(':
            stack.pop()
    except:
        stack.append(input_str[i])

if len(stack) == 0:
    print("YES")
else:
    print("NO")