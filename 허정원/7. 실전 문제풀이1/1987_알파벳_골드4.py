'''
문제
세로 
$R$칸, 가로 
$C$칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (
$1$행 
$1$열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 
$R$과 
$C$가 빈칸을 사이에 두고 주어진다. (
$1 ≤ R,C ≤ 20$) 둘째 줄부터 
$R$개의 줄에 걸쳐서 보드에 적혀 있는 
$C$개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
'''

# 강의 참고
# 백트래킹

def search(y, x):
	global dy, dx, R, C, board, st, ans

	# base case
	if y < 0 or x < 0 or y >= R or x >= C: # 경계 밖이거나, 이미 밟은 거면 돌아감
		return
	if board[y][x] in st:
		return
	st.add(board[y][x]) # 현재 위치 처리

	ans = max(ans, len(st))

	# 상하좌우 이동
	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]
		search(ny, nx)

	st.remove(board[y][x])

# 이동 방향
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

R, C = map(int, input().split())
board = [input() for _ in range(R)]

# 상태 저장 변수
st = set() # 현재까지 밟은 알파벳 저장
ans = 0 # 최대 몇 개까지 밟았는지 저장

search(0, 0)

print(ans)
