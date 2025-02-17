'''
문제
정수 
$N$을 $m$으로 나눈 나머지가 $R$이 되도록 하는 모든 양의 정수 
$m$의 합을 구하라.

입력
첫째 줄에 정수 
$N$과 $R$이 공백을 사이에 두고 주어진다. 

출력
정수 N을 m으로 나눈 나머지가 R이 되도록 하는 모든 양의 정수 m의 합을 출력한다. 조건을 만족하는 $m$이 없으면 0을 출력한다.

예제 입력 1 
16 4
예제 출력 1 
18

6, 12
'''
'''
n, r = map(int, input().split())

li = []
# 첫 시도 완전 탐색 -> 시간 초과 !
for i in range(1, n+1):
	if n % i == r:
		li.append(i)
print(sum(li))
'''

# 16 4
# 16 % i = 4
# 12 % i = 0
# 16 % i = 4 인 i 를 찾아야하자나
# 그렇다면 (16 - 4) % i = 0
# (n -r) 의 약수를 후보로 순회해보자!
# 12 의 약수 -> 1, 2, 3, 4, 6, 12
# r 보다 작은 약수는 나머지 연산 결과 r보다 작은 값을 반환하게 된다

'''
n, r = map(int, input().split())
x = n -r
li = []
for i in range(1, int(x**(1/2)) + 1):
    if x % i == 0:
        li.append(i)
        li.append(x//i)

li = list(filter(lambda t:t > r, li))

print(sum(li))
'''

# 위 코드가 틀린 이유
# 16 의 약수 -> [1, 16, 2, 8, 4, 4]
# 제곱수 중복 처리가 안됨!!
# 중복을 허용하지 않는 set을 사용하자

n, r = map(int, input().split())
x = n -r
s = set()
for i in range(1, int(x**(1/2)) + 1):
    if x % i == 0:
        s.add(i)
        s.add(x//i)

ans = list(filter(lambda t:t > r, s))

print(sum(ans))