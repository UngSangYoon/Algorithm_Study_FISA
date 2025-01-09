'''
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
'''
from math import sqrt

num = list(map(int, input('자연수 두개를 입력해주세요.(ex.1 2): ').split()))

def max_div(n):  # 최대공약수
    s = set()  # 교집합, 집합형은 중복 허용하지 않음.
    for i in range(1, n+1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return s

def get_gcd(a, b):
    a = max_div(a)
    b = max_div(b)
    return max(a & b)

def get_lcm(a, b):
    return (a * b // get_gcd(a, b))

print(f'최대공배수: {get_gcd(num[0], num[1])}')
print(f'최소공배수: {get_lcm(num[0], num[1])}')
