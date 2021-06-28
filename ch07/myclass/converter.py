#단위 변환 클래스
class ScaleConverter:   #1인치 - 2.54cm - 25.4mm
    def __init__(self,units_from,units_to,factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, val):
        return self.factor*val


if __name__ == "__main__":
    c=ScaleConverter("inches","mm",25.4)
    print("Converting 2 inches")
    print(str(c.convert(2))+c.units_to)