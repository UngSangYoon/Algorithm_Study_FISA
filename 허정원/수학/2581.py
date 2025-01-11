def divisor(x):
    cnt = 0
    for i in range(2, x+1):
        if x % i == 0:
            cnt += 1
    return cnt

a = int(input())
b = int(input())
lst = []

for j in range(a, b+1):
    if divisor(j) == 1:
        lst.append(j)

if len(lst) == 0:
    print(-1)
else: 
    print(sum(lst))
    print(lst[0])
