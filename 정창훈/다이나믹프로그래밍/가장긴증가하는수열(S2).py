# 입력 받기
N = int(input())  # 수열의 크기
A = list(map(int, input().split()))  # 수열 A

# DP 배열 초기화
dp = [1] * N  # 각 수에서 시작하는 LIS의 길이는 최소 1

# DP 계산
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:  # A[i]가 A[j]보다 크면
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 증가하는 부분 수열의 길이는 dp 배열의 최대값
print(max(dp))
