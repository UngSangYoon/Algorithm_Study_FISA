N = int(input())
memo = [0 for _ in range(N+1)]
print(memo)

def F(n):
    # 종료조건
    if n <= 2:
        return n
    
    # 메모제이션
    if memo[n] > 0:
        return memo[n]
    
    memo[n] = F(n-1) + F(n-2)
    memo[n] %= 10007
    return memo[n]

print(F(N))
