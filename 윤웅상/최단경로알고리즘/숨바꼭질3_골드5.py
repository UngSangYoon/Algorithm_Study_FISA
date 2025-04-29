from queue import PriorityQueue

INF = int(1e12)
MAX = int(1e5)

# input
N, K = map(int, input().split())

# solve (dijkstra)
time = [INF] * (MAX + 1)

pq = PriorityQueue()
time[N] = 0
pq.put([0, N])

while not pq.empty():
	cur_time, cur_pos = pq.get()

	nexts = [
				(cur_time, 2 * cur_pos),
				(cur_time + 1, cur_pos + 1),
				(cur_time + 1, cur_pos - 1)
			]

	for next_time, next_pos in nexts:
		if 0 <= next_pos <= MAX:
			if next_time < time[next_pos]:
				time[next_pos] = next_time
				pq.put([next_time, next_pos])

print(time[K])
