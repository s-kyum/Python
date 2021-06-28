import time

print(time.time()) #1970.01.01 자정이후를 초로 환산
print(time.ctime()) #날짜/시간/요일 표시
print(time.localtime())
print(time.strftime('%x',time.localtime()))
print(time.strftime('%c',time.localtime()))

#time.sleep(1) : 1초간 대기 / 파이썬에서만 1초를 1로 표기 다른언어에서는 1000을 곱해서 표기

for i in range(1,11):
    print(i)
    time.sleep(1)
    
    
