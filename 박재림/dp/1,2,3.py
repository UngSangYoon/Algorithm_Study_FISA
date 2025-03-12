import sys
input = sys.stdin.readline

T = int(input().strip())  # 테스트 케이스 개수

# n의 최대값이 10이므로, dp 테이블을 11까지 준비
dp = [0] * 11

# 초기값 설정
dp[0] = 1  # 편의상 '0을 만드는 방법'을 1가지로 설정(아무것도 사용하지 않는 경우)
dp[1] = 1  # (1)
dp[2] = 2  # (1+1, 2)
dp[3] = 4  # (1+1+1, 1+2, 2+1, 3)

# n이 4 이상일 때부터 점화식 적용
for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

# 테스트 케이스 처리
for _ in range(T):
    n = int(input().strip())
    print(dp[n])
