# 풀었던 코드 , dp알고리즘으로 풀지 못함함 
N = int(input())


dp = [0] * N

for i in range(N):
    if i == 0 :
        dp[0] = 'SK'
    elif i == 1 :
        dp[1] = 'CY'
    elif i % 2 == 0:
        dp[i] = 'SK'
    else:
        dp[i] = 'CY'
print(dp[N-1])

#########################################################################################################
#dp 알고리즘으로 풀었을때 

N = int(input())

# dp[i]는 돌이 i개 남았을 때, 현재 턴인 사람이 이길 수 있으면 True, 아니면 False
dp = [False] * (N + 1)

# 기본 경우 설정하기
dp[0] = False         # 돌이 0개면 이길 수 없음
if N >= 1:
    dp[1] = True      # 돌이 1개면 1개 가져가서 승리
if N >= 2:
    dp[2] = False     # 돌이 2개면, 1개만 가져갈 수 있는데, 그럼 상대가 이길 수 있음
if N >= 3:
    dp[3] = True      # 돌이 3개면, 3개 가져가서 승리

# 돌이 4개 이상일 때, dp 배열 채우기
for i in range(4, N + 1):
    # i개 남았을 때, 만약 내가 1개 또는 3개를 가져간 후 상대가 지는 경우(False)가 있다면,
    # 나는 이길 수 있다.
    if not dp[i - 1] or not dp[i - 3]:
        dp[i] = True
    else:
        dp[i] = False

# dp[N]이 True면 상근이가 이기고, False면 창영이가 이기는 거야.
print("SK" if dp[N] else "CY")
