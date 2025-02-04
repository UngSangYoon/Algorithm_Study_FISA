# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
# 리스트 안에 튜플 형식으로 넣고, 정렬하여 출력

import sys
input = sys.stdin.readline 

n = int(input())
li = []

for i in range(n):
    a, b = map(int, input().split())
    li.append((a, b))
result = sorted(li, key=lambda x:(x[0], x[1]))

for a,b in result:
    print(a, b)