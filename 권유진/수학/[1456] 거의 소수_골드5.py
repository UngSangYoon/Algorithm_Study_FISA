'''
문제
어떤 수가 소수의 N제곱(N ≥ 2) 꼴일 때, 그 수를 거의 소수라고 한다.

두 정수 A와 B가 주어지면, A보다 크거나 같고, B보다 작거나 같은 거의 소수가 몇 개인지 출력한다.

입력
첫째 줄에 왼쪽 범위 A와 오른쪽 범위 B가 공백 한 칸을 사이에 두고 주어진다.

출력
첫째 줄에 총 몇 개가 있는지 출력한다.

제한
1 ≤ A ≤ B ≤ 1014
예제 입력 1 
1 1000
예제 출력 1 
25
'''
import math

def prime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    else : 
        return True
    
A,B = map(int,input().split())
ans=0

while A<=B:
    if prime(A) and A*A<B:
        ans+=1
    A+=1

print(ans)
