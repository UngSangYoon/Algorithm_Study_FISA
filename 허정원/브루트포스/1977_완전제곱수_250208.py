'''
문제
M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하시오. 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 완전제곱수는 64, 81, 100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.

입력
첫째 줄에 M이, 둘째 줄에 N이 주어진다. M과 N은 10000이하의 자연수이며 M은 N보다 같거나 작다.

출력
M이상 N이하의 자연수 중 완전제곱수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 단, M이상 N이하의 자연수 중 완전제곱수가 없을 경우는 첫째 줄에 -1을 출력한다.

예제 입력 1 
60
100
예제 출력 1 
245
64
예제 입력 2 
75
80
예제 출력 2 
-1
'''

# 1. 런타임에러
import math
m = int(input())
n = int(input())

# 시작 & 끝 정수 찾기
start = int(math.sqrt(m)) # 64 -> 8
end = int(math.sqrt(n)) # 100 -> 10
lst = []

# 정수 범위랑 체크
for i in range(m, n+1):
  if start**2 <= i and end**2 >= i:
    lst.append(i**2)

# 출력
if len(lst) == 0:
  print(-1)
else: 
  print(sum(lst))
  print(min(lst))


# 2. lib 안쓰는 방법
m = int(input())
n = int(input())

lst = []
i = 0

while i * i < m:
  i += 1

while i * i <= n:
  lst.append(i**2)
  i += 1

if len(lst) == 0:
  print(-1)
else:
  print(sum(lst))
  print(min(lst))
