t = int(input())

def gold(n):
    gold_pair = []
    for p in range(2, (n//2)+1):
        if sosu[p] & sosu[n-p]:
               gold_pair.append((p, n-p))
    print(gold_pair[-1][0], gold_pair[-1][1])
    return
               
sosu = [True] * 10001
sosu[0], sosu[1] = False, False
for i in range(2, int(10000**(0.5))+1):
    if sosu[i]:
        for j in range(i*i, 10001, i):
            sosu[j] = False

for _ in range(t):
    n = int(input())
    gold(n)