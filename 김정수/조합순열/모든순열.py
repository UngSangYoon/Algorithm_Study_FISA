'''
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.
'''

from itertools import permutations

n = int(input())
product=[]

for i in range(1,n+1):
    product.append(i)


ans = list(permutations((product), n))

for num in ans:
    for _ in num:
        print(_, end=' ')
    print()


