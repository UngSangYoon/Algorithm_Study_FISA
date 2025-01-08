'''
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
'''

from math import sqrt

a, b = map(int, input().split())

# 최대공약수
# 약수를 구한다.
def get_division(n):
    s = set()
    for i in range(1, n + 1):
        if n % i == 0: # 나머지가 0 인 경우
            s.add(i)
    return s

def get_GCD(a, b):
    set_a = get_division(a)
    set_b = get_division(b)
    return max(set_a & set_b) # 교집합 중 최대값.

# 최소공배수
# a x b = 최대공약수 x 최소공배수 임.
def get_LCM(a, b):
    return (a * b // get_GCD(a, b))

print(get_GCD(a, b))
print(get_LCM(a, b))