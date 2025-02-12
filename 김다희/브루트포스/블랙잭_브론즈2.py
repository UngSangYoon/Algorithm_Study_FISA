# 1. 다중 for문 (브루트 포스)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))
max_sum = 0

# 모든 세 카드 조합을 탐색하기 위한 3중 for문
for i in range(n): 
    for j in range(i+1, n): # j는 항상 i보다 뒤쪽에서 선택 
        for k in range(j+1, n): # k는 항상 j보다 뒤쪽에서 선택 
            card_sum = card[i] + card[j] + card[k]

            if (card_sum <= m) and (card_sum > max_sum):
                max_sum = card_sum
print(max_sum)

# 2. 조합으로 접근...
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# card = list(map(int, input().split()))
# max_sum = 0

# def com(index, level, current_sum):
#     global max_sum
#     if level == 3:
#         if (current_sum <= m) & (current_sum > max_sum):
#             max_sum = current_sum
#         return
    
#     for i in range(index, n):
#         com(i + 1, level + 1, current_sum + card[i])

# com(0, 0, 0)
# print(max_sum)