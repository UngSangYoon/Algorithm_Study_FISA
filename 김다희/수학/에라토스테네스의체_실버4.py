# 에라토스테네스의 체
# 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.

n, k = map(int, input().split())
li =  list(range(2,n+1)) # n까지 리스트
result = 0
while k > 0: # k를 1만큼 계속 감소
    p = min(li) # p는 리스트 중 최소
    for i in range(len(li)): # 리스트 길이만큼 반복
        if (li[i]%p == 0) & (k > 0): # p의 배수이면
            result = li[i]
            li[i] = 2003 
            k = k-1
print(result)