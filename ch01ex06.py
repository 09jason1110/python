# ch01ex06.py
# 커피 판매 이익 구하기

print('일일 판매량을 입력하세요.')
an=int(input('아메리카노 판매수: '))
cn=int(input('카페라떼 판매수: '))
pn=int(input('카푸치노 판매수: '))

s=an*2000+cn*3000+pn*3500
print()
print(f'일일 판매 매출액은 {s} 입니다.')
a=s*30
print(f'한 달 30일 기준 예상 매출액은 {a} 입니다.')
print()

p=int(input('예상 지출액을 입력하세요: '))

n_p=a-p
print(f'한 달 예상 순이익은 {n_p} 입니다.')
