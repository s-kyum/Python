#영어 타자 연습 프로그램
import random
import time
f = open('words.txt','r')
word = f.read().split()
#print(word)
f.close()

n = 1 #문제번호
print("[타자게임]준비되면 엔터")
input()
start=time.time()
q = random.choice(word) #무작위 단어 출제
while n<=10:
    print("문제",n)
    print(q)
    x = input()  #user가 입력하는 단어
    if x == q :
        print("통과")
        n=n+1
        q = random.choice(word)
    else:
        print("오타입니다.")
print("게임종료")
end = time.time()
et = end-start
print("타자시간 : %.2f초" %et)