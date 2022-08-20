# ch06ex03
# 강좌 리스트

lec=['python', 'c']
print(lec)

lec.append('office')
lec.append('cad')
lec.append('game')
print(lec)

lec.remove('game')
print(lec)

cnt=len(lec)
print(f'{cnt}')

if 'python' in lec:
    print ('파이썬 포함')
