# 113999, ATM
# https://www.acmicpc.net/problem/11399

import sys

input = sys.stdin.readline
n = int(input())
p = sorted(list(map(int, input().split())))
p_sum = 0

for i in range(len(p)+1):
	p_sum = p_sum + sum(p[0:i])

print(p_sum)