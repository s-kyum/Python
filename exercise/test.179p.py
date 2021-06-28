#홀수인지 짝수인지 판별
def is_odd(number):
    if number%2!=0:
        return True
    else:
        return False

print(is_odd(5))

#입력된 모든 수의 평균구하는 프로그램
#가변 매개변수
def avg_numbers(*args):
    result=0
    for i in args:
        result +=i
    return result/len(args)

print(avg_numbers(1,2))
print(avg_numbers(7500,10000,15000,8000,10000))

#두개의 숫자를 입력받아 더하기
input1=int(input("첫번째 숫자를 입력하세요."))
input2=int(input('두번째 숫자를 입력하세요.'))

total=input1+input2
print('두 수의 합은 %s입니다.'%total) #%d도 가능

#출력결과가 다른것 하나
print("you" "need" "python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))

