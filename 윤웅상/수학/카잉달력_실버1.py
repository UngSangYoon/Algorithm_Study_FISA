# M = 10 이고 N = 12
# 1        2        3         4        5        6         7        8        9        10         11       12        13
# <1,1> -> <2,2> -> < 3,3> -> <4,4> -> <5,5> -> <6,6> - > <7,7> -> <8,8> -> <9,9> -> <10,10> -> <1,11>-> <2,12> -> <3,1>
# 10 20 30 40 50 60
# 12 24 48 60
# M과 N의 최소공배수가 멸망해이다. WHY? 그 때 둘다 <M,N>이 됨
# <x,y> 에서 x가 될수 있는 년 : M * ?  + x -> 기울기가 M이고 절편이 x인 일차함수
# <x,y> 에서 x가 될수 있는 년 : N * ?' + y -> 기울기가 N이고 절편이 y인 일차함수
# M * ? + x =  N * ?' + y 를 찾아야함
# [x, x+M, x+2M, x+3M, ....] 에서 -y를 한뒤 N으로 나누어떨어지는지만 확인하면 됨

# 유클리드 호제법 사용
def gcd(a,b):
	if b == 0:
		return a
	return gcd(b, a%b)

def lcm(a,b):
	return a*b//gcd(a,b)

def solve(m,n,x,y):
	end = lcm(max(m, n), min(m, n))
	year = x
	while year <= end:
		if (year - y) % n == 0:
			return year
		year += m
	return -1
	

t = int(input())
for _ in range(t):
    m, n, x, y = map(int,input().split())
    print(solve(m,n,x,y))