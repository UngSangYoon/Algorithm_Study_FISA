# 3085, 사탕 게임
# https://www.acmicpc.net/problem/3085

# 문제 요약
# N×N 보드에 색이 다른 사탕들이 놓여 있음
# 인접한 두 사탕을 한 번만 바꿔서, 같은 색이 연속된 가장 긴 행 또는 열의 길이를 구하기
# 그때 먹을 수 있는 최대 사탕 개수를 출력하는 문제

# 어떤 알고리즘?
# 완전 탐색 
# 상하, 좌우 교환: O(N²), 개수 세기: O(N²), O(N²)*O(N²)=O(N⁴)
# N ≤ 50 -> O(50⁴) 1초 내에 연산 가능

# 흐름
# 1. N×N 보드를 입력받기
# 2. 함수 cnt_max_candies(board):
#    - 각 행과 열을 확인하여 같은 색 사탕이 연속된 최대 길이를 반환
# 3. 보드의 모든 칸에서:
#    - 오른쪽 또는 아래쪽 사탕과 교환
#    - 교환 후 최대 연속 사탕 개수 갱신
#    - 원래 상태로 복구

# 4. 최댓값 출력



# 풀이 코드
import sys

# 1. N×N 보드를 입력받기
input = sys.stdin.readline
N = int(input())
board = [list(input().strip()) for _ in range(N)]
max_candies = 0

# 2. 함수 cnt_max_candies(board)
# 최대 사탕 개수 세는 함수
def cnt_max_candies(color):
    max_cnt = 1 

    for i in range(N):
        # 좌우 일치
        cnt = 1
        for j in range(1,N): # j: 열 번호
            if color[i][j] == color[i][j-1]:
                cnt = cnt + 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
        # 상하 일치
        cnt = 1
        for j in range(1,N): # j: 행 번호
            if color[j][i] == color[j-1][i]:
                cnt = cnt + 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1

    return max_cnt

# 3. 교환하며, 최대 개수 세기
for i in range(N):
    # 좌우 교환
    for j in range(N): # j: 열 번호
        if j+1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 교환
            max_candies = max(max_candies, cnt_max_candies(board)) 
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 복구
        
    # 상하 교환
    for j in range(N): # j: 행 번호
        if j+1 < N:
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i] # 교환
            max_candies = max(max_candies, cnt_max_candies(board)) 
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i] # 복구

print(max_candies)