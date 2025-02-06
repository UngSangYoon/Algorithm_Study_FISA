N = int(input())

lst = [tuple(map(int, input().split())) for _ in range(N)]

lst = sorted(lst)
for x, y in lst:
    print(x, y)