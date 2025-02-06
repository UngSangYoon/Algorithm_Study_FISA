def combination(index, level):
	if level == 6:
		# 선택한 R 개의 원소를 출력
		print(*choose)
		return

	# for문
	for i in range(index, len(lst)): 
		choose.append(lst[i]) # 인덱스가 i인 원소를 선택(추가)
		combination(i+1, level+1) # 다음 for 문으로 들어가는 역할
		choose.pop() # (넣었던) 인덱스가 i인 원소를 제거
		
lst = []
choose = []
N_list = []

while True: 
    n = list(map(int, input().split()))
    n = n[1:]
    if n == []:
        break
    N_list.append(n)
		

for lst in N_list:
	combination(0,0)
	print()

