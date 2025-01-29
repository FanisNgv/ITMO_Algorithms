first_deq = [None] * (5 * 10**5)  
second_deq = [None] * (5 * 10**5)  
 
head_1 = 0  
tail_1 = 0  
 
head_2 = 0  
tail_2 = 0  
 
num_of_operations = int(input())  
 
for _ in range(num_of_operations):
    current_operation = input().split()
 
    if current_operation[0] == '+':
        second_deq[tail_2] = int(current_operation[1])
        tail_2 += 1
 
    elif current_operation[0] == '*':
        first_deq[tail_1] = int(current_operation[1])
        tail_1 += 1
 
 
    elif current_operation[0] == '-':
        if head_1 < tail_1:
            print(first_deq[head_1])
            head_1 += 1
        else:
            print(second_deq[head_2])
            head_2 += 1
 
    # Балансировка
    if (tail_2 - head_2) > (tail_1 - head_1):
        first_deq[tail_1] = second_deq[head_2]
        tail_1 += 1
        head_2 += 1
    elif ((tail_1 - head_1) - (tail_2 - head_2) > 1):
        head_2 -= 1
        second_deq[head_2] = first_deq[tail_1 - 1]
        tail_1 -= 1