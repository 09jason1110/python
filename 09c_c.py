# 09c_c.py
# 덧셈 문제 맞히기

import random
import time

s1=0
s2=0

start=time.time()
for a in range(10):
    n1=random.randint(1,10)
    n2=random.randint(1,10)

    usr=int(input(f'{a+1}번: {n1}+{n2}='))
    if usr == n1+n2:
        print('정답')
        s1=s1+1
    else:
        print('오답')
        s2=s2+1
end=time.time()
et=end-start

print('-'*30)
print(f'정답: {s1}개')
print(f'오답: {s2}개')
print(f'걸린시간: {et}초')
# 모두 정답이면 '당신은 덧셈의 신!'출력하기
if s2==0 and et < 30:
    print('당신은 덧셈의 신!')
