# ch18p1.py
# 지역 변수

def f():
    # 지역 변수
    a=5
    print(f'지역변수 a: {a}')

# 전역 변수
a=1
f()
print(f' 전역변수 a: {a}')
