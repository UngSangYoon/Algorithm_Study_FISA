from itertools import combinations


def solution(n):

	return 0

n, k = map(int,input().split())
li_ = list(map(int,input().split()))
tmp = list()
f = filter(lambda a: a>0, li_)
for i in f:
	tmp.append(i)

print(tmp)