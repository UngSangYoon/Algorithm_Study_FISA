# 9461
 
t = int(input())

n = [int(input()) for _ in range(t)]
max_n = max(n)

f = [0] * (max_n+1)

f[1] = 1
f[2] = 1
f[3] = 1

for i in range(4, max_n+1):
    f[i] = f[i-2]+f[i-3]

for j in n:
    print(f[j])