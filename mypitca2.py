# mypitca2.py
# 여러 문장 기록하기

f=open('mypitca2.txt','w')

while True:
    msg = input('기록내용을 입력하세요: ')
    if msg == '':
        break

    print(msg)
    f.write(msg+'\n')

f.close()
