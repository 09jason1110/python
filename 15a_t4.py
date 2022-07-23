# 15a_t4.py
# 타자 게임 만들기

import random
import time

# 단어 리스트
w=['고양이', '강아지', '여우', '원숭이',
   '쥐', '판다', '개구리', '뱀', '늑대']

# 단어 원소 재배치
random.shuffle(w)

# 문제번호 초기화
n=1

print('게임을 시작하려면 enter!')
input()

start=time.time()

while n<6:
    print(f'문제 {n}')
    print(w[n])
    u=input()

    if u==w[n]:
        print('통과!')
        n=n+1

    else:
        print('오타! 다시입력!')

end=time.time()
et=end-start

print(f'타자시간: {et:.1f}초')
