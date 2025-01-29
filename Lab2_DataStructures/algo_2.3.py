n = int(input())
first_railway = list(reversed(input().split()))
first_railway = [int(x) for x in first_railway]

second_railway = []
dead_end = []
logs = []

next_element = 1

while len(first_railway) > 0 or len(dead_end) > 0:

    if len(dead_end) > 0 and dead_end[-1] == next_element:
        second_railway.append(dead_end.pop())
        logs.append('2 1')
        next_element += 1

    elif len(first_railway) > 0:
        dead_end.append(first_railway.pop())
        logs.append('1 1')

    else:
        logs = ['0']
        break

for element in logs:
    print(element)
