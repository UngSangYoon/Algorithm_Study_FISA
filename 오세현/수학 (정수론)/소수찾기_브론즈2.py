'''
백준 1978번: 소수찾기_브론즈2
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''

from math import sqrt

#약수 구하는 함수
def divisors(n):
  d = set()

  for i in range(1, int(sqrt(n)) + 1):    
    if n % i == 0:
      d.add(i)
      d.add(n // i)
  return d
  
#소수 구하는 함수
def is_prime(n):
  return (len(divisors(n)) == 2)

#수의 개수 n 입력
n = int(input())

#n개의 수 입력
li1 = list(map(int, input().split()))

#소수 값 저장 변수
prime_n = 0

for i in range(n):
  if is_prime(li1[i]) == True:
    prime_n += 1

print(prime_n)
