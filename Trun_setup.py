#Trun_setup.py
#터틀런 만들기

import turtle as t

#배경 
t.setup(500, 500)
t.bgcolor('orange')

#te
te=t.Turtle()
te.up()
te.shape('turtle')
te.color('red')
te.speed(0)
te.goto(0, 200)

#ts
ts=t.Turtle()
ts.up()
ts.shape('circle')
ts.color('green')
ts.speed(0)
ts.goto(0, -200)

#t
t.up()
t.shape('turtle')
t.color('white')
t.speed(0)
t.goto(0, 0)
