a, b = map(int, input().split())

# 유클리드 호제법 사용
def gcd(a,b):
	if b == 0:
		return a
	return gcd(b, a%b)

def lcm(a,b,gcd):
	return a*b//gcd

g = gcd(a,b)
print(g)
print(lcm(a,b,g))