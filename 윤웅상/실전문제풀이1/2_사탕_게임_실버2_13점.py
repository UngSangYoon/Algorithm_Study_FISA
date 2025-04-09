# 브루트 포스

def get_max_candies(matrix, N):
    max_candies = 0
    
    # 행 검사
    for i in range(N):
        count = 1
        for j in range(1, N):
            if matrix[i][j] == matrix[i][j-1]:
                count += 1
            else:
                count = 1
            max_candies = max(max_candies, count)
    
    # 열 검사
    for j in range(N):
        count = 1
        for i in range(1, N):
            if matrix[i][j] == matrix[i-1][j]:
                count += 1
            else:
                count = 1
            max_candies = max(max_candies, count)
    
    return max_candies

N = int(input())
matrix = [list(input()) for _ in range(N)]
max_candies = 0

# 모든 가능한 인접한 쌍에 대해 교환하고 최대값 계산
for i in range(N):
    for j in range(N):
        # 오른쪽과 교환
        if j + 1 < N:
            matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
            max_candies = max(max_candies, get_max_candies(matrix, N))
            matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
        
        # 아래쪽과 교환
        if i + 1 < N:
            matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
            max_candies = max(max_candies, get_max_candies(matrix, N))
            matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]

print(max_candies)