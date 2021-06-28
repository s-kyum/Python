#숫자 추측 게임

import random

com = random.randint(1,100)
while True:
    try:
        guess = int(input("맞혀보세요(1~100):"))
        if guess > 100 or guess < 1:
            print("100이하의 숫자를 입력해주세요")
        elif guess == com:
            print("정답")
            break
        elif guess > com:
            print("예상한 숫자보다 작습니다.")
        elif guess < com:
            print("예상한 숫자보다 큽니다.")

    except ValueError:
        print("숫자가 아닙니다. 다시 입력해주세요.")

