#t_timer2.py
# 0.1초마다 이동하는 거북이

import turtle as t
import random


#초기 설정값
#t_speed=random.randint(8, 20)
#ts_speed=random.randint(8, 20)

def d_line(sx, sy, ex, ey):
    t.up()
    t.goto(sx, sy)
    t.down()
    t.goto(ex, ey)

def t_run():
    t_speed=random.randint(1, 20)
    ts_speed=random.randint(1, 20)
    t.forward(t_speed)
    ts.forward(ts_speed)
    if t.xcor()<300 and ts.xcor()<300:
        t.ontimer(t_run, 100)


#배경설정 
t.setup(700, 300)
t.bgcolor('orange')
#트랙 그리기
t.color('white')
t.speed(0)
for ly in range(-100, 101, 100):
    d_line(-350, ly, 350, ly)


#거북이 설정
#white
t.color('white')
t.shape('turtle')
t.speed(0)
t.up()
t.goto(-300, 50)

#red
ts=t.Turtle()
ts.color('red')
ts.shape('turtle')
t.speed(0)
ts.up()
ts.goto(-300, -50)

#이동
t_run()

