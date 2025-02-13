def combination(index, level):
	if level == 6:
		# 선택한 R 개의 원소를 출력
		print(" ".join(map(str, choose)))
		return

	# for문
	for i in range(index, k): 
		choose.append(arr[i]) # 인덱스가 i인 원소를 선택(추가)
		combination(i+1, level+1) # 다음 for 문으로 들어가는 역할
		choose.pop() # (넣었던) 인덱스가 i인 원소를 제거

# k가 0이 될 때까지 반복
while True:
    k, *arr = list(map(int, input().split()))
    if k == 0:
        break
    choose = [] # 선택한 원소를 보관       
    combination(0, 0)
    print() # 출력 형식 맞추기



