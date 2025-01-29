queue = [None] * 10**5
head = 0
tail = 0
num_of_operations = int(input())
count_before = [0] * 10**5

log = []

for _ in range(num_of_operations):
    current_operation = input().split()
    current_operation = [int(x) for x in current_operation]

    if current_operation[0] == 1:
        queue[tail] = current_operation[1]
        count_before[current_operation[1]-1] = tail - head
        tail += 1

    elif current_operation[0] == 2:
        head_id = queue[head]
        count_before[head_id-1] = None
        for i in range(head+1, tail):
            count_before[queue[i]-1] -= 1
        head += 1

    elif current_operation[0] == 3:
        count_before[queue[tail-1]-1] = 0
        tail -= 1

    elif current_operation[0] == 4:
        log.append(count_before[current_operation[1]-1])

    elif current_operation[0] == 5:
        log.append(queue[head])

for element in log:
    print(element)
