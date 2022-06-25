# ch04ex01.py
# 평군 계산기


s=0
avg=0
c=0
while True:
    score=int(input('점수를 입력하세요:'))
    if score<0:
        break
    c=c+1
    s=s+score
    
avg=s/c
print()
print(f'입력한 점수의 평균은 {avg:.1f}점 입니다.')
