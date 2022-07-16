# 13b_k.py
#키보드 입력

import turtle as t

t.speed(0)

def t_up():
    t.setheading(90)
    t.forward(20)

def t_left():
    t.setheading(180)
    t.forward(20)

def t_right():
    t.setheading(0)
    t.forward(20)

def t_down():
    t.setheading(270)
    t.forward(20)

def clr_sc():
    t.clear()#화면만 지우기
    # t.reset() 화면을 지우고 원점으로 이동

# u: 펜 들기, d: 펜 내리기
def p_up():
    t.color('orange')
    t.up()

def p_down():
    t.color('black')
    t.down()
# r: red, b:blue, k:black (c_red, c_black, c_black)
def c_red():
    t.color('red')

def c_blue():
    t.color('blue')

def c_black():
    t.color('black')

# 선 굵기
def ps_1():
    t.pensize(1)

def ps_2():
    t.pensize(5)

def ps_3():
    t.pensize(10)

t.shape('turtle')

# t.onkeypress(명령, '~')
t.onkeypress(t_up, 'Up')
t.onkeypress(t_left, 'Left')
t.onkeypress(t_down, 'Down')
t.onkeypress(t_right, 'Right')
t.onkeypress(clr_sc, 'Escape')
t.onkeypress(p_up, 'u')
t.onkeypress(p_down, 'd')
t.onkeypress(c_red, 'r')
t.onkeypress(c_blue, 'b')
t.onkeypress(c_black, 'k')
t.onkeypress(ps_1, '1')
t.onkeypress(ps_2, '2')
t.onkeypress(ps_3, '3')
t.listen()
