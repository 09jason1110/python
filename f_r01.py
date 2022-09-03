# f_r01.py
# 파일 불러오기

f=open('mypitca2.txt', 'r')

for one in f:
    print(one, end='')


f.close()
