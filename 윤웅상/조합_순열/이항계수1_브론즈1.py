n, k = map(int, input().split())
ans = 1
k_fac = 1

for i in range(n-k+1, n+1):
    ans *= i

for i in range(1, k+1):
    k_fac *= i
print(ans//k_fac)