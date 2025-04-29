from collections import deque


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, h):
    q = deque()
    q.append((y, x))
    visited[y][x] = True

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < N and 0 <= nx < N) and (not visited[ny][nx]) and(lst[ny][nx] > h):
                q.append((ny, nx))
                visited[ny][nx] = True

max_count = 1
for h in range(min(map(min, lst)), max(map(max, lst))+1):
    visited = [[False] * (N) for _ in range(N)]
    count = 0
    for y in range(N):
        for x in range(N):
            if lst[y][x] > h and not visited[y][x]:
                count += 1
                bfs(y,x,h)
    max_count = max(max_count, count)

print(max_count)