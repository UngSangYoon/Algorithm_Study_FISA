# 1026, 보물
# https://www.acmicpc.net/problem/1026
import sys

input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

result = sum([a[k] * b[k] for k in range(n)]) 

print(result)