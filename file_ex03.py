# file_ex03.py
# 학생정보 파일에 기록하기

f=open('file_ex03.txt', 'w')

while True:
    name=input('학생이름: ')
    if name == '종료':
        break

    score=int(input('성적: '))

    msg=f'{name} {score}'
    f.write(msg+'\n')

print()
print('file_ex03.txt 파일을 기록했습니다.')


f.close()
    
