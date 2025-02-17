from itertools import combinations
import sys

input = sys.stdin.readline
n, s = map(int, input().split())
seqen = list(map(int, input().split()))
k = []; cnt = 0

for i in range(1, n+1):
    for j in combinations(seqen, i):
        if sum(j) == s:
            cnt = cnt + 1

print(cnt)