#while 문 (반복)
'''
i=1
while i < 11:
    print('hello~')
    i += 1
'''
'''
#1부터 10까지 출력
i=1
sum=0
while i < 11:
    sum += i
    #print(i,  end=' ') #수평으로 출력하기
    print("i=",i,",sum=",sum)
    i += 1
print("합계 : ",sum)

#while~if break 반복조건문
i=1
while True:
    print(i)
    i += 1
    if i>10:
        break
'''
#while~break
i=1
while True:
    print("반복을 계속할까요? [y/n] : ")
    answer = input()
    if answer =='y' or answer =='Y':
        print("반복을 계속합니다.")
        i+=1
        print(i)
    elif answer =='n' or answer =='N':
        print("반복을 중단합니다.")
        break
    else:
        print("잘못된 입력입니다.")
