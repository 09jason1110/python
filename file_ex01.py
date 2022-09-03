#file_ex01.py
# 문장을 파일로 기록

f=open('file_ex01.txt', 'w')

msg='파이썬 파일 기록은 쉽다.'
f.write(msg + '\n')

f.close()
