assistant_stack = []

num_of_numbers = int(input())
main_stack = input().split()
main_stack = list(reversed([int(x) for x in main_stack]))

needed_number = 1
is_impossible = False
log = []

while True:
    while (len(assistant_stack) != 0 and assistant_stack[-1] == needed_number):
        assistant_stack.pop()
        needed_number += 1
        log.append('pop')
    if (len(main_stack) > 0):
        assistant_stack.append(main_stack.pop())
        log.append('push')
    if (len(assistant_stack) != 0 and assistant_stack[-1] == needed_number):
        assistant_stack.pop()
        needed_number += 1
        log.append('pop')
    elif (len(main_stack) > 0 and assistant_stack[-1] < main_stack[-1]):
        print('impossible')
        is_impossible = True
        break
    if (len(main_stack) == 0 and len(assistant_stack) == 0):
        break
if(not is_impossible):
    for element in log:
        print(element)

