from math import prod # 리스트 내부 원소들의 곱하기기...

num = list(range(1,11))

def com(n,k):
    ans = int(prod(num[n-k:n])/prod(num[:k]))
    return ans

n, k = map(int, input().split())
print(com(n,k))