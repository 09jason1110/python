# 15b_1.py
# 태극 모양 그리기

import turtle as t

t.bgcolor('black')
t.speed(0)

col=['red', 'yellow', 'blue']
for x in range(500):
    t.color(col[x%3])
    

    t.forward(x)
    t.left(119)
