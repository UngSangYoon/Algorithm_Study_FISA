n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

array_s = sorted(array, key = lambda x : (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))

for i in array_s[:3]:
    print(i[0], end = ' ')