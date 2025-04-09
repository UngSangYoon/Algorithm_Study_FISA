def search(lev):
	global row, col, square, matrix, pos

	# base case
	if lev == len(pos): # 스도쿠 완성
		for i in range(9): 
			for j in range(9):
				print(matrix[i][j], end=' ')
		exit(0)

	y, x = pos[lev]

	# recursive case
	for n in range(1, 10):
		if (not row[y][n]) and (not col[x][n]) and (not square[y // 3][x // 3][n]): # 행, 열, 3x3 구역에 숫자 n이 존재하지 않으면
			row[y][n] = col[x][n] = square[y // 3][x // 3][n] = True # 행, 열, 3x3 구역에 숫자 n이 존재하는 것으로 표시
			matrix[y][x] = n # 스도쿠 판에 숫자 n 채우기
			for i in range(9):
				for j in range(9):
					print(matrix[i][j], end=' ')
				print()
			search(lev + 1) # 다음 위치로 이동      

			matrix[y][x] = 0 # 채운 숫자 지우기
			row[y][n] = col[x][n] = square[y // 3][x // 3][n] = False # 행, 열, 3x3 구역에 숫자 n이 존재하지 않는 것으로 표시


#initial settings
row = [[False] * 10 for _ in range(9)] # 행 체크
col = [[False] * 10 for _ in range(9)] # 열 체크
square = [[[False] * 10 for _ in range(3)] for _ in range(3)] # 3차원 배열 9개 구역에 1~9 숫자 존재 여부 확인

# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
pos = [] # 0인 위치(채워야하는 숫자) 저장
for i in range(9):
	for j in range(9):
		cur = matrix[i][j]
		if cur == 0:
			pos.append((i, j))
		else:
			row[i][cur] = col[j][cur] = square[i // 3][j // 3][cur] = True

search(0)
