'''

수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!

'''


n = int(input())
classes = []
for _ in range(n):
    _class = list(map(int, input().split())) 
    classes.append(_class)

times = []


for start, end in classes:
	times.append((start, 1))
	times.append((end, -1))

times.sort()
max_time = 0
cnt = 0

for tmp in times:
	cnt += tmp[1]
	max_time = max(max_time, cnt)

print(max_time)

#########################################################33
'''
import sys
input = sys.stdin.read

data = input().splitlines()

n = int(data[0])
classes = []

for i in range(1, n + 1):
    start, end = map(int, data[i].split())
    classes.append((start, end))

times = []

for start, end in classes:
    times.append((start, 1))
    times.append((end, -1))

times.sort()

max_time = 0  # 최대 강의실 수
cnt = 0  # 현재 사용 중인 강의실 수

for time, change in times:
    cnt += change
    max_time = max(max_time, cnt)

print(max_time)

'''


#####