# 11053, 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

# 1. 입력 처리
# 2. DP 배열 초기화
# 3. 이중 반복문으로 LIS 계산
#   - i는 현재 원소 위치
#   - j는 i보다 앞에 있는 모든 원소들
#   - A[j] < A[i]이면, DP[i] = max(DP[i], DP[j]+1)


import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))


