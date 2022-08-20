# list_for_ex02
#학생 성적표 총점, 평균 구하기

grades=[80, 95, 77, 82, 99]

s=0
a=0
c=0

for idx, one in enumerate(grades):
    s=s+one
    c=c+1
    num=idx+1
    print(f'{num}번 {one}')

a=s/c

print()
print(f'학급 총점은 {s}점이고, 평균은 {a}이다')
