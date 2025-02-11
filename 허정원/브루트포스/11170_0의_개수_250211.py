'''
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

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    nums = [i for i in range(a, b+1)]
    lst = [int(digit) for num in nums for digit in str(num)]
    print(lst.count(0))
