from ch07.myclass.converter import ScaleConverter
#단위 변환 클래스 확장(상속)
#온도 변환 - 화씨(F) = 섭씨(C) X 1.8 + 32
class Converters(ScaleConverter):
    def __init__(self,units_from,units_to,factor,offset):
        super().__init__(units_from,units_to,factor)
        self.offset = offset

    def convert(self,val):  #부모 메서드 이름이 같고 내용이 다르다 : 재정의(오버라이드)
        return self.factor*val + self.offset

con = Converters('C','F',1.8,32)
print("converting 20C")
print(str(con.convert(20))+con.units_to)
