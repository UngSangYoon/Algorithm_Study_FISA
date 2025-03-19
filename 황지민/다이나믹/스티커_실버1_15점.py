# 9465

# n[0][0]
# n[1][0]

# n[0][0]+n[1][1]
# n[1][0]+n[0][1]

# n[0][0]+n[1][1]+n[0][2]
# n[1][0]+n[0][1]+n[1][2]

# n[0][0]+n[1][1]+n[0][2]+n[1][3]
# n[1][0]+n[0][1]+n[1][2]+n[0][3]

# t = int(input())
# for _ in range(t):
#     tt = int(input())   
#     n = [list(map(int, input().split())) for _ in range(2)]

#     f = [0] * (tt+1)


#     if n[0][0] >= n[1][0]:
#         for i in range(1, tt+1):
#             f[i] = (max(f[i-1] + n[(i+1)%2][i-1], f[i-2]+ n[(i)%2][i-1]))
#     else:
#         for j in range(1, tt+1):
#             f[j] = (max(f[j-1] + n[j%2][j-1], f[j-2]+ n[(j+1)%2][j-1]))


#     print(f[tt])

t = int(input())
for _ in range(t):
    tt = int(input())   
    n = [list(map(int, input().split())) for _ in range(2)]

    if tt == 0:
        print(0)
        continue
    if tt == 1:
        print(max(n[0][0], n[1][0]))
        continue

    f = [[0] * tt for _ in range(2)]
    f[0][0] = n[0][0]
    f[1][0] = n[1][0]
    f[0][1] = n[1][0] + n[0][1]
    f[1][1] = n[0][0] + n[1][1]

    for i in range(2, tt):
        f[0][i] = max(f[1][i-1], f[1][i-2]) + n[0][i]
        f[1][i] = max(f[0][i-1], f[0][i-2])+n[1][i]

    print(max(f[0][tt-1], f[1][tt-1]))