# 풀이 1번 -> recursion error 발생

# n, k = map(int, input().split())

# # 팩토리얼 구현
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(n) // (factorial(k) * factorial(n - k)))

# 풀이 2번 - for문으로 구현
n, k = map(int, input().split())

def factorial(n):
    result = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(n) // (factorial(k) * factorial(n - k)))