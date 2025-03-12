# 2748

# 0,1로 시작
# 

N = int(input())
F = [0] * (N+1)
F[0] = 0
F[1] = 1

for i in range(2, N+1):
    F[i] = F[i-2] + F[i-1]

print(F[N])