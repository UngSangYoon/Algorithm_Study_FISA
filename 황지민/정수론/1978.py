'''
소수 찾기 - 1978

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력
4
1 3 5 7

예제 출력
3
'''

from math import sqrt

n = map(int, input().split())

numbers = list(map(int, input().split()))

def p(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

count = 0
for n in numbers:
    if p(n):
        count += 1

print(count)
