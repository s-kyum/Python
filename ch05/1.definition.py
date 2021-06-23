#함수의 정의 및 호출
# return이 없고 매개변수 없는 함수

def say_good():
    print('very Good!')

say_good() #호출

#return이 없고 매개변수 있는 함수

def say_welcome(name):
    print("{}님 반갑습니다.".format(name))
name=input("이름을 입력하세요")
say_welcome(name)
