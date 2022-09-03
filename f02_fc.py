# f02_fc.py
# 파일 복사

s_file=open('mypitca2.txt', 'r')
d_file=open('mypitca2.txt', 'w')

for one in s_file:
    d_file.write(one)

print('파일 복사 완료')
d_file.close()
s_file.close()
