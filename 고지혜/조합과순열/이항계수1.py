# # math 모듈의 comb 함수 사용
# import math
# n, k = map(int, input().split())

# result = math.comb(n, k)  
# print(result)

# 팩토리얼로 직접 구하기
def factorial(n):
    if n == 0:
        return 1  # 0Ck=1
    else:
        return n * factorial(n-1)  

n, k = map(int, input().split())  # 4 2 -> 4C2=6
# n! / k! * (n-k)!
result = factorial(n) // (factorial(k) * factorial(n-k))  

print(result)