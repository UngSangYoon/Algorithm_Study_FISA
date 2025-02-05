N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]

dots = sorted(dots)

for x, y in dots:
	print(x, y)