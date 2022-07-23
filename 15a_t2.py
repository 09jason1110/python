# 15a_t2.py
# 타자게임 만들기

import random
import time

# 단어 리스트
w=['cat', 'dog', 'fox', 'monkey',
   'mouse', 'panda', 'frog', 'snake', 'wolf']


#게임 시작 안내
input('[타자게임] 준비되면 enter!')
start=time.time()#시작 시간 측정 

# 문제 초기화
n=1
q=random.choice(w)
#게임 루프
while n<6:
    #문제출제
    print(f'문제 {n}')
    print(q)

    # 사용자 입력(변수: u)
    u=input()

    #정타, 오타 확인
    if q==u:
        n=n+1
        q=random.choice(w)
    #정타시 '통과!', 오타시 '오타! 다시도전!'
        print('통과!')

    else:
        print('오타! 다시도전!')

# 타자 모두 입력시 종료 시간 측정
end=time.time()
et=end-start
print(f'타자시간: {et:.1f}초')
