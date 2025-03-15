# 9095
# 품
'''
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
'''

# 풀이
'''
n을 1,2,3 에 대한 합으로 나타낸 개수를 s(n)이라고 하면,
s(1) = 1
s(2) = 2
s(3) = 4
s(4) = 7
s(5) = 13
...
s(7) = 44
로 이어져 나간다.
규칙을 정리하자면, s(n) = s(n-1) + s(n-2) + s(n -3)이라는 규칙이 생긴다.
'''
'''
def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    if n > 3 :
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    return dp[n]

total = int(input())

for _ in range(1,total+1):
    n = int(input())
    print(solution(n))
    
'''
# 문제에서 n은 11보다 작음

total = int(input())

dp = [0] * (13)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 13):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(1,total+1):
    n = int(input())
    print(dp[n])
        