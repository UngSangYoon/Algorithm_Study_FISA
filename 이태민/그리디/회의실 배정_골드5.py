'''
문제
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
'''

import sys
input = sys.stdin.readline

def max_meetings(meetings):
    # 회의 종료 시간을 기준으로 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 0  # 선택된 회의 개수
    end_time = 0  # 마지막으로 선택된 회의의 종료 시간

    for start, end in meetings:
        if start >= end_time:  # 현재 회의가 마지막으로 선택된 회의와 겹치지 않으면
            count += 1  # 회의 개수 증가
            end_time = end  # 종료 시간 업데이트

    return count

n = int(input().strip())  # 회의 개수 입력
meetings = [tuple(map(int, input().split())) for _ in range(n)]  # 회의 시작 및 종료 시간 입력

result = max_meetings(meetings)  # 최대 회의 개수 계산
print(result)  # 결과 출력