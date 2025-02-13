# 순열
N = int(input())

arr = list(range(1, N + 1))
check = [False] * N # 원소 사용 여부를 체크
# check[k] 가 true 이면 인덱스가 k인 원소가 사용중임을 나타냄.
# check[k] 가 false 이면 인덱스가 k인 원소가 사용중이지 않음을 나타냄.
choose = [] # 나열한 원소를 보관

def permutation(level):
	if level == N:
		# 나열한 R 개의 원소를 출력
		print(' '.join(map(str, choose)))
		return

	# for문
	for i in range(0, N):
		if check[i] == True: # 인덱스가 i인 원소가 이미 사용중이라면 continue
			continue

		choose.append(arr[i]) # 인덱스가 i인 원소를 선택(추가) 
		check[i] = True # 인덱스가 i인 원소를 사용하고 있으므로 true로 초기화

		permutation(level+1) # 다음 for 문으로 들어가는 역할

		check[i] = False # 인덱스가 i인 원소의 사용이 끝났으므로 false로 초기화
		choose.pop() # (넣었던) 인덱스가 i인 원소를 제거


permutation(0)