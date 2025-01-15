# 재밌는 나머지 연산
# idea: n-r의 약수를 구하기~

from math import sqrt

n, r = map(int, input().split())
a = n - r

def div(a, r):
    s = set()
    for i in range(1, int(sqrt(a)) + 1):
        if a % i == 0:
            if i > r:
                s.add(i)
            if a//i > r:
                s.add(a // i)
    return(sum(s))

print(div(a,r))