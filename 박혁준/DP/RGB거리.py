#1149
# 품

'''
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
'''

N = int(input())
cost = [[0, 0, 0]]
cost += [list(map(int, input().split())) for _ in range(N)]

dp = [[-1, -1, -1] for _ in range(N + 1)]

# 초기값 처리
dp[1][0] = cost[1][0]
dp[1][1] = cost[1][1]
dp[1][2] = cost[1][2]

# DP Table 갱신
for i in range(2, N + 1): # dp[i][0 ~ 2]
	# dp[i][0]
	dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])

	# dp[i][1] 
	dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])

	# dp[i][2] 
	dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])


print(min(dp[N][0], dp[N][1], dp[N][2]))

