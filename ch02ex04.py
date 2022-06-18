# ch02ex04.py
# 학점 계산기

s=int(input('점수를 입력하세요: '))

if s>=90:
    g='A'

elif s>=80:
    g='B'

elif s>=70:
    g='C'

elif s>=60:
    g='D'

else:
    g='F'

print(f"당신의 학점은 '{g}' 입니다.")
