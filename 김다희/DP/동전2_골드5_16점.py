# 2294, 동전 2
# https://www.acmicpc.net/problem/2294

# dp[i]: i원을 만드는데 필요한 동전 개수의 합의 최솟값
# dp[i] = 1 + min(dp[i-coin1], dp[i-coin2], ...)


import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [1e9]*(k+1)
dp[0] = 0

# 아래 코드로 인해 인덱스 에러 발생
# 예를 들어 k = 100, coin = 500이면 범위 벗어남
# for c in coin:
#     dp[c] = 1

for c in coin:
    for i in range(c, k + 1):
        dp[i] = min(dp[i], 1 + dp[i-c])

if dp[k] >= 1e9:
    print(-1)
else:
    print(dp[k])