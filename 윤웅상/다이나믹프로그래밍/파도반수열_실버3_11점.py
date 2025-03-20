# 1,1,1,2,2,3,4,5,7,9(7+2),12(9+3),16(12+4),21(16+5),28(21+7),(28+9)
# 규칙 : 현재 가장 큰 수(최근에 추가된 수) + 4번째로 큰 수
# P[N] = P[N-1] + P[N-5]

T = int(input())
N_list = []

for _ in range(T):
    N = int(input())
    N_list.append(N)

max_n = max(N_list)

p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]
for i in range(12, max_n + 1):
    p.append(p[i-1] + p[i-5])

for i in N_list:
    print(p[i])