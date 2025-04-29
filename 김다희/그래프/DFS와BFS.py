# 1260, DFS와 BFS
# https://www.acmicpc.net/problem/1260

from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것부터 방문하기 위해 정렬
for i in graph:
    i.sort()

visited = [False] * (n + 1)

# DFS (재귀 사용)
def dfs(v, visited):
    '''
    v: 지금 정점 위치
    visited: 방문한 정점 확인 리스트 (T: 방문, F: 미방문)
    '''
    visited[v] = True
    print(v, end=' ')
    for u in graph[v]: # 현재 정점 이웃들에서
        if not visited[u]: # 만약 방문 안 했으면
            dfs(u, visited) # 재귀 호출


# BFS (큐 사용)
def bfs(start):
    '''
    start: 시작 정점 위치
    '''
    visited = [False]*(n+1) 
    queue = deque([start]) # 큐에 시작 정점 추가
    visited[start] = True # 시작 정점 방문
    while queue: # 큐에 남은 정점이 없을 때까지
        v = queue.popleft() # 큐의 첫 번째 정점 꺼내기
        print(v, end = ' ') # 꺼낸 정점 출력
        for u in graph[v]: # 꺼낸 정점 이웃들에서
            if not visited[u]: # 만약 방문 안 했으면
                visited[u] = True # 방문 체크
                queue.append(u) # 큐에 추가


# 실행
dfs(v, visited)
print()
bfs(v)
