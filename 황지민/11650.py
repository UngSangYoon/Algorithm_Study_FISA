# 11650

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

result = sorted(a, key = lambda x: (x[0], x[1]))

for i in result:
    print(i[0], i[1])
