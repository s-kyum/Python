import random
import turtle as t
from turtle import Turtle

def turn_right(): #오른쪽 화살키
    t.setheading(0)


def turn_up(): #위쪽 화살키
    t.setheading(90)


def turn_left(): #왼쪽 화살키
    t.setheading(180)


def turn_down(): #아래쪽 화살키
    t.setheading(270)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1, False, "center", ("",20))
    t.goto(0,-100)
    t.write(m2, False, "center", ("",15))
    t.home()
def play():
    global score
    global playing
    t.forward(15)

    #적 거북이의 속도는 점수가 올라가면 1씩 증가
    if random.randint(1,5)==3: #3을 뽑을 확률이 20%
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = score + 5
    if speed > 15:
        speed = 15
    te.forward(speed)

    #주인공이 먹이를 먹으면 점수가 1올라감
    if t.distance(tf) < 12:
        score +=1
        t.write(score)
        x=random.randint(-230,230)
        y=random.randint(-230,230)
        tf.goto(x,y)

    #주인공이 적에게 잡히면 게임종료
    if t.distance(te) < 12:
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score=0
    if playing:
        t.ontimer(play,100)

#메인영역
#점수 변수와 플레이 스위치(bool)선언
score=0
playing = False

t.setup(500,500) #너비 높이
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
t.onkeypress(start,"space")
t.listen()  #키보드의 동작을 기다림
message("Turtle Run", "[Space]")




t.mainloop()