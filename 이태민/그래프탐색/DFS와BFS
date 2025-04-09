'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''

# DFS와 BFS를 구현하기 위한 그래프를 인접 리스트로 표현
from collections import deque

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프를 정점 번호가 작은 순서로 방문하기 위해 정렬
for i in range(N + 1):
    graph[i].sort()

# DFS 구현 -> 재귀함수 사용
def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i) 

# BFS 구현 -> 큐를 사용
def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 정점 하나를 꺼낸다.
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

# DFS 탐색 시작
dfs(V)
print()
# BFS 탐색 시작
bfs(V)
