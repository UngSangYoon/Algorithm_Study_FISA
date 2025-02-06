from itertools import combinations
l = []
while True:
    try:
       n = int(input())
       l.append(n)      
    except:
        break

def solution(l):
    for i in combinations(l,7):
        if sum(i)==100:
            l= list(i)
            break
    l.sort()
    return l

for i in solution(l):
    print(i)

#####