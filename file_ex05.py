# file_ex05.py
# 문장 추가하기

f=open('file_ex01.txt', 'a')# a: 추가(advertisement)

msg = '파이썬은 파일에 추가하기도 쉽다. '
f.write(msg + '\n')

f.close()
