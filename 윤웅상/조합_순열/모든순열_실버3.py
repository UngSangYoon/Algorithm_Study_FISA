'''
문제
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

예제 입력 1 
3
예제 출력 1 
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''
N = int(input())
lst = list(range(1,N+1))
check = [False] * N # 원소 사용 여부를 체크
choose = []

def permutation(level):
	if level == N:
		# 나열한 R 개의 원소를 출력
		print(*choose)
		return

	# for문
	for i in range(0, N):
		if check[i] == True: # 인덱스가 i인 원소가 이미 사용중이라면 continue
			continue

		choose.append(lst[i]) # 인덱스가 i인 원소를 선택(추가) 
		check[i] = True # 인덱스가 i인 원소를 사용하고 있으므로 true로 초기화

		permutation(level+1) # 다음 for 문으로 들어가는 역할

		check[i] = False # 인덱스가 i인 원소의 사용이 끝났으므로 false로 초기화
		choose.pop() # (넣었던) 인덱스가 i인 원소를 제거

permutation(0)