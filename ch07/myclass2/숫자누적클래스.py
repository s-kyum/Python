#인스턴스 변수
class Counter:
    def __init__(self):
        self.x = 0    #인스턴스 변수(heap영역)
        self.x = self.x + 1
    def showinfo(self):
        print(self.x)

c=Counter()
c.showinfo()
c1=Counter()
c1.showinfo()
c2=Counter()
c2.showinfo()

#클래스 변수
class Counter2:
    x=0      #클래스 변수(전역변수)
    def __init__(self):
        Counter2.x = Counter2.x + 1
    def showinfo(self):
        print(self.x)
c=Counter2()
c.showinfo()
c1=Counter2()
c1.showinfo()
c2=Counter2()
c2.showinfo()
