# 12b_f.py
# 1~n 곱 구하는 함수 fact(n)

def fact(n):
    f=1
    for i in range(1, n+1):
        f=f*i
    return f

# 1~4곱 구하기 (1*2*3*4=24)
print(fact(4))

# 1~10곱 구하기
print(fact(10))
