'''
3초

문제
N부터 M까지의 수들을 종이에 적었을 때 종이에 적힌 0들을 세는 프로그램을 작성하라.

예를 들어, N, M이 각각 0, 10일 때 0을 세면 0에 하나, 10에 하나가 있으므로 답은 2이다.

입력
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 줄에는 N과 M이 주어진다.

1 ≤ T ≤ 20
0 ≤ N ≤ M ≤ 1,000,000
출력
각각의 테스트 케이스마다 N부터 M까지의 0의 개수를 출력한다.

예제 입력 1 
3
0 10
33 1005
1 4
예제 출력 1 
2
199
0
'''
# 하나하나 돌면서 자리수가 0이라면 0의 개수 +1 없다면 pass 방식
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b+1):
        lst = [int(digit) for digit in str(i)]
        for item in lst:
            if item == 0:
                cnt += 1

    print(cnt)

# count 함수 활용 방식
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    # 범위에 해당하는 수들의 집합
    nums = [i for i in range(a, b+1)]

    # 모든 수를 한 자리수로 쪼개서 저장
    lst = [int(digit) for num in nums for digit in str(num)]

    # 0의 개수 카운트
    print(lst.count(0))
