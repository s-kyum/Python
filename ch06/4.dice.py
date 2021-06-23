import random
#주사위 10번 던지기

dice = random.randint(1,6)
print(dice)

for i in range(10): #0부터 10개
    dice=random.randint(1,6)
    print(dice)

print('='*50)

#리스트에서 랜덤하게 단어 추출하기

w=['ashe','winston','ana','echo','soldier76','mercy','widow']
random.choice(w)
print(random.choice(w))

