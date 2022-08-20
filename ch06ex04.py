# ch06ex04
#책 장 리스트

bs=['파이썬', 'C', '캐드', '포토샙', 'JAVA', '엑셀']
print(bs)

bs.append('파워포인트')
print(bs)

bs.remove('JAVA')
print(bs)

bs.insert(4, '일러스트')
print(bs)

cnt=len(bs)

print(f'{cnt}')

while True:
    pd=input('도서 이름: ')

    if pd in bs:
        print('대여 가능')
        break
