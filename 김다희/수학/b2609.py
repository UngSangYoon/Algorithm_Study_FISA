# 최대공약수와 최소공배수
from math import sqrt

A, B = map(int, input().split())

def get_divisors(n):
	s = set()
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			s.add(i)
			s.add(n // i)
	return s

def get_GCD(a, b):
	set_a = get_divisors(a)
	set_b = get_divisors(b)
	return max(set_a & set_b)

print(int(get_GCD(A, B)))
print(int((A*B)/get_GCD(A, B)))