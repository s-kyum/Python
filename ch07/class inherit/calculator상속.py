#Calculator를 확장(상속)한 클래스 만들기
from ch07.myclass.calculator2 import Calculator
#제곱수 계산하는 기능(함수)추가
class UpCalculator(Calculator):
    def pow(self):
        return self.x **self.y

    def div(self):           #div(x,y)에서 y값이 0일떄 다운되는 현상 방지
        if self.y ==0:
            return "0으로 나눌 수 없습니다."
        else:
            return self.x/self.y
c2=UpCalculator(5,0)
print(c2.pow())
print(c2.add())
print(c2.mul())
print(c2.div())