from itertools import product

def solution(n):
    l1 = []
    for i in range(1,n+1):
        l1.append(i)
    cnt = 0
    for i in product(l1, repeat=2):
        if len(set(i)) == 2:
            cnt+=1
    return cnt
n = int(input())
print(solution(n))