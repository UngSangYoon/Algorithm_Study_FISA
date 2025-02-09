'''
어떤 수가 소수의 N제곱(N ≥ 2) 꼴일 때, 그 수를 거의 소수라고 한다.

두 정수 A와 B가 주어지면, A보다 크거나 같고, B보다 작거나 같은 거의 소수가 몇 개인지 출력한다.
'''

min , max = map(int, input().split())

from math import sqrt

N = max
is_prime = [True] * (N + 1)  # 처음에는 모두 true로 초기화
is_prime[1] = False  # 1은 소수가 아니므로

# 에라토스테네스의 체 알고리즘
for i in range(2, int(sqrt(N)) + 1):
    if not is_prime[i]: continue
    for j in range(2 * i, N + 1, i):
        is_prime[j] = False

for i in range(1, N + 1):
    print(i, is_prime[i])