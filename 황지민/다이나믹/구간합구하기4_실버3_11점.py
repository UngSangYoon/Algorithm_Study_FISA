
# 11659

n, m = map(int, input().split())

n_num = list(map(int, input().split()))

f = [0] * (n+1)
for i in range(n):
    f[i+1] = f[i] + n_num[i]

for i in range(m):
    start, end = map(int, input().split())
    print(f[end] - f[start-1])

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_num = list(map(int, input().split()))

f = [0] * (n+1)
for i in range(n):
    f[i+1] = f[i] + n_num[i]

result = []
for _ in range(m):
    start, end = map(int, input().split())
    result.append(str(f[end] - f[start-1]))

sys.stdout.write("\n".join(result))

