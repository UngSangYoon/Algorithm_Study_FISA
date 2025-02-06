"""
백준 11051번 이항 계수 2 실버2

문제
자연수 N과 정수 K가 주어졌을 때 이항 계수 nCk를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ K ≤ N)

출력
 
nCk를 10,007로 나눈 나머지를 출력한다.
"""

def mul_self(n, k):
    mul = 1
    for i in range(k):
        mul *= n
        n -= 1
    return mul

n, k = map(int, input().split())

print(mul_self(n, k) // mul_self(k, k) % 10007)


# math 라이브러리 이용
import math

def comb(n, k):
	return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))

n, k = map(int,input().split())

print(comb(n,k)%10007)