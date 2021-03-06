# 12c_t.py
# 사각형 4개 그리기

import turtle as t

# 사각형 그리는 함수 d_rect()
def d_rect():
    for x in range(4):
        t.forward(100)
        t.left(90)

# tx, ty이동하는 함수 move(tx, ty)
def move(tx, ty):
    t.up()
    t.goto(tx,ty)
    t.down()
#한변의 길이사 50 px 사각형 그리기(-100, -100)
move(-100, -100)
d_rect()

# 한변의 길이가 50px 사각형 그리기(-100, 100)
move(-100, 100)
d_rect()
    
# 한변의 길이가 50px 사각형 그리기(100, 100)
move(100, 100)
d_rect()
    
# 한변의 길이가 50px 사각형 그리기(100, -100)
move(100, -100)
d_rect()


