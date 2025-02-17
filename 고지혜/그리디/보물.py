import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# 작은값*큰값
a.sort()
b.sort(reverse=True)

sum = [a[i]*b[i] for i in range(n)]

sum_ = 0
for i in range(len(sum)):
    sum_ += sum[i]
    
print(sum_)
