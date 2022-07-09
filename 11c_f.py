#11c_f.py
# 반환값이 있는 함수

# 제곱을 구하는 함수 square(num)
def square(num):
    res=num*num #res=num**2
    return res


# 삼각형 넓이 구하는 함수 tri(b,h)
def tri(b,h):
    a=b*h/2
    return a


#4의 제곱 구하기
r=square(4)
print(r)

r= square(4) + square(5)
print(r)

r2=tri(3,10)
print(r2)
