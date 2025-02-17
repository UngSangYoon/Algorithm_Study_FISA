'''
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''


n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
ans = float('inf')

for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = cnt2 = 0
        # 8×8 부분 보드를 순회합니다.
        for x in range(8):
            for y in range(8):
                # (x+y)가 짝수인 칸은 top-left 색과 같아야 함
                if (x + y) % 2 == 0:
                    if board[i + x][j + y] != 'W':  # top-left가 'W'인 경우
                        cnt1 += 1
                    if board[i + x][j + y] != 'B':  # top-left가 'B'인 경우
                        cnt2 += 1
                else:
                    if board[i + x][j + y] != 'B':  # top-left가 'W'인 경우
                        cnt1 += 1
                    if board[i + x][j + y] != 'W':  # top-left가 'B'인 경우
                        cnt2 += 1
        ans = min(ans, cnt1, cnt2)

print(ans)


'''
1. 8x8로 잘라서 체스판을 칠하기 때문에 n-7씩 이중 for문으로 순회하기
2. 체스판 색칠의 규칙을 찾아보면 무조건 짝수에는 맨위 왼쪽 칸과 색이 같고, 홀수 칸에는 그것과 다른 색이 칠해짐
3. 따라서 짝수 칸과 홀수칸을 기준이 되는 맨 위 왼쪽 칸의 색과 비교하며 다르면 정답인 cnt를 증가시켜줌
4. 8x8이 다양하게 나올 수 있기 때문에 맨 위 칸이 검정색이 경우와 흰색인 경우 중 더 작은 경우를 선택함
5. ans = float('inf')를 하는 이유는 그냥 가장 큰 값을 두고 cnt1과 cnt2 중 작은 값을 정하기 위함임임
'''