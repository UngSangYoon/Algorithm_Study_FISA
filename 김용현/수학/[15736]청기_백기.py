"""
N명이 있다
n번째 선수가 n의 배수의 숫자들은 다 뒤집는다.
맨 마지막 백색이 위에 있는 경우?

초기 세팅 : 청이 모두 윗 방면

뒤집는 횟수가 홀수번인 깃발의 갯수를 세면 됩니다.

"""
"""
메모리 초과 ver
def common_divisor_ver2(N, memo):
    if memo[N] != 0:  
        return memo[N]

    cnt = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            cnt += 1
            if i != N // i:
                cnt += 1

    memo[N] = cnt 

def func(N):
    cnt = 0
    memo = [0] * (N + 1) 
    for i in range(1, N + 1):
        if common_divisor_ver2(i, memo) % 2 == 1:
            cnt += 1
    return cnt

N = int(input())
print(func(N))
"""

""" 그냥 제곱수 찾기"""

import math

N = int(input())

print(int(math.sqrt(N)))