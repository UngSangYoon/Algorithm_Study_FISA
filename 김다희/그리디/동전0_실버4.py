# 11047, 동전 0
# https://www.acmicpc.net/problem/11047
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coin = []; num = 0

for i in range(n):
    value = int(input())
    coin.append(value)
coin = sorted(coin, reverse = True)

while k > 0:
    for j in coin:
        while k >= j:
            num = num + k//j
            k = k % j
    
print(num)
    
