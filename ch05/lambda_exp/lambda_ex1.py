#매개 변수가 1개 있는 lambda 함수(익명 함수)

#1을 더하는 함수
oneup = lambda x : x+1                    # = def oneup(x):
print(oneup(2))                              # = return x + 1
print((lambda x : x+1)(3))   #변수 선언없이 바로 실행

#3의 배수를 계산하는 함수
times = lambda x : x*3
print(times(5))
print((lambda x : x*3)(5))
