
from itertools import combinations

n , k = map(int, input().split())
list_ = list(map(str, input().split()))

list_a = []
list_b = []

for i in list_ :
    if i in ["a","e","i","o","u"]:
        list_a.append(i)
    else:
        list_b.append(i)
combinations_a = []
for r in range(1, len(list_a) + 1):
    combinations_a.extend(combinations(list_a, r))

combinations_b = []
for r in range(2, len(list_b) + 1):
    combinations_b.extend(combinations(list_b, r))

result_set = set()
for a in combinations_a:
    for b in combinations_b:
        if len(a + b) == n:
            result_set.add("".join(sorted(a + b)))

sorted_results = sorted(result_set)
for i in sorted_results:
    print(i)

