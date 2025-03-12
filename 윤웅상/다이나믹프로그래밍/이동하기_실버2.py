import sys
sys.setrecursionlimit(100000000)
# top-down 방식 구현
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]

# 초기값 설정
dp[0][0] = arr[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + arr[0][i]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + arr[i][0]

def recur(r,c):
    if dp[r][c] != -1:
        return dp[r][c]
    
    else:
        dp[r][c] = max(recur(r-1,c), recur(r, c-1), recur(r-1, c-1)) + arr[r][c]
        return dp[r][c]
    
print(recur(N-1,M-1))
