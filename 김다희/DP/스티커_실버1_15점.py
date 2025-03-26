# 9465, 스티커
# https://www.acmicpc.net/problem/9465

# 반복되는 계산이 있는지? 
# dp[0][k]: 0행 k열 스티커를 선택했을 때 최대 점수의 합
# dp[1][k]: 1행 k열 스티커를 선택했을 때 최대 점수의 합
# 초기값 세팅?
# dp[0][0] = score[0][0]; dp[0][1] = dp[1][0] + score[0][1]
# dp[1][0] = score[1][0]; dp[1][1] = dp[0][0] + score[1][1]

# score
# 50 10 100 20 40
# 30 50 70 10 60

# dp
# 50 40 200 140 250
# 30 100 120 210 260

import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(2)]
    
    if n == 1:
        print(max(score[0][0], score[1][0]))
        continue

    elif n > 1:
        dp = [[0]*n for _ in range(2)]
        dp[0][0] = score[0][0]; dp[1][0] = score[1][0]
        dp[0][1] = score[1][0] + score[0][1]; dp[1][1] = score[0][0] + score[1][1]

        for j in range(2, n):
            dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + score[0][j]
            dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + score[1][j]

        print(max(dp[0][n-1], dp[1][n-1]))


