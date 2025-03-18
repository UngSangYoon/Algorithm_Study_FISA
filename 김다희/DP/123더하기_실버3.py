# 9095, 1,2,3 더하기
# https://www.acmicpc.net/problem/9095

# 반복되는 연산이 있는지? 1,2,3 관련 반복이 있을듯...
# 어떻게 줄일지? 
# dp(n): n을 1,2,3의 합으로 만들 수 있는 방법의 수
# dp(n) = dp(n-1) + dp(n-2) + dp(n-3)
# 초기값 설정: dp(1) = 1, dp(2) = 2, dp(3) = 4


import sys

input = sys.stdin.readline
T = int(input())
n = [int(input()) for _ in range(T)]

dp = [0] * max(max(n)+1, 4)
dp[1] = 1; dp[2] = 2; dp[3] = 4

for i in range(4, max(n)+1):
    dp[i] = dp[i-1] + dp[i-2]+ dp[i-3]
 
for j in n:
    print(dp[j])


# import sys

# input = sys.stdin.readline
# T = int(input())
# n = [int(input()) for _ in range(T)]

# for i in range(T):
#     K = n[i]
#     dp = [0] * (K+1)
#     dp[1] = 1; dp[2] = 2; dp[3] = 4
#     for j in range(4, K+1):
#         dp[j] = dp[j-1] + dp[j-2]+ dp[j-3]
#     print(dp[K])