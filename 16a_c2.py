# 16a_c2.py
# 타겟 그리기

import turtle as t
import random

# 변수 초기화
l=10
# 바닥 그리기
t.goto(300, 0)
t.goto(-300, 0)

#타겟그리기
tx=random.randint(50, 150)

t.color('green')
t.pensize(5)
t.up()
t.goto(tx - l/2, 3)
t.down()
t.goto(tx + l/2, 3)
print(f'타겟 좌표: {tx}, 길이: {l}px')
      
# 대포 초기화
t.up()
t.color('black')
t.goto(-200, 10)
t.setheading(20)
