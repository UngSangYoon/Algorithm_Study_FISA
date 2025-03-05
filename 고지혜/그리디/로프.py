'''
< k개의 로프를 사용해서 중량이 w인 물체 들어올리기>
# 각 로프 w/k만큼 중량 걸림
# 로프로 들어올릴 수 있는 최대 중량 구하기
1. 로프 내림차순(동전0과 비슷)
2. 최대 로프 중량 계산
'''
import sys

def rope(n, ropes):
    # 로프 내림차순
    ropes.sort(reverse=True)  # 내림차순
    # -> 로프를 여러개로 병렬했을 때, 가장 약한 로프를 고려해야함
    # 가장 약한 로프 * 사용개수(n) = 최대 중량이니까 내림차순으로 정렬해서 계산하기

    # 최대 중량
    max_w = 0
    for i in range(n):  # ex. n=2, i=0,1
        max_w = max(max_w, ropes[i] * (i + 1))  # 15*1=15, 10*2=20

    return max_w

n = int(sys.stdin.readline().strip())  # 로프 개수  
# n개의 줄에 각 로프가 버틸 수 있는 최대 중량
ropes = [int(sys.stdin.readline().strip()) for _ in range(n)]  # ex. 10 15
print(rope(n, ropes))

'''
ropes = 10, 15, 5일 때
15만 사용 - 15*1=15 -> max(0, 15)=15
15, 10 사용 - 15*1 vs 10*2 -> max(15, 20)=20
15, 10, 5 사용 - 15*1 vs 10*2 vs 5*3 -> max(20, 15)=20
'''