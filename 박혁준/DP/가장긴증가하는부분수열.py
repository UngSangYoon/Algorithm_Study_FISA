# 품
n = int(input())
A = list(map(int, input().split()))

B = [1] * n

for k in range(n):
    for j in range(k):
        if A[k] > A[j]:
            B[k] = max(B[k], B[j]+1)


ans = max(B)
print(ans)