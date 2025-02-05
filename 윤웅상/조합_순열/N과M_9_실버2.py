'''
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1 
3 1
4 4 2
예제 출력 1 
2
4
예제 입력 2 
4 2
9 7 9 1
예제 출력 2 
1 7
1 9
7 1
7 9
9 1
9 7
9 9
예제 입력 3 
4 4
1 1 1 1
예제 출력 3 
1 1 1 1
'''
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()  # 입력된 숫자를 사전 순으로 정렬

choose = []
visited = [False] * N  # 각 숫자의 방문 여부를 기록

def permutation(level):
    if level == M:
        print(*choose)
        return

    prev = -1  # 같은 숫자가 연속으로 선택되는 것을 방지하기 위해 이전 숫자 저장
    for i in range(N):
        # 방문하지 않았고, 이전 숫자와 다를 때만 선택
        if not visited[i] and lst[i] != prev:
            visited[i] = True  # 현재 숫자를 방문 처리
            choose.append(lst[i])
            prev = lst[i]  # 이전 숫자를 갱신
            permutation(level + 1)
            visited[i] = False  # 백트래킹
            choose.pop()

permutation(0)