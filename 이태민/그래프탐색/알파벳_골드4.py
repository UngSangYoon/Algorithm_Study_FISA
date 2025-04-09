'''
알파벳 다국어
 
문제
세로 
$R$칸, 가로 
$C$칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 
좌측 상단 칸 ($1$행 $1$열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 
$R$과 
$C$가 빈칸을 사이에 두고 주어진다. ($1 ≤ R,C ≤ 20$) 둘째 줄부터 
$R$개의 줄에 걸쳐서 보드에 적혀 있는 $C$개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
'''

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
maxcnt = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, cnt, bitmask):
    global maxcnt
    maxcnt = max(maxcnt, cnt)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            idx = ord(board[nx][ny]) - ord('A')
            if not (bitmask & (1 << idx)):
                dfs(nx, ny, cnt + 1, bitmask | (1 << idx))

start_bit = 1 << (ord(board[0][0]) - ord('A'))
dfs(0, 0, 1, start_bit)
print(maxcnt)