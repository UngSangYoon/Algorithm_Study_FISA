n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

# dp 배열 생성: 삼각형과 같은 모양의 2차원 배열
dp = [[0] * n for _ in range(n)]
dp[0][0] = triangle[0][0]  # 꼭대기 값 초기화

# 삼각형의 각 줄에 대해 최대 합 계산
for i in range(1, n):
    for j in range(i+1):
        # 맨 왼쪽인 경우
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        # 맨 오른쪽인 경우
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        # 가운데인 경우 두 경로 중 큰 값 선택
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

# 마지막 줄에서 최대 합 찾기
print(max(dp[n-1]))
