# 11726
# 품

'''
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
'''

n = int(input())

if n <= 2:
    print(n)

else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2])
    
    print((dp[n])%10007)
