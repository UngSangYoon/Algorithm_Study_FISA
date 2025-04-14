# 접근법 1. 브루트포스
# 앱 N 개에 대해서 모든 조합 -> 2^N 개의 조합
# 각 조합에 대해서 비용과 메모리 합 계산 -> O (2^N * N)


# 접근법 2. 다이나믹 프로그래밍
# 메모리 합을 기준으로 최적화
# dp[n][c] : n번째 앱까지 고려했을 때, c비용으로 얻을 수 있는 최대 메모리
N, M = map(int, input().split())
INF = int(1e12)
MAX = 10001

# input
mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

# solve
dp = [[0] * (MAX) for _ in range(N + 1)]

# 메모리 합을 기준으로 최적화
for n in range(1, N + 1):
	for c in range(0, MAX):
		dp[n][c] = dp[n - 1][c]
		if c - costs[n] >= 0:
			dp[n][c] = max(dp[n][c], dp[n - 1][c - costs[n]] + mems[n])
			
# 최소 비용 찾기
ans = INF
for c in range(0, MAX):
	if dp[N][c] >= M:
		ans = min(ans, c)

print(ans)
