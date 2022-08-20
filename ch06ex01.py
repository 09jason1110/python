#ch06ex01.py
#카트리스트

cart=[]
cart.append('사과')
cart.append('수박')
print(f'{cart}리스트에 원소 추가하기')

pack=list()
pack.append('홈런볼')
pack.append('우유')
print(f'{pack}')

cart=cart+pack
print(f'{cart}리스트 결합하기')

cart[1]='멜론'
print(f'{cart}리스트 원소 교체하기')

del cart[2]
print (cart)

cart.insert(2, '요거트')
print (cart)

cart.remove('요거트')
print(f'{cart}리스트 원소 추가 후 제거')
