# BFS 로 구현


N = int(input())
M = int(input())

# 그래프 인접리스트로 구현
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

visited = [False] * (N+1)

def bfs (start_node):
    queue = deque([start_node])
    visited[start_node] = True
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
bfs(1)

print(sum(visited)-1)