# 2579
'''
계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
'''

import sys

k = int(input())
array = []

for i in range(k):
    array.append(list(map(int,sys.stdin.readline().split())))
array = [lst + [0] for lst in array]
print(array)
answer = array

for i in range(2,k):
    if answer[i-1][1] != 1:
        if answer[i-1][0] > answer[i-2][0]:
            answer[i][0] += answer[i-1][0]
            answer[i][1] = 1
        else :
            answer[i][0] += answer[i-2][0]
    else :
        answer[i][0] += answer[i-2][0]

print(answer[-1][0])