# 9461, 피도반 수열
# https://www.acmicpc.net/problem/9461

# dp[i] = dp[i-1] + dp[i-5]
# dp[i]: i번째 정삼각형의 변 길이

import sys

input = sys.stdin.readline
T = int(input())
N = [int(input()) for _ in range(T)]

dp = [0]*(max(N)+1)
dp[1] = 1; dp[2] = 1; dp[3] = 1; dp[4] = 2; dp[5] = 2

for i in range(6, max(N)+1):
    dp[i] = dp[i-1] + dp[i-5]

for j in N:
    print(dp[j])
