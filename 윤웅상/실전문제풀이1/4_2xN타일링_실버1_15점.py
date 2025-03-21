n = int(input())

# 1 -> 1
# 2 -> 2
# 3 -> 3
# 4 -> 5

#    n = 4 가 되는 경우
# -> n = 2 에서 = 을 추가
# -> n = 3 에서 ㅣ 을 추가
if n == 1:
 print(1)

else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n]%10007)
