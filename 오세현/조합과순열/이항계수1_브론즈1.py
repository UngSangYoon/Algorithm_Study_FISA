"""
백준 11050번 이항계수1 브론즈1

문제
자연수 N과 정수 K가 주어졌을 때 이항 계수
nCk를 구하는 프로그램을 작성하시오.

입력
첫째 줄에
n과 k가 주어진다.

출력
nCk
를 출력한다.

"""

#라이브러리 사용
import itertools

li1 = list(map(int, input().split()))

n = li1[0]
k = li1[1]

# 빈 리스트에 n까지의 수 집어넣기
n_li = []

for i in range(n):
    n_li.append(i)

#nCk 구하기
nck = list(itertools.combinations(n_li, k))  #순열을 리스트로 반환하는 함수

print(len(nck))