# f_ld.py
# 리스트, 사전

cart=['사과', '배', '포도']
num=[5, 6, 3]
#1
for idx, one in enumerate(cart):
    print(one, num[idx])

print('-'*30)
#2
c_dic={'사과': 5, '배': 6, '포도': 3}

for k, v in c_dic.items():
    print(k, v)

print('-'*30)
#3
cn=[ ['사과', 5], ['배', 6], ['포도', 3] ]
for one in cn:
    print(one[0], one[1])

print('-'*30)
#4
for k, v in cn:
    print(k, v)

f=open('cart_deta.txt', 'w')
for k, v in cn:
    msg=f'{k}는 {v}개 있습니다.'
    f.write(msg+'\n')

f.close()
