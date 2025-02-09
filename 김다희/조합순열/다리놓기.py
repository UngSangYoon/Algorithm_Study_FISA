import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans = (math.prod(range(m-n+1, m+1)))/(math.prod(range(1, n+1)))
    print(int(ans))