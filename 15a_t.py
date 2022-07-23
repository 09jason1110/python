# 15a_t.py
# 타자 게임 만들기

import random

# 단어 리스트
w=['cat', 'dog', 'fox', 'monkey',
   'mouse', 'panda', 'frog', 'snake', 'wolf']

n=1
q=random.choice(w)
while n<6:
    print(f'*문제 {n}')
    print(q)

    u=input()

    # 정타 시 문제 번호 증가하고 문제 바꾸기
    if q==u:
        n=n+1
        q=random.choice(w)
        print('통과!')
    # 오타시 '오타! 다시도전!' 출력하기
    else:
        print('오타! 다시도전!')
