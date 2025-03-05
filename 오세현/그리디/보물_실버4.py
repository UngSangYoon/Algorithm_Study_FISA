"""문제
보물 실버4
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.

길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다. N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

출력
첫째 줄에 S의 최솟값을 출력한다."""

import sys

n = int(sys.stdin.readline())

# a, b 배열 입력
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))


# b의 인덱스 번호를 저장한 후, 내림차순 배열하기
"""
enumerate(iterable, start=0) : 반복 가능한 객체를 인덱스 번호와 함께 튜플로 반환함

ex)
b = [2, 7, 8, 3, 1]
print(enumerate(b))
    -> [(0, 2), (1, 7), (2, 8), (3, 3), (4, 1)]
"""
# b의 원소값에 대하여 내림차순 정렬
b = sorted(enumerate(b), key=lambda x: x[1], reverse=True)
# [(0, 8), (1, 7), (2, 3), (3, 2), (4, 1)] 반환하게 됨

# a 원소 재배열
a = sorted(a, reverse=False)

s = 0
# S 최솟값 계산
for i in range(n):
    s += a[i] * b[i][1]

print(s)

