# 10b_sum.py
# 1~10 합구하기

a=1
s=0

while a <= 10:
    s=s+a
    print(f'a:{a}, s:{s}')
    #a=a+1
    if s>1000:
        break

print(f'sum: {s}')
