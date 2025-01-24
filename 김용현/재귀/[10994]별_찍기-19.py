N=int(input())



"""         처음에 잘못 푼 방법 -> 위 아래 나눠서 생각한 후 일일히 계산하면서 풀었음 """


"""
for i in range(1,N*4-3+1):
    for j in range(1,N*4-3+1):
        # 윗 영역
        if i<=(N*4-3)/2+1:
            if i%2 ==1:
                if (j<i and j%2==0 )or (N*4-3-i<j and j%2==0):
                    print(' ',end='')
                    continue

            else:
                if (j<i and j%2==1) or (N*4-3-i<j and j%2==1):
                    print('*',end='')
                    continue
                else:
                    print(' ',end='')
                    continue
        # 아래 영역
        else :
            if i%2 ==1:
                if (j < N*4-3-i+1 and j % 2 == 0) or (i < j and j % 2 == 0):
                    print(' ', end='')
                    continue
            else:
                if (j<N*4-3-i+1 and j%2==1) or (i<j and j%2==1):
                    print('*',end='')
                    continue
                else:
                    print(' ',end='')
                    continue
        print('*',end='')
    print()
    
"""

""" 
    아래의 방법은 큰 사각형안에 작은사각형 그 안에 사각형 이라는 규칙을 발견 한 후 재귀 방법을 사용했음 
    재귀의 방법을 사용할 것이기 때문에 작은 사각형에서 큰 사각형을 그리는 것이 아니라 겉 -> 속으로 들어가는 방식을 취함
"""

def draw(grid, start, size):
    if size <= 0:
        return
    end = start + size - 1

    # 현재 사각형의 테두리 그리기
    for i in range(start, end + 1):
        grid[start][i] = '*'  # 위
        grid[end][i] = '*'    # 아래
        grid[i][start] = '*'  # 좌
        grid[i][end] = '*'    # 우

    # 내부 사각형으로 이동
    draw(grid, start + 2, size - 4)


size = 4 * N - 3 # 격자 크기는 4n-3으로 설정되어있음
grid = [[' ' for _ in range(size)] for _ in range(size)] # 2차원 배열 생성해줌


draw(grid, 0, size)

print('\n'.join(map(''.join, grid)))