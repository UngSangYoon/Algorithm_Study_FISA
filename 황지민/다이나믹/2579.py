# 2579

# 1칸 -> 1
# 2칸 -> 1 2, 2
# 3칸 -> 1 3, 2 3
# 4칸 -> 1 2 4, 1 3 4, 2 4

n = int(input())
score = [0] + [int(input()) for _ in range(n)]

f = [0] * (n+1)
if n == 1:
    print(score[1])
elif n ==2:
    print(score[1] + score[2])
else:
    f[1] = score[1]
    f[2] = score[1]+score[2]
    f[3] = max(score[1] + score[3], score[2] + score[3])

    for i in range(4, n+1):
        f[i] = max(f[i-2] + score[i], f[i-3] + score[i-1] + score[i])

    print(f[n])