# 문제: 다이나믹 프로그래밍 > 2×N 타일링 (S3)
# 주소: https://www.acmicpc.net/problem/11726
n = int(input("직사각형의 너비 n을 입력하세요: "))

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = 1

if n >= 2:
    dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print("2×" + str(n) + " 크기의 직사각형을 채우는 방법의 수:", dp[n])
