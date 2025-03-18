# 11726

# 2xn의 직사각형 -> 1x2, 2x1로 채우는 방법의 수

# n = 1 -> 2x1
# 2x1

# n = 2 -> 2x2
# 1x2 1x2
# 2x1 2x1

# n = 3 -> 2x3 ooo
#              ooo
# 1x2 1x2 1x2
# 2x1 2x1 1x2
# 1x2 2x1 2x1


n = int(input())

f = [0] * (n+2)
f[1] = 1
f[2] = 2

for i in range(3, n+1):
    f[i] = (f[i-1] + f[i-2]) % 10007

print(f[n])