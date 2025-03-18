# 10844, 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

# dp[i][j]: N = i & 끝자리가 j인 계단 수의 합
# dp를 어떻게 적용할지만 떠올리면, 그 이후는 생각보다 쉬운 문제제

N = int(input())
dp = [[0]*10 for _ in range(N+1)]
dp[1][0] = 0
for k in range(1, 10):
    dp[1][k] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(int(sum(dp[N])%1000000000))