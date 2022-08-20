# list_for1
# 리스트 원소 접근

# 리스트 초기화
s=[90, 80, 70, 85, 65]

#리스트 원소 출력
for one in s:
    print(one)

print('-' * 30)   
# 리스트 1원소 출력
print(s[0])
print(s[1])

print('-' * 30)
# 리스트 원소 출력(인덱스)
cnt=len(s)
for idx in range(cnt):
    print(f'{idx}: {s[idx]}')

print('-' * 30)  
# 리스트 인덱스, 원소 출력
for idx, one in enumerate(s):
    print(f'{idx}: {one}')
    
