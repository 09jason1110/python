# 16a_cannon.py
# 대포게임 만들기

import turtle as t
import random


l=50


def draw_line(sx, sy, ex, ey, col='black', ps=1):
    t.pensize(ps)
    t.color(col)
    t.up()
    t.goto(sx, sy)
    t.down()
    t.goto(ex, ey)

def reset_cannon(ang=20):
    t.up()
    t.color('black')
    t.goto(-200, 10)
    t.setheading(ang)

def turn_up():
    if t.heading()<90:
        t.left(2)

def turn_down():
    t.right(2)
def prn_msg(txt, col='blue'):
    t.color(col)
    my=random.randint(10, 150)
    t.sety(my)
    t.write(txt, False, 'center', ('D2cording', 15))

def fire():
    ang=t.heading()
    # 바닥에 닿을때까지 이동
    while t.ycor()>0:
        t.forward(15)
        t.right(5)


        
    # 바닥에 닿으면 충돌 확인
    d=t.distance(tx, 0)
    if d<= l/2:
        prn_msg('Good!')
    else:
        prn_msg('Bad!', 'red')
        reset_cannon(ang)

# 바닥 그리기
draw_line(-300, 0, 300, 0)

# 타겟 그리기
tx=random.randint(50, 150)
draw_line(tx-l/2, 3, tx+l/2, 3, 'green', 5)

# 대포 초기화
reset_cannon()

# 키입력
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(fire, 'space')
t.listen()
