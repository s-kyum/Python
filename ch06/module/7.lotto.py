#로또 번호 생성

import random as r
lotto=[]

for x in range(6):
    n=r.randint(1,45)
    if n not in lotto:
        lotto.append(n)
    #if len(lotto) ==6:   <<이렇게 해도 중복되면 5개밖에 출력안됌 
        #break

print(lotto)

lotto2=[]
while len(lotto2)<6:
     n=r.randint(1,45)
     if n not in lotto2:
        lotto2.append(n)
print(lotto2)
