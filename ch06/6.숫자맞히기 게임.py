#숫자 추측 게임

import random

com = random.randint(1,100)
while True:
    guess = int(input("맞혀보세요(1~100):"))
    if guess > com:
        print("예상한 숫자보다 작습니다.")
    if guess < com:
        print("예상한 숫자보다 큽니다.")
    if guess == com:
        print("정답")
        break
    
