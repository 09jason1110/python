# 09a_w.py
# 마음대로 걷는 거북이

import turtle as t
import random

t.shape('turtle')
t.speed(0)

for a in range(500):
    ang=random.randint(1,360)
    t.setheading(ang)
    d=random.randint(1,20)
    t.forward(d)
