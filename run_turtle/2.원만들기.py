#여러개의 원 만들기
import turtle as t

t.speed(0)
t.color('green')
t.bgcolor('black')
t.pensize(2)
n =100
for x in range(n):
    t.circle(200)
    t.left(360/n)


