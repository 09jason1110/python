# 15a_t3.py
# 문제 출제 방법 2

import random

# 단어 리스트
w=['cat', 'dog', 'fox', 'monkey',
   'mouse', 'panda', 'frog', 'snake', 'wolf']

# 단어 리스트 원소 순서 변경
random.shuffle(w)

# 문제 번호로 출력하기
n=1
while n<6:
    print(f'문제 {n}')
    print(w[n])

    n=n+1
