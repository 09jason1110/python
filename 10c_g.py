# 10c_g.py
# 숫자 추측해 맞히기

import random

c=0
n=random.randint(1,100)
# print(f'정답: {n}')
while True:
    u=int(input('맞혀 보세요'))
    c=c+1

    if abs(u-n)>= 20:
        msg='*2'
    else:
        msg=''

    if u==n:
        print('정답!')
        break
    elif u<n:
        print(f'up{msg}')
    else:
        print(f'down{msg}')

print(f'시도횟수:{c}번')
