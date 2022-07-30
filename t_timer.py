#t_timer.py
# 터틀런 만들기

import turtle as t

def t_move():
    t.forward(10)
    if t.xcor()>250:
        t.speed(0)
        t.goto(-250, 0)

    t.ontimer(t_move, 100)



#화면 설정
t.setup(500, 500)
t.bgcolor('orange')

#거북이 설정
t.shape('turtle')
t.color('white')
t.up()
t.speed(0)
t.goto(-250, 0)

#거북이 이동                                   
t_move()
