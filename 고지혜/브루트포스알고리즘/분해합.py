# m + m의 각 자리 수 합 = n
# m < n
# 256(m) = 245(n) + 2 + 4 + 5
# 1. for문에서 사용되는 range 범위 - 가장 큰 값 기준으로 범위 결정
# def decomposition(n):
#     # 각 자리수 최대 자연수는 9, m자리수 합은 최대 9*d
#     # range(m의 최소값, 여러 자리수일 경우 고려 ,n을 만들 수 있는 작은 값)
#     for m in range(max(1, len(str(n)), n+1)):
#         # 
#         if m + sum(map(int, str(m))) == n:
#             return m
#     return 0


# n = int(input())
# print(decomposition(n))

# ---------------------------------------------------------

# 2. for문에서 사용되는 range 범위 - n보다 작은 자연수 모두 검사
def decomposition(n):
    # 각 자리수 최대 자연수는 9, m자리수 합은 최대 9*d
    for m in range(n):
        digits_sum = sum(map(int, str(m)))  # m의 각 자리수 합
        if m + digits_sum == n:
            return m
    return 0

n = int(input())
print(decomposition(n))