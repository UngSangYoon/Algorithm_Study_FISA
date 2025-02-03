# 1. for문으로 풀기
# 5 21
# 5 6 7 8 9, 5C3=10
import sys

n, m = map(int, sys.stdin.readline().split())  # N과 M 입력
cards = list(map(int, sys.stdin.readline().split()))

max_sum = 0  # m과 가까운 합 

for i in range(n - 2):  # 첫 번째 카드
    for j in range(i + 1, n - 1):  # 두 번째 카드
        for k in range(j + 1, n):   # 세 번째 카드
            card_sum = cards[i] + cards[j] + cards[k]
            # M 이하이면서 가장 큰 값이면 max_sum 갱신
            if card_sum <= m and card_sum > max_sum:
                max_sum = card_sum

print(max_sum) 
# ---------------------------------------------------
# 2. combinations 함수 이용해서 풀기
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())  # N과 M 입력
cards = list(map(int, sys.stdin.readline().split()))

max_sum = 0  # m과 가까운 합 

for set_ in combinations(cards, 3):
    card_sum = sum(set_)
    if card_sum <= m:
        max_sum = max(max_sum, card_sum)

print(max_sum)
# ---------------------------------------------------
# >> 약 0.1097초, 약 0.1147초
# 3중 for문이 더 빠르지만 차이가 미미하기 때문에 코드 가독성을 고려하면 combinations() 쓰는게 좋을 것 같음.
# import time
# import itertools

# # 테스트 데이터 설정
# n, m = 100, 500  # 카드 개수: 100, 최대 합: 500
# cards = list(range(1, 101))  # 1부터 100까지 숫자로 카드 리스트 생성

# # 함수 없이 3중 for문 사용 (Brute Force)
# start_time = time.time()
# max_sum_for = 0

# for i in range(n - 2):
#     for j in range(i + 1, n - 1):
#         for k in range(j + 1, n):
#             card_sum = cards[i] + cards[j] + cards[k]
#             if card_sum <= m and card_sum > max_sum_for:
#                 max_sum_for = card_sum

# end_time = time.time()
# brute_force_time = end_time - start_time

# # itertools.combinations() 사용
# start_time = time.time()
# max_sum_combinations = 0

# for combo in itertools.combinations(cards, 3):
#     card_sum = sum(combo)
#     if card_sum <= m and card_sum > max_sum_combinations:
#         max_sum_combinations = card_sum

# end_time = time.time()
# combinations_time = end_time - start_time

# # 결과 출력
# print(brute_force_time, combinations_time)