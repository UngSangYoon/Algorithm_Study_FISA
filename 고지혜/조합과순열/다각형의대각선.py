# 1. 함수 이용해서 풀기 (math.comb)
# import math

# def count_intersections(n):
#     if n < 4:  # 삼각형까지니는 교차점 개수 0
#         return 0
#     else:
#         return math.comb(n, 4)  # n개 꼭짓점 중 4개 뽑기

# n = int(input())
# print(count_intersections(n))

# ---

# 2. 반복문 사용해서 풀기
def func1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def func2(n, k):
    if n < k:
        return 0
    return func1(n) // (func1(k) * func1(n-k))


def solve():
    n = int(input())
    print(func2(n, 4))

solve()