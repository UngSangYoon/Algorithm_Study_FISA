N = int(input())

d_3 = N // 3
d_5 = N // 5

ans = -1
for i in range(0, d_3 + 1):
    for j in range(0, d_5 + 1):
        if (3 * i + 5 * j) == N:
            if ans == -1 or (i + j) < ans:
                ans = (i + j)

print(ans)