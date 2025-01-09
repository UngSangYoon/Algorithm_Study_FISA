n = int(input())
fac = 1
if n != 0:
    for i in range(1, n+1):
        fac *= i
print(fac)