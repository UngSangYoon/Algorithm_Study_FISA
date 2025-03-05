# 2217, 로프
# https://www.acmicpc.net/problem/2217
import sys

input = sys.stdin.readline
n = int(input())
w = sorted([int(input()) for _ in range(n)], reverse = True)
w_max = -1

for i in range(n):
    w_max = max(w_max, w[i]*(i+1))

print(w_max)
