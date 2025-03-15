# 1463, 1로 만들기
# https://www.acmicpc.net/problem/1463

# if-if를 써야하는데, if-elif를 사용해서 틀림...

N = int(input())
dp = [0] * (N+1)

for i in range(2,N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    
print(dp[N])

