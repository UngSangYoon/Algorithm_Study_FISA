import math

def lcm(a, b):
  return abs(a*b) // math.gcd(a, b)

n = int(input())
for i in range(n):
  a, b = map(int, input().split())
  print(lcm(a, b))
