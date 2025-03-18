import sys
sys.setrecursionlimit(int(1e6))

INF = int(1e12)

def func(n, k): # dp[n][k]를 반환
	global cost, dp

	# base case
	if dp[n][k] != -1:
		return dp[n][k]

	# recursive case
	best = INF
	for i in range(3):
		if i != k:
			best = min(best, func(n - 1, i))

	dp[n][k] = best + cost[n][k]
	return dp[n][k]


N = int(input())
cost = [[0, 0, 0]]
cost += [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0]] + [[-1, -1, -1] for _ in range(N)]

print(min(func(N, 0), func(N, 1), func(N, 2)))
