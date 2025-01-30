# def pascal(n, k):
#     if n >= k:  
#         return math.comb(n-1, k-1)
#     else:
#         return 0
# => # 문제에서 1<=k<=n<=30을 만족하므로 작성 필요x

# import math    
# 1. 함수 이용해서 풀기
# n, k = map(int, input().split())
# print(math.comb(n-1, k-1))

# 2. 함수 사용하지 않기 - for문으로
n, k = map(int, input().split())  # 5 3 -> 4C2 = 6

result = 1
for i in range(k-1):  # 0 1 
    # (n-1)C(r-1) = (n-1)! / (r-1)!*(n-r)!
    # 분자 -> (n-1)*(n-2)*..*(n-k+1)
    # result = result * ((n - 1) - i)
    result *= (n - 1 - i)
    # 분모 -> 1*..*(k-1)
    # result  = result // (i + 1)  
    result //= (i + 1)  

print(result)