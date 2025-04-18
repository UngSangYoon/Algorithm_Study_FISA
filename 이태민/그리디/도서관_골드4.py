'''
도서관
 
문제
세준이는 도서관에서 일한다. 
도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다. 
세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 
각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 
세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다. 
책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 
그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.

입력
첫째 줄에 책의 개수 N과, 세준이가 한 번에 들 수 있는 책의 개수 M이 주어진다. 
둘째 줄에는 책의 위치가 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 
책의 위치는 0이 아니며, 절댓값은 10,000보다 작거나 같은 정수이다.

출력
첫째 줄에 정답을 출력한다.

예제 입력 1 
7 2
-37 2 -6 -39 -29 11 -28
예제 출력 1 
131

예제 입력 2 
8 3
-18 -9 -4 50 22 -26 40 -45
예제 출력 2 
158
'''

n, m = map(int, input().split())
array = list(map(int, input().split()))

# 절대값이 가장 큰 수를 구한다.
max_value = max(array, key=abs)
max_value = abs(max_value)

# 음수와 양수 부분을 구분한다.
negative_array = sorted([abs(x) for x in array if x < 0], reverse=True)
positive_array = sorted([x for x in array if x > 0], reverse=True)

# 이동거리 저장
distance = 0

for i in range(0, len(positive_array), m):
    distance += positive_array[i] * 2
for j in range(0, len(negative_array), m):
    distance += negative_array[j] * 2

# 마지막 이동은 편도만 계산
distance -= max_value

print(distance)