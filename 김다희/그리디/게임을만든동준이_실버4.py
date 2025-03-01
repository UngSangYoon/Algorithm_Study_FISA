# 2847, 게임을 만든 동준이
# https://www.acmicpc.net/problem/2847
import sys

input = sys.stdin.readline
n = int(input())
score = [int(input()) for _ in range(n)]
num = 0

for i in range(1, n):
    if score[n-i] <= score[n-i-1]:
        k = score[n-i] - 1
        num = num + (score[n-i-1] - k)
        score[n-i-1] = k

print(num)