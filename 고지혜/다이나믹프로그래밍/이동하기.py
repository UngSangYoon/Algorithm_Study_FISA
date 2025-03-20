'''
<준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값>
- (1, 1)에서 시작
- (r, c)에 있으면, 이동 가능한 위치: (r+1, c), (r, c+1), (r+1, c+1)

2차원 배열 필요
[n][m]
i=0 j=0, dp[0][0] = candy[0][0] = 1
    j=1, 1+2 -> dp[0][1] = candy[0][0] + candy[0][1]
    j=2, 1+2+3 -> dp[0][2] = (candy[0][0] + candy[0][1]) + candy[0][2]
                            = dp[0][1] + candy[0][2]
    j=3, 1+2+3+4 -> dp[0][3] = (candy[0][0] + candy[0][1] + candy[0][2]) + candy[0][3]
                            = dp[0][2] + candy[0][3]
i=1 j=0, dp[1][0] = candy[1][0] = 0
    j=1, 0+0 -> dp[1][1] = candy[1][0] + candy[1][1]
    j=2, 0+0+0 -> dp[1][2] = (candy[1][0] + candy[1][1]) + candy[1][2]
                            = dp[1][1] + candy[1][2]
    j=3, 0+0+0+5 -> dp[1][3] = (candy[1][0] + candy[1][1] + candy[1][2]) + candy[1][3]
                            = dp[1][2] + candy[1][3]
i=2 j=0, dp[2][0] = candy[2][0] = 9
    j=1, 9+8 -> dp[2][1] = candy[2][0] + candy[2][1]
    j=2, 9+8+7 -> dp[2][2] = (candy[2][0] + candy[2][1]) + candy[2][2]
                            = dp[2][1] + candy[2][2]
    j=3, 9+8+7+6 -> dp[2][3] = (candy[2][0] + candy[2][1] + candy[2][2]) + candy[2][3]
                            = dp[2][2] + candy[2][3]
'''
import sys

N, M = map(int, sys.stdin.readline().split())  # 세로 3, 가로 4
candy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def move(N, M, candy):
    dp = [[0] * M for _ in range(N)]
    # 시작위치 설정
    dp[0][0] = candy[0][0]  

    for n in range(N):
        for m in range(M):
            if n == 0 and m == 0:
                continue  # 시작 위치 이미 설정 완료
            # 오른쪽 탐색 (r, c+1)
            if m > 0:
                dp[n][m] = max(dp[n][m], dp[n][m-1] + candy[n][m])
            # 아래로 (r+1, c)
            if n > 0:
                dp[n][m] = max(dp[n][m], dp[n-1][m] + candy[n][m])
            # 대각선 (r+1, c+1)
            if n > 0 and m > 0:
                dp[n][m] = max(dp[n][m], dp[n-1][m-1] + candy[n][m])
    return dp[N-1][M-1]

print(move(N, M, candy)) 

# -------------------------------------------------------

import sys

N, M = map(int, sys.stdin.readline().split())  # 세로 3, 가로 4
candy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def move(N, M, candy):
    dp = [[0] * M for _ in range(N)]
    # 시작위치 설정
    dp[0][0] = candy[0][0]  

    for n in range(N):
        for m in range(M):
            if n == 0 and m == 0:  # 시작점 
                dp[n][m] = candy[n][m]
            elif n == 0:  # 첫 번째 행에서는 왼쪽에서만 
                dp[n][m] = dp[n][m-1] + candy[n][m]
            elif m == 0:  # 첫 번째 열에서는 위쪽에서만 
                dp[n][m] = dp[n-1][m] + candy[n][m]
            else:  # 나머지 경우: 왼쪽, 위쪽, 대각선 중 최댓값을 선택 후 그 자리에 있는 사탕 개수와 더하기
                dp[n][m] = max(dp[n-1][m], dp[n][m-1], dp[n-1][m-1]) + candy[n][m]
    return dp[N-1][M-1]

print(move(N, M, candy)) 