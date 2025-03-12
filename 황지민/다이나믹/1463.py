# 1463

# 1. X%3 == 0 -> x/3
# 2. X%2 == 0 -> x/2
# 3. x-1

x = int(input())

f = [0] * (x+1) # DP 테이블

for i in range(2, x+1):
    f[i] = f[i-1]+1 # 1을 빼는 경우

    if i % 2 == 0:
        f[i] = min(f[i], f[i//2]+1) # 2로 나누는 경우

    if i % 3 == 0:
        f[i] = min(f[i], f[i//3]+1) # 3으로 나누는 경우

print(f[x])
    