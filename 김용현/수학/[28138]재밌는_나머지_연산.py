

"""

16-4 의 약수
1 2 3 4 6 12
여기서 1 2 3 4 가 날라가는 이유?

--->

N % i = R 에서 i를 구하는 게 목적

N = ixk + R  (k=1,2,3,4,5....)

ixk = N-R

i>R (몫은 나머지보다 커야하니까)

i는 N-R의 약수

i>R인 약수만 고르면 된다.

"""



def func(N,R):
    m=N-R
    cnt=0
    for i in range(1,int(m**0.5+1)):
        if m%i ==0:
            if i>R:
                cnt+=i
            if R < m//i != i: # 대칭되는 약수가 만약 R보다 작고 i와 같은 수가 아니라면
                cnt+=m//i
    return cnt



N,R = map(int,input().split())

print(func(N,R))




