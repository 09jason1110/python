# list3
#성적표 만들기

import random

score=[]

for x in range(20):
    s=random.randint(0, 100)
    score.append(s)

#성적표 출력
print(f'score: {score}')

#성적 정렬
score.sort()
print(f'score: {score}')

#성적 내림차순 정렬
score.reverse()
print(f'score: {score}')
