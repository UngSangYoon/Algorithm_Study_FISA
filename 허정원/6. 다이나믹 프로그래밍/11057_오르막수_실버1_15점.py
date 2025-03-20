'''

'''
N = int(input())

# dp 테이블 0 ~ 9
dp = [[0]*10 for _ in range(N)]

# 초기화
for i in range(10):
    dp[0][i] = 1

# n : 자리수, K 마지막 숫자
for n in range(1, N):    
    for k in range(10):
        for j in range(k+1):
            dp[n][k] += dp[n-1][j]

print(sum(dp[N-1])%10007)
