'''
문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

from queue import PriorityQueue
INF = int(1e5)

N, E = map(int, input().split())
adj_list = [[] for _ in range(N + 1)] # 1-index

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

v1, v2 = map(int, input().split())

def dijkstra(start):
    global N, adj_list
    dist = [INF] * (N+1)
    pq = PriorityQueue()
    dist[start] = 0
    pq.put([0, start])

    while not pq.empty():
        cur_dist, cur_node = pq.get()
        if cur_dist > dist[cur_node]:
            continue
        for adj_node, adj_dist in adj_list[cur_node]:
            temp_dist = cur_dist + adj_dist
            if temp_dist < dist[adj_node]:
                dist[adj_node] = temp_dist
                pq.put([temp_dist, adj_node])
    
    return dist


# 1 start
dist_1 = dijkstra(1)
# v1 start
dist_v1 = dijkstra(v1)
# v2 start
dist_v2 = dijkstra(v2)

route1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
route2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]
best = min(route1,route2)

print(best if best < INF else -1)