#장바구니 클래스
class Cart:
    def __init__(self,goods):
        self.li = []
        self.li.append(goods)

    def showinfo(self):
        print(self.li)

c1=Cart("커피")
c1.showinfo()
c2=Cart("계란")
c2.showinfo()

#장바구니 누적
class Cart:
    li=[]
    def __init__(self,goods):
        Cart.li.append(goods)
    def showinfo(self):
        print(self.li)

c1=Cart('커피')
c1.showinfo()
c2=Cart('계란')
c2.showinfo()