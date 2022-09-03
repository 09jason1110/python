# file_ex06.py
# 파일 불러오기

f=open('file_ex01.txt', 'r')

for one in f:
    print(one, end='')

f.close()
