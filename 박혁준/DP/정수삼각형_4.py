# 1932 정수 삼각형 //4
# 품
'''
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.
'''

import sys

def solution(n, matrix):
    matrix[1][1] += matrix[0][1]
    matrix[1][2] += matrix[0][1]
    for i in range(2,n):
        matrix[i][1] += matrix[i-1][1]
        for j in range(2, len(matrix[i])-1):
            matrix[i][j] += max(matrix[i-1][j-1],matrix[i-1][j])
        matrix[i][-1] += matrix[i-1][-1]
    return max(matrix[-1])

n = int(input())

matrix = [[0] for _ in range(n)]
for i in range(n):
    matrix[i] = [0] + list(map(int, sys.stdin.readline().split()))
if n == 1 : print(matrix[0][1])
else : print(solution(n, matrix))
