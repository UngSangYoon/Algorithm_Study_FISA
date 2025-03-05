# 1541, 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
import sys

input = sys.stdin.readline
s = input().split('-')
for i in range(len(s)):
	if i == 0:
		s_sum = sum(list(map(int, s[i].split('+'))))
	else:
		s_sum = s_sum - sum(list(map(int, s[i].split('+'))))
  
print(s_sum)