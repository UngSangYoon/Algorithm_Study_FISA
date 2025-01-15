'''
문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

예제 입력 1 
10 11 12
예제 출력 1 
4
'''
# 분할 사용 (시간초과)

# 지수법칙 : a^(n+m) = a^n * a^m => A * sol(B) = A * sol(B//2) * sol(B//2)
# 모듈러 성질 : (a*b)%c = (a%c * b%c)%c

#거듭제곱하는 횟수(b) 값이 짝수라면 그대로 (X * X) % c 값을 반환하고,
#홀수라면 (a * (X * X)) % c 값을 반환

'''
시간초과 : 재귀 반복 수행 
A,B,C =map(int,input().split())

def sol(n): 
    if n==1:
        return A % C
    
    if n%2==0 :
        return sol(n//2) * sol(n//2) % C
    else :
        return (sol(n//2) * sol(n//2) * A) % C

print(sol(B))
'''

# n_half 로 결과 재활용 (재귀 여러번 X)
A,B,C =map(int,input().split())

def sol(n): 
    if n==1:
        return A % C

    n_half=sol(n//2)

    if n%2==0 :
        return n_half * n_half % C
    else :
        return (n_half * n_half * A) % C

print(sol(B))