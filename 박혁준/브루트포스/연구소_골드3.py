def solution(li_):
	print(li_)

n, k= map(int,input().split())

list_ = [[0 for col in range(k)] for row in range(n)]
for i in range(0,n):
	list_[i] = list(map(int, input().split()))


for i in range(0, n):
	print(*list_[i]) # 리스트앞에 *붙이고 출력하면 내용만 출