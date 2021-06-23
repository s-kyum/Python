#주사위 2개를 10번 던지기

import random
dice1=random.randint(1,6)
dice2=random.randint(1,6)

for i in range(10):
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        total = dice1+dice2
        print('dice1=',dice1,'dice2=',dice2,'total=',total)
        if total ==7:
            print("seven!")
        if total == 11:
            print("eleven!")
        if dice1==dice2:
            print("doble!")
