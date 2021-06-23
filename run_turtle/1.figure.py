#도형 그리기
import turtle as t
t.shape("turtle")

#사각형 그리기
t.color('blue')
t.pensize(5)
for i in range(4):
    
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(50)
    t.forward(100)
    t.right(50)
   
#삼각형 그리기
t.color('red')
t.pensize(5)
n=5
for i in range(n):
    t.forward(100)
    t.left(360/n)
#원
t.color('blue')
for i in range(2):
    t.circle(50)
    t.forward(50)
