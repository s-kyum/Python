#전역 변수의 범위
def price():
    price = 250*quantity
    print("{}원 입니다.".format(price))

quantity=2 #전역변수
price()
