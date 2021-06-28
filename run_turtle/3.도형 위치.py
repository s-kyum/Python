#도형 위치 맘대로
import turtle as t
t.shape('turtle')
def polygon(n):
    for x in range(n):
        t.forward(100)
        t.left(360/n)

def polygon2(n, d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)

polygon(3)

t.up() # 선올리기
t.back(100)
t.left(90)
t.forward(100)

t.down()
polygon2(5,150)

t.up()
t.forward(200)
t.right(90)
t.forward(100)
t.down()
polygon(4)

t.up()
t.right(90)
t.forward(500)

t.down()
t.circle(50)

t.mainloop()
