# list2
# 리스트 초기화, 제거, 추가

#빈 리스트 만들기
bag1=[]
bag2=list()
print(f'bag1: {bag1}')
print(f'bag2: {bag2}')

# bag1에 '휴대폰', '필통' 추가
bag1.append('휴대폰')
bag1.append('필통')
print(f'bag1: {bag1}')

# bag2에 '사과', '텀블러', '사탕'추가
bag2.append('사과')
bag2.append('텀블러')
bag2.append('사탕')
print(f'bag2: {bag2}')

# bag3에 bag1과 bag2 합치기
bag3=bag1+bag2
print(f'bag3: {bag3}')

#bag3에서 '사탕'을 '핸드크림'으로 바꾸기
bag3[-1]='핸드크림'
print(f'bag3: {bag3}')

#bag3에서 '텀블러'앞에 '물티슈 넣기
bag3.insert(3, '물티슈')
print(f'bag3: {bag3}')

#bag3에서 '사과 제거
del bag3[2]
print(f'bag3: {bag3}')

# bag3에서 '텀블러' 제거
bag3.remove('텀블러')
print(f'bag3: {bag3}')
