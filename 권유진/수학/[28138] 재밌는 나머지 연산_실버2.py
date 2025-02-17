'''
문제
정수 N을 m으로 나눈 나머지가 R이 되도록 하는 모든 양의 정수 m의 합을 구하라.

입력
첫째 줄에 정수 N과 R이 공백을 사이에 두고 주어진다. 

출력
정수 N을 m으로 나눈 나머지가 R이 되도록 하는 모든 양의 정수 m의 합을 출력한다. 
조건을 만족하는 m이 없으면 0을 출력한다.

예제 입력 1 
16 4
예제 출력 1 
18
조건을 만족하는 m에는 6과 12가 있다.
'''

'''
# 시간 초과 
N, R = map(int, input().split())
csum = 0

for m in range(1, N + 1):
    if N % m == R:
        csum += m

print(csum)
'''

# N = mq + R (0 <= R <m) 

import math

N,R=map(int,input().split())
csum=0
tmp=N-R

for m in range(1,int(math.sqrt(tmp))+1):
    if tmp%m==0 :
        if m > R : csum+=m
        # m의 약수 but m이면 안됨
        if (tmp // m) > R and m != (tmp // m):
                csum += (tmp // m)
print(csum)