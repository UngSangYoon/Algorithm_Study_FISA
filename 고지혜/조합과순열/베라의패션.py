# 베라의 패션

n = int(input())

# 모든 조합 개수 n*n, 상=하 n가지 -> n*n-n=n(n-1) 
result = n * (n-1)
print(result)

# 2. => 메모리 초과  (n*n개 조합 모두 저장하기 때문))
# from itertools import product

# n = int(input())

# # 모든 조합
# cloth = range(1, n+1)  # 1~n
# comb = list(product(cloth, cloth))  # n*n

# # print(len(comb))  # n=5 일때, 25
# # 상, 하의가 다른 경우
# diff = [(top, bottom) for top, bottom in comb if top != bottom]

# print(len(diff))

# 3. => 메모리 초과
# from itertools import product

# n = int(input())

# # 모든 조합
# cloth = range(1, n+1)  # 1~n
# comb = list(product(cloth, cloth))  # n*n
# diff = []
# for top, bottom in comb:
#     if top != bottom:
#         diff.append((top, bottom))  # 여러개 값은 튜플로

# print(len(diff))
