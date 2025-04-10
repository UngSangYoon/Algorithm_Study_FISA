'''
문제
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
'''
'''
[문제 설명]
- 1개의 회의실에 N개의 회의를 최대한 많이 배정하는 문제
- 각 회의는 시작 시간과 종료 시간이 주어짐
- 회의는 중단될 수 없음
- 한 회의가 끝나는 즉시 다음 회의 시작 가능
- 시작시간과 종료시간이 같을 수 있음 (시작하자마자 끝나는 것으로 간주)
'''

# 회의의 개수 N 입력받기
N = int(input())

# N개의 회의 정보를 저장할 2차원 리스트 초기화
# A[i][0]: i번째 회의의 종료 시각
# A[i][1]: i번째 회의의 시작 시각
A = [[0] * 2 for _ in range(N)]

# N개의 회의 정보 입력받기
for i in range(N):
    S, E = map(int, input().split())
    # 종료시각을 첫 번째 원소로 저장 (정렬의 첫 번째 기준)
    A[i][0] = E  
    # 시작시각을 두 번째 원소로 저장
    A[i][1] = S

# 회의를 종료시각 기준으로 정렬
# 종료시각이 같은 경우 시작시각이 빠른 순으로 정렬됨
A.sort()

# 선택된 회의 개수를 카운트
count = 0
# 이전 회의의 종료 시각을 저장 (초기값: -1)
end = -1

# 모든 회의를 순회하면서 겹치지 않는 회의 선택
for i in range(N):
    # 현재 회의의 시작시각이 이전 회의의 종료시각보다 크거나 같으면
    if A[i][1] >= end:
        # 현재 회의 선택
        end = A[i][0]  # 종료시각 갱신
        count += 1     # 회의 개수 증가

# 최대 회의 개수 출력
print(count)