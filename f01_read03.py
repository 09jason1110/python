# f01_read03.py
# 파일 불러오기

f=open('mypitca2.txt', 'r')

msg=f.readlines()
print(msg)

print('-' * 30)

for one in msg:
    print(one, end='')
f.close()
