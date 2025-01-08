'''
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

예제 입력 1 
24 18
예제 출력 1 
6
72
'''

a, b = map(int, input().split())

def get_divisors(x):
    set_S = set()
    for i in range(1, x+1):
        if x % i == 0 :
            set_S.add(i)

    return set_S

def gcd(y, z):
    set_a = get_divisors(y)
    set_b = get_divisors(z)
    return max(set_a & set_b)

g = gcd(a, b)
print(g)
print(int(a * b / g))

'''
완성
'''