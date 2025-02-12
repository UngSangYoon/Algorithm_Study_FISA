n = int(input())
cnt = 0; min_cnt = 10000

for i in range(n//5 + 1):
    for j in range(n//3 + 1):
        if i*5 + j*3 == n:
            min_cnt = min(min_cnt, i+j)

if min_cnt == 10000:
    print(-1)
else:
    print(min_cnt)