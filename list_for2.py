# list_for2
#성적 처리

score=[98, 78, 88, 67, 75]

s=0#합계
a=0#평균
c=0#명수
for one in score:
    s=s+one
    c=c+1

a=s/c

print(f'성적: {score}')
print(f'총점: {s}점')
print(f'명수: {c}점')
print(f'평균: {a}점')
