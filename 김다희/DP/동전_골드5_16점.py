# 9084, 동전
# https://www.acmicpc.net/problem/9084

# dp[i]: 금엑 i를 만들 수 있는 경우의 수
# 만약 테스트 갯수가 1개였으면 간단했을텐데...


import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())

    dp = [0]*(M+1)
    dp[0] = 1

    for c in coin:
        for i in range(c, M+1):
            dp[i] = dp[i] + dp[i-c]
    
    print(dp[M])

    


