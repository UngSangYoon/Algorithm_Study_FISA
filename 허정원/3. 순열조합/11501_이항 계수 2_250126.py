'''
문제
자연수 
\(N\)과 정수 
\(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 
\(N\)과 
\(K\)가 주어진다. (1 ≤ 
\(N\) ≤ 1,000, 0 ≤ 
\(K\) ≤ 
\(N\))

출력
 
\(\binom{N}{K}\)를 10,007로 나눈 나머지를 출력한다.

예제 입력 1 
5 2
예제 출력 1 
10

'''

import math
n, k = map(int, input().split())
comb = math.comb(n, k)
if comb < 10007:
  print(comb)
else: print(comb % 10007) 
