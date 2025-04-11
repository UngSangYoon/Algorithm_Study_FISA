# 2606. 바이러스
# https://www.acmicpc.net/problem/2606

# DFS로 구현 (이 방식이 더 쉬워서...)
# DFS vs BFS?
# DFS: 모든 경로를 탐색해야 할 때, 도달 여부만 확인할 때
# 모든 경로/조합 탐색 (완전탐색)
# 특정 노드에서 시작해서 다른 노드에 도달 가능한가?
# 그래프 내 구조 판별
# 트리 순회 및 탐색

# BFS: 최단 경로(최소 이동 횟수) 를 구할 때, 확산/전파 문제
# 불이 붙은 칸이 몇 초 뒤 어디까지 번지는가
# 바이러스가 퍼지는데 최소 몇 분 걸리는가
# 친구 추천에서 ‘2단계 친구’까지만 감염됨

import sys

input = sys.stdin.readline
C = int(input()) # 컴퓨터 개수
N = int(input()) # 간선 개수
graph = [[] for _ in range(C+1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(C+1)
cnt = -1

def dfs(v):
    global cnt
    visited[v] = True
    cnt = cnt + 1
    for u in graph[v]:
        if not visited[u]:
            dfs(u)

dfs(1)
print(cnt)
