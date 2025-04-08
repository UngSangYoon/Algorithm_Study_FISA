# 1018, 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

# M*N 사이즈 보드
# 각 정사각형은 랜덤으로 흰, 검
# 보드의 일부분 잘라서 8*8 크기의 체스판 만들기
# (1) 맨 왼쪽 위 칸이 흰색
# (2) 맨 왼쪽 위 칸이 검은색 >> 계산할 필요 없음 ((2) = 64 - (1)이니까...)
# 다시 칠하는 칸을 최소화하자

# 전체 판 체크 횟수: (M-8)*(N-8) <- 최대 42*42=1600
# 판 내에서 비교 횟수: 7*8=56
# 총 약 75000번 연산 -> 전체 비교 가능


import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

# (1) 케이스의 판 만들기
w_board = [list("WBWBWBWB"),list("BWBWBWBW")]*4

# 다시 칠하는 갯수 세는 함수 정의
def cnt_board(board):
    min_cnt = 1000
    # 판에서 시작 지점 (a,b)
    for a in range(N-7): # 행
        for b in range(M-7): # 열

            w_cnt = 0
            for c in range(a, a+8): # a~a+7까지 순회
                for d in range(b, b+8): # b~b+7까지 순회
                    # 만약 입력 받은 판과 (1) 케이스 판과 다르면, w_cnt 증가
                    if board[c][d] != w_board[c-a][d-b]:
                        w_cnt = w_cnt + 1
            min_cnt = min(min_cnt, w_cnt, 64-w_cnt)
    return min_cnt

print(cnt_board(board))

