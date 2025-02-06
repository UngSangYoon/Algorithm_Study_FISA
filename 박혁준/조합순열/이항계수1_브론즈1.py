# (1 ≤ (N\) ≤ 10, 0 ≤ (K\) ≤ (N\))
# 위 조건일 때, n!/k!*(n-k)!
import math
n, k = map(int, input().split())
def solution(n, k):
    ans = int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))    
    return ans

print(solution(n, k))


#####