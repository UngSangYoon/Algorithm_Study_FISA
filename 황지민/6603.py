# 6603.py
# 재귀-> 종료조건을 잘 생각해봐라

def combination(index, level):
	if level == 6:
		# 선택한 R 개의 원소를 출력
		
		print(' '.join(map(str,choose)))
		return

	# for문
	for i in range(index, k): 
		choose.append(lst[i]) # 인덱스가 i인 원소를 선택(추가)
		combination(i+1, level+1) # 다음 for 문으로 들어가는 역할
		choose.pop() # (넣었던) 인덱스가 i인 원소를 제거

while True:

	k, *lst = map(int, input().split())
	choose = []
	combination(0, 0)
	print()
    
	if k == 0:
		break 
    
    