# 1912, 연속합
# https://www.acmicpc.net/problem/1912

import sys

input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))

dp = [0]*(n+1)
dp[0]= s[0]
max_sum = s[0]

for i in range(1, n):
    dp[i] = max(s[i], dp[i-1]+s[i])
    max_sum = max(max_sum, dp[i])

print(max_sum)