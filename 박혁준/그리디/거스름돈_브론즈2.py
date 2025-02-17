def solution(n):
	cnt = 0
	tmp = 1000-n
	for i in [500,100,50,10,5,1]:
		j = tmp//i
		cnt += j
		tmp-=j*i

	return cnt

n = int(input())
print(solution(n))

#####