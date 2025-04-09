# 11726, 2×n 타일링
# https://www.acmicpc.net/problem/11726

# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수
# dp에서 많이 본 유형
# dp[n] = dp[n-1] + dp[n-2]

n = int(input())

dp = [0]*max(3, (n+1))
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(int(dp[n]%10007))


