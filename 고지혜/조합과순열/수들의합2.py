# 연속된 수열
# 1. 시간 복잡도(O(n^2)) -> 입력 데이터 커지면 성능 문제
# def count_sum(n, m, data):
#     count = 0  # 합이 m이 되는 경우의 수

#     for i in range(1, n+1):  # i=1, 1~10
#         sum = 0  # 합계
#         # 1 2
#         # 1 2 3
#         # 1 2 3 4(멈추고 i 넘어감)
#         for j in range(i, n+1):  # i=1, j=1~10
#             sum += data[j-1]
#             if sum == m:
#                 count += 1
#                 break

#     return count

# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# print(count_sum(n, m, data))

# --

# 2. 시간 복잡도(O(n)) -> 성능 문제 해결하기
# 10 5
# 1 2 3 4 2 5 3 1 1 2
def count_sum(n, m, data):
    count = 0  # 합이 m이 되는 경우의 수
    start = 0
    sum = 0

    for end in range(n):  
        sum += data[end]  

        while sum > m:  # 합이 m보다 크다면 start 증가시키기(시작부분 옮기기)
            sum -= data[start]  
            start += 1
        
        if sum == m:
            count += 1

    return count    

n, m = map(int, input().split())
data = list(map(int, input().split()))
print(count_sum(n, m, data))