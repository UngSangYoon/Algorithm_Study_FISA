# 2025.01.12. Sun
"""
두 개의 자연수를 입력받아
최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다.
이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를
둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

"""

def get_divisor(n):
    s = set()
    for i in range(1, n+1):
        if n % i == 0:
            s.add(i)
    return s

def get_GCD_LCM(a, b):
    s1 = get_divisor(a)
    s2 = get_divisor(b)
    gcd = max(s1 & s2)
    lcm = int(a*b / gcd)
    return gcd, lcm

a, b = map(int, input().split())

gcd, lcm = get_GCD_LCM(a, b)

print(gcd, lcm)