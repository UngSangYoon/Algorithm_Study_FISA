# 브루트포스 -> 노드 방문
#         -> 가능한 노드 이어서 계속 탐색
#         ->
# 답이 될 수 없는 경우 제외하고 탐색 -> 백트래킹
# 그리디 -> 최선의 선택이 무엇인지 모름
# DP -> DP 테이블의 크기가 너무 커짐

# DFS(깊이 우선 탐색)를 이용하여 보드에서 방문 가능한 최대 칸 수를 찾는 함수
def search(y, x):
    global dy, dx, R, C, board, check, cur_len, ans

    # 1. base case (종료 조건)
    # 현재 좌표 (y, x)가 보드의 범위를 벗어나면 더 이상 탐색할 수 없으므로 리턴
    if y < 0 or x < 0 or y >= R or x >= C:
        return

    # 현재 칸에 있는 알파벳이 이미 방문한 알파벳(check 리스트에서 True이면)
    # 중복 방문이 되므로 더 이상 진행할 수 없으므로 리턴
    if check[ord(board[y][x]) - ord('A')]:
        return

    # 2. 현재 칸의 알파벳을 방문 처리
    # board[y][x]는 현재 칸의 문자이며, 'A'를 뺀 값으로 인덱스를 얻는다.
    check[ord(board[y][x]) - ord('A')] = True

    # 현재 경로의 칸 수를 1 증가시킴 (현재 칸을 포함)
    cur_len += 1

    # 최대 칸 수(ans)를 현재 경로의 칸 수(cur_len)와 비교하여 갱신
    ans = max(ans, cur_len)

    # 3. 재귀적으로 상하좌우 탐색
    for i in range(4):
        ny = y + dy[i]   # 다음 행 위치 : y 좌표에 방향 벡터 dy를 더함
        nx = x + dx[i]   # 다음 열 위치 : x 좌표에 방향 벡터 dx를 더함
        # 재귀 호출로 다음 위치로 이동하여 탐색 진행
        search(ny, nx)

    # 4. 백트래킹 처리
    # 현재 칸에서 더 이상 이동할 수 없으므로, 현재 경로 길이에서 1 감소
    cur_len -= 1
    # 현재 칸의 알파벳 방문 표시를 해제하여 다른 경로에서 재방문 가능하도록 함
    check[ord(board[y][x]) - ord('A')] = False


# 방향 벡터: 상, 우, 하, 좌 순으로 이동할 때 좌표 변화량
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 입력 받기: 보드의 행의 수(R)와 열의 수(C)
R, C = map(int, input().split())
# 보드의 각 행을 입력받아 board 리스트에 저장
board = [input() for _ in range(R)]

# check 리스트: 알파벳 방문 여부를 저장하기 위한 리스트 (알파벳은 총 26개)
# check[i]가 True이면 해당 알파벳 (chr(i + ord('A')))을 이미 방문한 상태임을 의미
check = [False] * 26

# 현재까지 경로의 칸 수를 저장하는 변수
cur_len = 0
# 전체 탐색 과정에서 방문한 최대 칸 수를 저장하는 변수
ans = 0

# (0, 0) 위치(좌측 상단)에서 탐색 시작
search(0, 0)

# 최대 경로 길이(최대 방문 칸 수)를 출력
print(ans)