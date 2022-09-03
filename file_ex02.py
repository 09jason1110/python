# file_ex02.py
# 문장을 파일로 기록하기

f=open('file_ex02.txt', 'w')

msg='life is short'
print(msg)
f.write(msg+'\n')


msg='you need python'
print(msg)
f.write(msg+'\n')

f.close()

