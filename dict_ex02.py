# dict_ex02.py
# 단어 번역 하기

dic={'apple': '사과', 'banana': '바나나',
     'watermelon':'수박', 'grape': '포도'}

while True:
    w=input('번역할 단어는: ')
    if w == '':
        break
    ws=dic.keys()
    if w in ws:
        print(dic[w])
    else:
        print('단어가 없습니다')

