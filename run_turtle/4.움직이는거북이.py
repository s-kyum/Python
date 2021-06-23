#거북이 마음대로 왔다갔다
import turtle as t
import random as r
t.shape('turtle')
t.speed(0.5)

t.color('blue')
t.pensize(3)
t.bgcolor('black')
t.setup(1000,1000)
for i in range(1000):  #거북이 움직이는 횟수
    angle = r.randint(1,360) #거북이 방향(각도)
    t.setheading(angle)
    t.forward(30)
