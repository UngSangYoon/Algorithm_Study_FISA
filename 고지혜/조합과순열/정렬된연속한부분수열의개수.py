import sys
import itertools

def count_increasingarrays():
    input_ = sys.stdin.readlines()
    n = int(input_[0].strip())  # 수열의 길이 n
    list_ = list(map(int, input_[1].split()))
    
    count = 0
    # length = 1        

    # i는 구간의 시작을 의미
    for i in range(n):
        # j는 구간의 끝을 의미, j는 i부터 시작해서 오름차순 구간을 확인
        for j in range(i, n):
            if i == j or list_[j-1] < list_[j]:  # 현재 요소가 이전 요소보다 크면 오름차순 구간 계속됨
                count += 1
            else:
                break  # # list_[i]가 이전 원소보다 작거나 같으면 오름차순 구간 끊어짐, j 증가x
            
    return count

print(count_increasingarrays())
