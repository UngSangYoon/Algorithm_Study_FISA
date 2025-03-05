# # 1. replace를 사용하여 5->6, 6->5 모든 경우 고려
def min_max_sum(a, b):
    # 최소값 계산 (5를 6으로 착각하지 않게 & 6을 5로 변경)
    min_a = int(a.replace('6', '5'))
    min_b = int(b.replace('6', '5'))
    min_sum = min_a + min_b

    # 최대값 계산 (6을 5로 착각하지 않게 & 5를 6으로 변경)
    max_a = int(a.replace('5', '6'))
    max_b = int(b.replace('5', '6'))
    max_sum = max_a + max_b

    return min_sum, max_sum

a, b = input().split()
min_sum, max_sum = min_max_sum(a, b)
print(min_sum, max_sum)

# ------------------------------------------
# 2. itertools 사용하기 & 1번 방법 
# from itertools import product

# def min_max_sum(A: str, B: str):
#     # 가능한 모든 값 set에 넣기
#     possible_A = set([A.replace('5', '6'), A.replace('6', '5')])
#     possible_B = set([B.replace('5', '6'), B.replace('6', '5')])
    
#     # 모든 조합의 합 구하기
#     all_sums = [int(a) + int(b) for a, b in product(possible_A, possible_B)]
    
#     return min(all_sums), max(all_sums)

# # 입력 받기
# A, B = input().split()
# min_result, max_result = min_max_sum(A, B)
# print(min_result, max_result)
