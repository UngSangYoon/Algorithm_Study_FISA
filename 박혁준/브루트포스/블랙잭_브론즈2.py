from itertools import combinations

def solution(n, li, ans):
	for i in list(combinations(li,3)):
		if sum(i) > n:
			continue
		if (n-sum(i))<(n-ans):
			ans = sum(i)

	return ans



ans = 0
n, k = map(int, input().split())
list_ = list(map(int, input().split()))

print(solution(k,list_,ans))


######