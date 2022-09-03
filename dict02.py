# dict02
# 딕셔너리

st={1000: '홍길동', 1001:'김철수', 2000:'김영희', 2001:'홍길자'}

print(st)
print(st.keys())# 키출력
print(st.values())# 값 출력
print(st.items())#둘다 출력

print('-'*50)
# 학번, 이름 출력

for one in st.keys():
    print(f'학번: {one}')
    name=st[one]
    print(f'이름: {name}')

print('-'*50)
for snum, name in st.items():
    print(f'학번: {snum}, 이름: {name}')

print('-'*50)
sn=st.keys()
num=int(input('조회할 학생 번호: '))
if num in sn:
    print(f'학번: {num}, 이름: {st[num]}')
else:
    print('학생이 없습니다')
