'''
문제
정수 
$N$을 
$m$으로 나눈 나머지가 
$R$이 되도록 하는 모든 양의 정수 
$m$의 합을 구하라.

입력
첫째 줄에 정수 
$N$과 
$R$이 공백을 사이에 두고 주어진다. (
$1 \le N \le 10^{12}; 0 \le R \lt N$)

출력
정수 
$N$을 
$m$으로 나눈 나머지가 
$R$이 되도록 하는 모든 양의 정수 
$m$의 합을 출력한다. 조건을 만족하는 
$m$이 없으면 0을 출력한다.

예제 입력 1 
16 4
예제 출력 1 
18
조건을 만족하는 
$m$에는 
$6$과 
$12$가 있다.

예제 입력 2 
6 0
예제 출력 2 
12
예제 입력 3 
12 8
예제 출력 3 
0
'''

import math

n, k = map(int, input().split())

def get_divisors(n, k):
    s = set()
    for i in range(1, int(math.sqrt(n - k))+1):
        if (n - k) % i == 0:
            if i > k:
                s.add(i)
            if i != (n-k)//i and (n-k)//i >k:
                s.add((n-k)//i)

    if not s:
        return 0
    else:
        return sum(s)

print(get_divisors(n, k)) 