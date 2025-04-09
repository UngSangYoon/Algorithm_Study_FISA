'''
문제
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

입력
첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

출력
첫째 줄에 경우의 수를 출력한다.
'''
import sys

n = int(sys.stdin.readline())
dp = [0] * 31
dp[2] = 3

# 반복문을 통해 점화식을 수행
for i in range(4, n + 1):

    # 짝수만을 타일로 채울 수 있다.
    if i % 2 == 0:
        dp[i] += dp[i - 2] * dp[2]

        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2 # dp[j]에 특수한 모양 2개의 조합

        dp[i] += 2 # 특수한 모양 2개 추가

print(dp[n])