# 14501

# 오늘 + N + 1 : 퇴사날짜
# N: 일을 할 일수

# ti = 처리하는데 걸리는 일수
# pi = 받을 액수

# f[n]
# f[1] = 0
# f[2] = 0
# f[3] = 10
# f[4] = 10 + 20
# f[5] = 10 + 20
# f[6] = 10 + 20 + 15
# f[7] = 10 + 20 + 15

n = int(input())
ti_lst = []
pi_lst= []
for _ in range(n):
    ti, pi = map(int, input().split())
    ti_lst.append(ti)
    pi_lst.append(pi)

f = [0] * (n+1)

for i in range(n-1, -1, -1):
    if ti_lst[i] + i > n:
        f[i]= f[i+1]
    else:
        f[i] = max(pi_lst[i]+f[i+ti_lst[i]], f[i+1])

print(f[0])

