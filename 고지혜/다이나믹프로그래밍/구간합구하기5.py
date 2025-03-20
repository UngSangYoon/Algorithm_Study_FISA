'''
< 총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력하기 >
- 첫째 줄: 표의 크기 N과 합을 구해야 하는 횟수 M
- 둘째 줄: N개의 줄에는 표에 채워져 있는 수
- M개 줄: 네 개의 정수 x1, y1, x2, y2 
=> (x1, y1)부터 (x2, y2)의 합을 구해 출력

1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

->
0 0 0 0 0
0 1 3 6 10
0 3 8 15 24
0 6 15 27 42
0 10 24 42 64
8=3+3-1+3=8
15=6+8-3+4=15
24=15+10-6+5=24
..
42=15+24-8+11=42
'''
import sys

N, M = map(int, sys.stdin.readline().split())  # 표의 크기 4, 횟수 3 
num = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def prefix_sum5(N, M, num):
    dp = [[0] * (N+1) for _ in range(N+1)]

    # 누적합
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + num[i-1][j-1]

    # x1, y1, x2, y2 
    result = []
    for _ in range(M):  # M 횟수만큼
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())  
        '''
        (2,2)~(3,4)
        (3,4)(42)-(3,1)(6)-(1,4)(10)+(1,1)(1)(중복)=27
        (1,1)
        -
        1 3 6 10 - (1,4)
        3 8 15 24
        6 15 27 42
        -       -
        (3,1)   (3,4)
        '''
        result.append(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])

    return result


result = prefix_sum5(N, M, num)
for _ in result:
    print(_)