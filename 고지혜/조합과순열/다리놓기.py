import sys
import math
# nCr
def bridge(n, m):
    if n <= m:  # n <= m
        return math.comb(m, n)
    else:
        return 0


input_ = sys.stdin.readlines()
t = int(input_[0].strip())  # 테스트 케이스 개수

for i in range(1, t+1):  # 3
   n, m =  map(int, input_[i].split())  # 1 2 3
   print(bridge(n, m))