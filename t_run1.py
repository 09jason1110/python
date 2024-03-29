#t_run1.py
# 거북이 이동하기

import turtle as t
import random

#이동함수 구현
def t_up():
    t.setheading(90)

def t_down():
    t.setheading(270)

def t_left():
    t.setheading(180)

def t_right():
    t.setheading(0)

def t_move():
    t.forward(10)
    #print(f'x: {t.xcor()}')
    d=t.distance(ts)
    #print(f'먹이와의 거리: {d}px')
    if d<20:
        print('hit!')
        ts_x=random.randint(-230, 230)
        ts_y=random.randint(-230, 230)
        ts.speed(0)
        ts.goto(ts_x, ts_y)
        
        
    #1. 화면 오른쪽 가면 왼쪽으로 나오기
    if t.xcor() > 260:
        t.setx(-260)

    #1. 화면 왼쪽 가면 오른쪽으로 나오기
    elif t.xcor() < -260:
        t.setx(260)

    #1. 화면 위쪽 가면 아래쪽으로 나오기
    elif t.ycor() > 260:
        t.sety(-260)

    #1. 화면 아래쪽 가면 위쪽으로 나오기
    elif t.ycor() < -260:
        t.sety(260)

        
    t.ontimer(t_move, 100)

#창 설정
t.setup(500, 500)
t.bgcolor('orange')

#먹이 초기화
ts=t.Turtle()
ts.color('green')
ts.shape('circle')
ts.up()
ts.goto(0, -200)

#거북이 초기화
t.color('white')
t.shape('turtle')
t.speed(0)
t.up()

#거북이 이동
t.onkeypress(t_up, 'Up')
t.onkeypress(t_down, 'Down')
t.onkeypress(t_right, 'Right')
t.onkeypress(t_left, 'Left')
t.listen()

#거북이 이동 실행
t_move()
