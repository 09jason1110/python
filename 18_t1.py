# 18_t1.py
# 터틀런

import turtle as t
import random

# 변수 초기화
score=0
playing=False 

def set_turtle(tname, tshape, tcol, tx, ty):
    tname.shape(tshape)
    tname.color(tcol)
    tname.speed(0)
    tname.up()
    tname.goto(tx, ty)

def message(m1, m2):
    t.goto(0, 100)
    t.write(m1, False, 'center', ('D2Coding', 30))
    t.goto(0, -100)
    t.write(m2, False, 'center', ('D2Coding', 30))
    t.home()

def reset_game():
     global score
     score=0
     set_turtle(te, 'turtle', 'red', 0, 200)
     set_turtle(ts, 'circle', 'green', 0, -200)
     set_turtle(t, 'turtle', 'white', 0, 0)
     te.setheading(0)
     ts.setheading(0)
def turn_up():
    t.setheading(90)

def turn_down():
    t.setheading(270)

def turn_left():
    t.setheading(180)

def turn_right():
    t.setheading(0)

def speed_up():
    t.forward(10)
    
def start():
    global playing
    if playing==False:
        playing=True
        t.clear()
        play()

def check_ts():
    global score
    d=t.distance(ts)
    if d<12:
        score=score+1
        ts_x= random.randint(-230, 230)
        ts_y= random.randint(-230, 230)
        ts.goto(ts_x, ts_y)

def move_te():
    global score
    r=random.randint(1, 5)
    if r==2:
        ang=te.towards(t.pos())
        te.setheading(ang)
    te_s=score+5
    if te_s > 12:
        te_s = 12
    te.forward(te_s)

def check_te():
    global playing
    d=t.distance(te)
    if d < 12:
        playing=False
        message('GAME OVER', f'SCORE: {score}')
        reset_game()
def play():
    # 글로벌 변수 설정 
    global score, playing
    t.forward(10)

    # 먹이 충돌
    check_ts()

    # 악당 충돌
    move_te()
    check_te()
   
    if playing:
        t.ontimer(play, 100)# 0.1 초후에 play함수 실행
# 배경
t.setup(500, 500)
t.bgcolor('orange')

# 악당 생성
te=t.Turtle()


# 먹이 생성
ts=t.Turtle()


reset_game()


# 시작 구현
message('Turtle Run', 'SPACE')
# massage(m1, m2) 함수 구현

# 키입력
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_right, 'Right')
t.onkeypress(start, 'space')
t.onkeypress(speed_up, 's')
t.listen() 
