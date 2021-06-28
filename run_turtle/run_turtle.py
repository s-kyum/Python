import random
import turtle as t
from turtle import Turtle

def turn_right(): #오른쪽 화살키
    t.setheading(0)
    t.forward(10)

def turn_up(): #위쪽 화살키
    t.setheading(90)
    t.forward(10)

def turn_left(): #왼쪽 화살키
    t.setheading(180)
    t.forward(10)

def turn_down(): #아래쪽 화살키
    t.setheading(270)
    t.forward(10)

def play():
    t.forward(10)
    te.forward(9)
    #적거북이가 주인공을 쫓아감
    ang=te.towards(t.pos())
    te.setheading(ang)
    #주인공 거북이가 먹이에 닿으면 먹이가 랜덤하게 이동
    if t.distance(tf) < 12:
        x = random.randint(-230,230)
        y = random.randint(-230,230)
        tf.goto(x,y)
    if t.distance(te) < 12:
       t.ontimer(play, 100) #0.1초

#메인영역
t.setup(500,500) #너비,높이
t.title("달려라 거북이")
t.speed(0)
t.up()
t.color('white')
t.bgcolor('black')
t.shape('turtle')

#적 거북이
te = t.Turtle()     #Turtle() 클래스에서 te인스턴스 생성
te.shape('turtle')
te.color('yellow')
te.speed(0)
te.up()
te.goto(0,200)

#먹이
tf = t.Turtle()
tf.shape('circle')
tf.color('blue')
tf.shapesize(0.7)
tf.up()
tf.goto(0,-200)

t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.listen()  #키보드의 동작을 기다림
play()

t.mainloop()