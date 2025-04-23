from collections import deque
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
for x in range(N):
    for y in range(M):
        if matrix[y][x] == 1:
            q.append((x, y, 0))

max_day = 0

while q:
    x, y, day = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= ny < M and 0 <= nx < N)  and matrix[ny][nx] == 0:
            matrix[ny][nx] = 1
            q.append((nx, ny, day + 1))
            max_day = max(max_day, day + 1)

for row in matrix:
    if 0 in row:
        print(-1)
        exit()

print(max_day)