# list1.py
# 리스트 초기화, 수정, 연산

# 리스트 초기화
lec1=['파이썬', '자바', 'C']
print(f'lec1:{lec1}')

lec2=['워드', '파워포인트', '포도']
print(f'lec2: {lec2}')

#lec2 원소 변경 ('포도'를 '엑셀'로)
lec2[2]='엑셀'
print(f'lec2: {lec2}')

#lec3 = lec1+lec2로 초기화
lec3= lec1+lec2
print(f'lec3: {lec3}')

# '자바'만 lec1 에서 출력
print(f'lec1[1]: {lec1[1]}')

#'엑셀'만 lec3에서 출력
print(f'lec3[5]: {lec3[5]}')

# 마지막 원소 선택
#1. len(lec3)
cnt=len(lec3)
print(f'lec3 원소 수: {cnt}개')
print(f'lec3 마지막 원소: {lec3[cnt - 1]}')

# 2. 뒤에서 인덱스 하기 (-)
print(f'lec3 마지막 원소: {lec3[-1]}')
print(f'lec3 마지막 두번째 원소: {lec3[-2]}')
