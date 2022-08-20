# list_for_ex01
# 학생 성적표 출력

grades=[80, 95, 77, 82, 99]
# 3
for idx, one in enumerate(grades):
    num=idx + 1
    print(f'{num}번 {one}')

print('-' * 6)
# 2
cnt=len(grades)
for idx in range(cnt):
    num = idx+1
    print(f'{num}번 {grades[idx]}')
