# 15903, 카드 합체 놀이
# https://www.acmicpc.net/problem/15903

# 입력: n, m, 그리고 카드에 쓰인 숫자가 담긴 리스트 A

# 1. 최소 힙(minHeap) 초기화:
#    - A의 모든 요소를 minHeap에 넣는다.

# 2. m번 반복:
#    a. 가장 작은 카드 두 장을 minHeap에서 꺼낸다.
#       - x = minHeap에서 최소값 추출
#       - y = minHeap에서 최소값 추출
#    b. 두 카드의 합을 계산:
#       - new_value = x + y
#    c. 합친 결과를 다시 minHeap에 두 번 삽입:
#       - minHeap에 new_value 삽입
#       - minHeap에 new_value 삽입

# 3. 모든 합체가 끝난 후, minHeap에 남아있는 모든 카드 값을 합산:
#    - score = 모든 카드 값의 합

# 4. score 출력

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
minHeap = A

for i in range(m):
    x = min(minHeap)
    A.remove(x)
    y = min(minHeap)
    A.remove(y)

    new_value = x + y
    A.append(new_value)
    A.append(new_value)

print(sum(A))