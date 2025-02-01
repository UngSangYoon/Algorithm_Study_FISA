n = int(input())

array = [tuple(map(int, input().split())) for _ in range(n)]

for i in sorted(array):
    print(i[0], i[1])