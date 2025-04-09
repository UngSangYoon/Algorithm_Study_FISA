N, M = map(int, input().split())

# input
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 접근법 1. 브루트포스
# 앱 N 개에 대해서 모든 조합 -> 2^N 개의 조합
# 각 조합에 대해서 비용과 메모리 합 계산 -> O (2^N * N)


# 접근법 2. 다이나믹 프로그래밍
# 메모리 합을 기준으로 최적화
# dp[i][j] : i번째 앱까지 고려했을 때, j 메모리를 확보할 수 있는 최소 비용
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if memory[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - memory[i]] + cost[i])

print(dp[N][M])


