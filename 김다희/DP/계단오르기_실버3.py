# 2579, 계단 오르기
# https://www.acmicpc.net/problem/2579

# 반복되는 구간이 있을까?
# dp(i) = max(1, 2)
# 1: dp(i-3) + score(i-1) + score(i-2)
# 2: dp(i-2) + score(i-1)

import sys

input = sys.stdin.readline
N = int(input())
score = [int(input()) for _ in range(N)]
dp = [0] * max(4, N+1)

if N == 1:
    print(score[0])
elif N == 2:
    print(score[0] + score[1])
else:
    dp[1] = score[0]
    dp[2] = score[0] + score[1]
    dp[3] = max(score[0] + score[2], score[1] + score[2])

    for i in range(4, N+1):
        dp[i] = max(dp[i-2] + score[i-1], dp[i-3] + score[i-2] + score[i-1])
    
    print(dp[N])




# 런타임에러, N=1,2 고려 안 함
# import sys

# input = sys.stdin.readline
# N = int(input())
# score = [int(input()) for _ in range(N)]
# dp = [0] * max(4, N+1)
# dp[1] = score[0]; dp[2] = score[0]+score[1]
# dp[3] = max(score[0] + score[2], score[1] + score[2])

# for i in range(4, N+1):
#     dp[i] = max((dp[i-3]+score[i-1]+score[i-2], dp[i-2]+score[i-1]))

# print(dp[N])