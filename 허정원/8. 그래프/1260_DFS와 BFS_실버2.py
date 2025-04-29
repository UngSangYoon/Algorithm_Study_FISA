'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''

from collections import deque

N, M, V = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(M)]

# 인접 리스트 그래프 생성
graph = {i: [] for i in range(1, N + 1)}
for a, b in table:
    graph[a].append(b)
    graph[b].append(a)

# 오름차순
for key in graph:
    graph[key].sort()

# DFS
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=' ')
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue: # queue가 빌 때까지 계속 반복
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

# 5. 실행
dfs(graph, V)
print()
bfs(graph, V)
