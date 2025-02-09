from itertools import permutations
# n, m = map(int,input().split())
# l = list(map(int,input().split()))

s= '1 2 3 4 2 5 3 1 1 2'
sets = list(map(int, s.split()))

data = permutations(sets, 5)

for i in data:
   print(i)