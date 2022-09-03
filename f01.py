# f01.py
# 문장 기록

f=open('mypitca.txt', 'w')

msg = '파이썬 문장 기록하기' 
f.write(msg + '\n')
f.write('파이썬은 파일 기록도 쉽다.'+'\n')

f.close()
