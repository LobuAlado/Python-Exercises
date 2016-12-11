#Junkenpo with lists

from random import randint

hand1 = [0,0,0]
hand2 = [0,0,0]

print("Welcome to JunKenPo game with lists")
for i in range(0,10):
    sort = randint(0,2)
    hand1[sort] = 1
    sort = randint(0,2)
    hand2[sort] = 1

    #Player hand
    if hand1[0] == 1:
        print("Player - Rock")
    elif hand1[1] == 1:
        print("Player - Paper")
    elif hand1[2] == 1:
        print("Player - Scissor")

    #Enemy hand
    if hand2[0] == 1:
        print("Enemy - Rock")
    elif hand2[1] == 1:
        print("Enemy - Paper")
    elif hand2[2] == 1:
        print("Enemy - Scissor")

    #Selecting the hands
    for i in range(0,3):
        if hand1[i] == 1:
            attack = i
        if hand2[i] == 1:
            defense = i

    #Chossing the winner
    if attack == 0 and defense == 2:
        print("Player win\n")
    elif attack == 1 and defense == 0:
        print("Player win\n")
    elif attack == 2 and defense == 1:
        print("Player win\n")
    elif attack == defense:
        print("Drawn\n")
    elif attack == 2 and defense == 0:
        print("Enemy win\n")
    elif attack == 0 and defense == 1:
        print("Enemy win\n")
    elif attack == 1 and defense == 2:
        print("Enemy win\n")
    
    hand1 = [0,0,0]
    hand2 = [0,0,0]
