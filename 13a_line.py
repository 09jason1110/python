# 13a_line.py
# 반복 도형 그리기

import turtle as t

t.bgcolor('black')
t.speed(0)

for x in range(300):
    if x % 3 == 0:
        col ='red'
    elif x % 3 == 1:
        col='yellow'
    else:
        col='blue'

    t.color(col)

    t.forward(x * 2)
    t.left(119)
