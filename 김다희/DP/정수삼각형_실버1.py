# 1932, 정수 삼각형
# https://www.acmicpc.net/problem/1932

# 반복되는 구간? 
# i행 j열을 선택한 경우 최댓값 = i-1행 j열까지의 최댓값 + i행 j열 점수

# score: 하삼각행렬
# 7   0   0   0   0
# 3   8   0   0   0
# 8   1   0   0   0
# 2   7   4   4   0
# 4   5   2   6   5

# dp: 초기값 설정
# 7   0   0   0   0
# 10  15  0   0   0
# 0   0   0   0   0
# 0   0   0   0   0
# 0   0   0   0   0

# 각 케이스 별로 나누는 것이 생각보다 까다로웠다... 

import sys

input = sys.stdin.readline
n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(score[0][0])
    sys.exit()

if n >= 2:
    dp = [[0]*(k+1) for k in range(n)]
    dp[0][0] = score[0][0]
    dp[1][0] = score[0][0] + score[1][0]; dp[1][1] = score[0][0] + score[1][1]

    for i in range(2, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + score[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + score[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + score[i][j]

    print(max(dp[n-1]))