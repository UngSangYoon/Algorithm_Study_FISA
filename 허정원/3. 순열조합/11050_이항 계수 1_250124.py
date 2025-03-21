'''
문제
자연수 
\(N\)과 정수 
\(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 
\(N\)과 
\(K\)가 주어진다. (1 ≤ 
\(N\) ≤ 10, 0 ≤ 
\(K\) ≤ 
\(N\))

출력
 
\(\binom{N}{K}\)를 출력한다.

예제 입력 1 
5 2
예제 출력 1 
10
'''

def fac(N):
    if N == 1 or N == 0:
        return 1
    return N * fac(N-1)

n, r = map(int, input().split())
print(int(fac(n) / (fac(r) * fac(n-r))))
