N, K = map(int, input().split())

W = [0]
V = [0]

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# dp 디자인 n번 물건까지 넣을 수 있고 무게의 합이 k이하일 때의 최대 가치
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]


for n in range(1, N + 1):
    for k in range(1, K + 1): 
        # dp[n - 1][k] : 무게의 합이 k d이하일 때 n-1번까지 고려
        dp[n][k] = dp[n - 1][k]
        if k - W[n] >= 0:
            # dp[n - 1][k - W[n]] : n번 물건을 담기 전 최대 가치
            dp[n][k] = max(dp[n][k], dp[n - 1][k - W[n]] + V[n])

print(dp[N][K])
