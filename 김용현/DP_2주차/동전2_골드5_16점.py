# 입력 받기
n, k = map(int, input().split())  # 동전 개수, 목표 금액
coins = [int(input()) for _ in range(n)]  # 동전 리스트

# DP 테이블 초기화
dp = [float('inf')] * (k + 1)  # dp[i] -> i원을 만들기 위한 최소 동전 개수 저장
dp[0] = 0  # 0원을 만드는 방법은 0개 (아무 동전도 사용하지 않음)

# 동전별로 DP 갱신
for coin in coins:
    for j in range(coin, k + 1):
        dp[j] = min(dp[j], dp[j - coin] + 1)  # 최소 동전 개수 갱신

# 결과 출력 (만들 수 없는 경우 -1 출력)
print(dp[k] if dp[k] != float('inf') else -1)