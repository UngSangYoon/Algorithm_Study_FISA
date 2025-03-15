# 1149, RGB거리
# https://www.acmicpc.net/problem/1149

# N번째 집을 칠하는 최소 비용 = (N-1)번째 집을 칠하는 최소 비용 + 남은 색 중 최소 비용
import sys

input = sys.stdin.readline
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for k in range(N)]

# 초기화
dp[0][0] = cost[0][0] # dp[i][0]: R
dp[0][1] = cost[0][1] # dp[i][1]: G
dp[0][2] = cost[0][2] # dp[i][2]: B

for i in range(1, N):
    # dp = 그 전 다른 dp들의 최솟값 + 각 비용 값
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + cost[i][2]

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))