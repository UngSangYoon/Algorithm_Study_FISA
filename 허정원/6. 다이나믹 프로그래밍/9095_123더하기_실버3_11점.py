'''
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
'''

n = int(input())

for i in range(n):
    tmp = int(input())

    if tmp == 0:
        print(0)
        continue

    dp = [0] * (max(4, tmp+1)) 
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, tmp+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[tmp])
