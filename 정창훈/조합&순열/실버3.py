'''
문제
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.
'''

import itertools

N = int(input())
numbers = list(range(1, N+1))

permutation = itertools.permutations(numbers)

for i in permutation:
    print(*i)