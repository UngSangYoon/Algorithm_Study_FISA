
# 완전탐색
# 1. arr에서 8*8 부분배열을 모두 확인
# 2. 각 부분배열에서 확인 -> 비효율적일 것 같음 


# 2차원 누적합 테이블 따로 설계
# 1. 1열, 1행 누적합 선행 처리
# 2. 각 행/열 인덱스에서 -1 
# BBB    011
# BBB -> 123  
# BBB    134
n, m = map(int, input().split())
arr = [([' '] + list(input())) for _ in range(n)]
arr.insert(0, [' ']*(m+1))

dp_w = [[0]*(m+1) for _ in range(n+1)] # 행/열 인덱스 합 짝수가 'W' 
dp_b = [[0]*(m+1) for _ in range(n+1)] # 행/열 인덱스 합 짝수가 'B' 

# DP 테이블 초기값 처리
# 1열 처리
for x in range(1, n+1):    
    if arr[x][1] == 'B': # 현재 칸이 Black
        if x % 2 == 1:   # 홀수번째 수
            dp_w[x][1] = dp_w[x-1][1] + 1 # B -> W
            dp_b[x][1] = dp_b[x-1][1]     # B -> B

        else:            # 짝수번째 수
            dp_w[x][1] = dp_w[x-1][1]     # B -> B
            dp_b[x][1] = dp_b[x-1][1] + 1 # B -> W
    
    else:                # 현재 칸이 White
        if x % 2 == 1:   # 홀수번째 수
            dp_w[x][1] = dp_w[x-1][1]     # W -> W
            dp_b[x][1] = dp_b[x-1][1] + 1 # W -> B
                         # 현재 칸이 White
        else:            # 짝수번째 수
            dp_w[x][1] = dp_w[x-1][1] + 1 # W -> B
            dp_b[x][1] = dp_b[x-1][1]     # W -> W
# 1행 처리
for y in range(1, m+1):
    if arr[1][y] == 'B': # 현재 칸이 Black
        if y % 2 == 1:   # 홀수번째 수
            dp_w[1][y] = dp_w[1][y-1] + 1 # B -> W
            dp_b[1][y] = dp_b[1][y-1]     # B -> B

        else:            # 짝수번째 수
            dp_w[1][y] = dp_w[1][y-1]     # B -> B
            dp_b[1][y] = dp_b[1][y-1] + 1 # B -> W
    
    else:                # 현재 칸이 White
        if y % 2 == 1:   # 홀수번째 수
            dp_w[1][y] = dp_w[1][y-1]     # W -> W
            dp_b[1][y] = dp_b[1][y-1] + 1 # W -> B

        else:            # 짝수번째 수
            dp_w[1][y] = dp_w[1][y-1] + 1 # W -> B
            dp_b[1][y] = dp_b[1][y-1]     # W -> W

# DP 테이블 채우기
for x in range(2, n+1):
    for y in range(2, m+1):
        if (x+y) % 2 == 0: # 합이 짝수
            if arr[x][y] == 'W':
                dp_w[x][y] = dp_w[x][y-1] + dp_w[x-1][y] - dp_w[x-1][y-1]     # W -> W
                dp_b[x][y] = dp_b[x][y-1] + dp_b[x-1][y] - dp_b[x-1][y-1] + 1 # W -> B
            else:
                dp_w[x][y] = dp_w[x][y-1] + dp_w[x-1][y] - dp_w[x-1][y-1] + 1 # B -> W
                dp_b[x][y] = dp_b[x][y-1] + dp_b[x-1][y] - dp_b[x-1][y-1]     # B -> B
            
        else:
            if arr[x][y] == 'W':
                dp_w[x][y] = dp_w[x][y-1] + dp_w[x-1][y] - dp_w[x-1][y-1] + 1 # W -> B
                dp_b[x][y] = dp_b[x][y-1] + dp_b[x-1][y] - dp_b[x-1][y-1]     # W -> W
            else:
                dp_w[x][y] = dp_w[x][y-1] + dp_w[x-1][y] - dp_w[x-1][y-1]     # B -> B
                dp_b[x][y] = dp_b[x][y-1] + dp_b[x-1][y] - dp_b[x-1][y-1] + 1 # B -> W

min_cost = 10e9

for x in range(8, n+1):
    for y in range(8, m+1):
        cost = min(dp_w[x][y] - dp_w[x-8][y] - dp_w[x][y-8] + dp_w[x-8][y-8], dp_b[x][y] - dp_b[x-8][y] - dp_b[x][y-8] + dp_b[x-8][y-8])
        min_cost = min(min_cost, cost)

print(min_cost)