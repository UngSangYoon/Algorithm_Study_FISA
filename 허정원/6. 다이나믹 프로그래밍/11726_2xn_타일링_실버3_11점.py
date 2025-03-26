'''
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.


'''

n = int(input())

dp = [0] * (max(3, n+1))
dp[1], dp[2] = 1, 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
