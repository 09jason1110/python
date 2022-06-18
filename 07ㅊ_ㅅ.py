# 07c_t.py
# 타임 맞추기

import time

input('준비되면 엔터를 누르세요')

s=time.time()

input('20초를 센후 엔터를 누르세요.')
e=time.time()

et=int(e-s)
t=abs(20-et)
print(f'실제시간: {et} 초')
print(f'20초와의 차이: {t} 초')
