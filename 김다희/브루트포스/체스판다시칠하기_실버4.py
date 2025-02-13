# 체스판 다시 칠하기

# idea: 체크판의 성질을 생각해보기~
# 흰 색으로 시작하는 체크판일 경우, 행 번호와 열 번호 합이 짝수면 흰 색임
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
min_cnt = 100

# 4중 for문 
# a, i: 몇 행?, b, j: 몇 열?
# 총 (n-7)*(m-7)개의 체크판 경우의 수가 발생~~
for a in range(n-7): 
    for b in range(m-7):
        w_cnt = 0 # w로 시작하는 경우, 다시 칠해야 하는 횟수
        b_cnt = 0 # b로 시작하는 경우, 다시 칠해야 하는 횟수
        for i in range(a, a+8):
            for j in range(b, b+8):
                now_color = board[i][j]
                if (i+j)%2 == 0:
                    w_color = 'W'
                    b_color = 'B'
                else:
                    w_color = 'B'
                    b_color = 'W'
                
                if now_color != w_color:
                    w_cnt = w_cnt + 1
                if now_color != b_color:
                    b_cnt = b_cnt + 1
        min_cnt = min(min_cnt, w_cnt, b_cnt) # 3개 비교 후 최솟값 반환

print(min_cnt)