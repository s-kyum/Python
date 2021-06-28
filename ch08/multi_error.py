#다중 예외 처리
try:
    a = ['사과','메론']
    print(a[2])
    4/0
except IndexError:
    print("리스트범위를 초과하였습니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")