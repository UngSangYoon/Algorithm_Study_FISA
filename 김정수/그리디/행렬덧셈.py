n,m = map(int, input().split())

A = []

for _ in range(n*2):
    A.append(list(map(int, input().split())))


ans = 0


for i in range(n):
    for j in range(m):
        ans = A[i][j] + A[i+n][j]
        print(ans, end=" ")
    print()