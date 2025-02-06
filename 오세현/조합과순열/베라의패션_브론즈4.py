"""
백준 15439번 베라의 패션 브론즈4
문제
베라는 상의 N 벌과 하의 N 벌이 있다. i 번째 상의와 i 번째 하의는 모두 색상 i를 가진다. N 개의 색상은 모두 서로 다르다.

상의와 하의가 서로 다른 색상인 조합은 총 몇 가지일까?

입력
입력은 아래와 같이 주어진다.

N
출력
상의와 하의가 서로 다른 색상인 조합의 가짓수를 출력한다.
"""

"""
상의 빨 주 노 초 파
하의 빨 주 노 초 파

(빨,주) != (주,빨)

5개 중에 2개 뽑음 순서 있으므로 순열 5P2

"""
#라이브러리 사용
import itertools

n = int(input())

#n개의 수를 리스트에 저장
lst = list(range(n))

print(lst)

#n개 중에 2개 고르는 순열
np2 = itertools.permutations(lst, 2)  #순열을 리스트로 반환하는 함수

print(len(np2))