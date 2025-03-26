# 14501, 퇴사
# https://www.acmicpc.net/problem/14501

# N일 동안 최대한 많은 상담
# T: 상담을 완료하는데 걸리는 기간
# P: 상담을 했을 때 받을 수 있는 금액
# dp[i]: i일까지 받을 수 있는 최대 금액

 
import sys

input = sys.stdin.readline
N  = int(input())
tp = [list(map(int, input().split())) for _ in range(N)]

dp = [0]*(N+1)

for i in range(N):
    t, p = tp[i]
    if i+t <= N:
        dp[i+t] = max(dp[i] + p, dp[i+t])
    dp[i+1] = max(dp[i], dp[i+1])


print(dp[N])