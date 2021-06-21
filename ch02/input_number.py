#숫자를 입력 받기

print("숫자를 입력해 주세요 : ")
num = input()
print("입력하신 숫자는",num,"입니다.")
print(type(num))  #숫자가 아닌 문자로 나옴(str)


print("숫자를 입력해 주세요 : ")
num2 = int(input())   #int : 문자 ->숫자로 형변환
print(num2)
print(type(num2))

print("숫자를 입력해주세요 : ")
num3 = int(input())
print("제곱수 : ",num3*num3,)
print(type(num3))
