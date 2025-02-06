# 7 난쟁이 키 합은 100, 9개 키 \n 단위로 입력 받기
# 여러 개 경우인 경우 합 키인 경우 중 아무거나 출력

#1. itertools로 풀기
# import sys
# from itertools import combinations

# def sevenDwarf():
#     input_data = sys.stdin.read().splitlines()
#     heights = list(map(int, input_data))   # 9개 난쟁이 키 정수로 변환
#     total_sum = sum(heights)

#     for comb in combinations(heights, 2):  # 2명 선택하는 모든 조합
#         if total_sum - sum(comb) == 100:  # 나머지 7명 합 100인지 확인하기
#             result = [h for h in heights if h not in comb]  # 나머지 7명 선택
#             result.sort()  # 오름차순 정렬

#             for height in result:
#                 print(height)
#             return
        
# sevenDwarf()

# ---

# 2. for문으로 풀기
import sys

def sevenDwarf():
    input_data = sys.stdin.read().splitlines()
    heights = list(map(int, input_data))   # 9개 난쟁이 키 정수로 변환
    total_sum = sum(heights)


    for i in range(9):
        for j in range(i+1, 9):
            if total_sum - (heights[i] + heights[j]) == 100:
                # i와 j 제외한 나머지 7명 키
                # k는 전체 난쟁이, i와 j는 제외된 난쟁이
                result = [heights[k] for k in range(9) if k != i and k != j]
                result.sort()  # 오름차순 정렬

                for height in result:
                    print(height)  # 정렬된 키 출력
                return 

sevenDwarf()