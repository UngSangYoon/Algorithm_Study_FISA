
T = int(input())
for _ in range(T):
    n = int(input())
    
    top = list(map(int, input().split()))
    bottom = list(map(int, input().split()))
    
    # DP 테이블 설계 -> 각 열 위/아래/선택x 3가지 경우 -> n * 3의 테이블 설계
    dp = [[0]*3 for _ in range(n+1)] # n이 4인 경우 dp   
                                     #   [0 0 0] 
                                     #   [0 0 0] 
                                     #   [0 0 0]
                                     #   [0 0 0]
                                     #   [0 0 0]
    for i in range(1, n+1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + top[i-1] # 현재 열에서 위 스티커 선택
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + bottom[i-1]# 현재 열에서 아래 스티커 선택
        dp[i][2] = max(dp[i-1])  # 현재 열에서 아무것도 선택하지 않음

    print(max(dp[n]))