R, N = map(int, input().split())

lst = sorted(list(input().split()))

check = [False] * N # 원소 사용 여부를 체크
# check[k] 가 true 이면 인덱스가 k인 원소가 사용중임을 나타냄.
# check[k] 가 false 이면 인덱스가 k인 원소가 사용중이지 않음을 나타냄.
choose = [] # 나열한 원소를 보관

def combination(index, level):
	if level == R:
		# 나열한 R 개의 원소를 출력
		# 리스트 요소 중 모음 개수가 1개 이상이고 자음 개수가 2개 이상인 경우만 출력
		vowel_cnt = sum(str_ in 'aeiou' for str_ in choose)
		consonant_cnt = R - vowel_cnt
		if vowel_cnt >= 1 and consonant_cnt >= 2:
			print(''.join(choose))
		return

	# for문
	for i in range(index, N): 
		choose.append(lst[i]) # 인덱스가 i인 원소를 선택(추가)
		combination(i+1, level+1) # 다음 for 문으로 들어가는 역할
		choose.pop() # (넣었던) 인덱스가 i인 원소를 제거

combination(0, 0)