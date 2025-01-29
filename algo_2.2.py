n = int(input())

first_player_deck = input().split()
second_player_deck = input().split()
first_player_deck = [eval(i) for i in first_player_deck]
second_player_deck = [eval(i) for i in second_player_deck]

head_first_player = 0
tail_first_player = int((n/2) - 1)
head_second_player = 0
tail_second_player = int((n/2) - 1)

steps = 0
while head_first_player <= tail_first_player and head_second_player <= tail_second_player and steps < 2e5:
        card1 = first_player_deck[head_first_player]
        card2 = second_player_deck[head_second_player]
        
        if (card1 == 0 and card2 == n - 1) or (card1 > card2 and not (card2 == 0 and card1 == n - 1)):
            first_player_deck.append(card1)
            head_first_player += 1
            tail_first_player += 1

            first_player_deck.append(card2)
            head_second_player += 1
            tail_first_player += 1
        else:
            second_player_deck.append(card1)
            head_first_player += 1
            tail_second_player += 1

            second_player_deck.append(card2)
            head_second_player += 1
            tail_second_player += 1
        
        steps += 1

if(head_first_player > tail_first_player):
    print('second', steps)
elif(head_second_player > tail_second_player):
    print('first', steps)
else:
    print('draw')