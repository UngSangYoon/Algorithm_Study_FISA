from collections import deque

N, M = map(int, input().split())
Maze = [[0] * M for _ in range(N)]
Visited = [[False] * M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(N):
    numbers = list(input())
    for j in range(M):
        Maze[i][j] = int(numbers[j])


def BFS(x, y):
    q = deque()
    q.append((x, y))
    Visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < M
                and Visited[nx][ny] == False
                and Maze[nx][ny] != 0
            ):
                Visited[nx][ny] = True
                q.append((nx, ny))
                Maze[nx][ny] = Maze[cx][cy] + 1


BFS(0, 0)
print(Maze[N - 1][M - 1])