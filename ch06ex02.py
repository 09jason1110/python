# ch06ex02
# 카트리스트 3

cart=['사과', '멜론', '우유']

cnt=len(cart)

print(f'리스트 원소 개수: {cnt}개')

while True:
    pd=input('확인할 물품: ')

    if pd=='종료':
        break

    if pd in cart:
        print('구매 했습니다')

    else:
        print('구매 전 입니다')
