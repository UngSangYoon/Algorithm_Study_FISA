'''
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
