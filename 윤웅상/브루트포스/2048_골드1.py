from itertools import product
# 브루트포스
# 이동 시 상하좌우(4개 경우의 수)
# 5번 이동하므로 4 ** 5 = 1024 의 경우의 수가 존재

def move_left(board, N):
    def merge(row):
        new_row = [num for num in row if num != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [num for num in new_row if num != 0]
        return new_row + [0] * (N - len(new_row))
    
    new_board = [merge(row) for row in board]
    return new_board

def move_right(board, N):
    return [list(reversed(row)) for row in move_left([list(reversed(row)) for row in board], N)]

def move_up(board, N):
    transposed = list(map(list, zip(*board)))
    moved = move_left(transposed, N)
    return list(map(list, zip(*moved)))

def move_down(board, N):
    transposed = list(map(list, zip(*board)))
    moved = move_right(transposed, N)
    return list(map(list, zip(*moved)))

N = int(input())
initial_board = [list(map(int, input().split())) for _ in range (N)]
ans = -1

key = ['l', 'r', 'u', 'd']
for command in product(key, repeat=5):
    board = initial_board
    for k in command:
        if k == 'l':
            board = move_left(board, N)
        elif k == 'r':
            board = move_right(board, N)
        elif k == 'u':
            board = move_up(board, N)
        elif k == 'd':
            board = move_down(board, N)
    m =max(map(max, board))
    if  ans < m:
        ans = m

print(ans)
