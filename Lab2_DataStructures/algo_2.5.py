input_balls = input().split()
input_balls = [int(x) for x in input_balls]
stack = []
deleted_elements = 0

for i in range(len(input_balls)):
    if (len(stack) == 0):
        stack.append([input_balls[i], 1])
    else:
        if (stack[-1][0] == input_balls[i]):
            stack[-1][-1] += 1
            if (i < len(input_balls) - 1 and stack[-1][0] != input_balls[i+1] and stack[-1][-1] >= 3):
                deleted_elements += stack[-1][-1]
                stack.pop()
        else:
            stack.append([input_balls[i], 1])

if stack[-1][-1] >= 3:
    deleted_elements += stack[-1][-1]
    stack.pop()    
    
print(deleted_elements)
